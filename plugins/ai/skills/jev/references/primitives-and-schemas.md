# Primitives and schemas: Choice, Score, Noul, state, structured content

Field-level reference for the jev evaluation payload. Read this when you are writing or debugging a `questions` map, deciding between primitives, or interpreting an answer object. The payload is the same on every transport. Only the envelope differs: on the direct API `model` sits inside the body, and on Cloudflare `model` is outside the payload. See `api-and-sdks.md` and `cloudflare-workers-ai.md` for the envelopes.

## Request shape

> Source: https://docs.typesafe.ai/api.md
> Source: https://docs.typesafe.ai/concepts/state.md

One call carries one `state` and a map of named `questions`. Every question is evaluated against the same state, in parallel and in isolation, so one question cannot leak into another. Answers come back keyed by the same names.

| Field | Type | Notes |
|---|---|---|
| `state` | string \| object \| array | Content to evaluate. Text only: no images, audio or video. |
| `model` | string | Direct API only, and required there, e.g. `jev-latest`. It is not part of the Cloudflare payload. |
| `questions` | object | Map of name → question. It must not be empty; the JS SDK throws on an empty map. |

State shapes:
- **String**: a single text, e.g. `"My card was charged twice."`
- **Object**: the recommended shape for most requests. Named fields keep related records (ticket + order + policy) unambiguous.
- **Array**: sequences such as a message thread or several records.

Language: English gets the best accuracy. Other languages, CJK included, are accepted "but currently have lower accuracy". Test before you rely on non-English input.

## Choice: pick one of an unordered set

> Source: https://docs.typesafe.ai/primitives/choice.md

| Request field | Type | Required | Notes |
|---|---|---|---|
| `type` | `"choice"` | yes | |
| `instructions` | string \| object \| array | yes | The question. |
| `criteria` | object | yes | Option name → description. A value may be a string, `null`, an object or an array. |

Limit: **255 options at most**. Include an `"other"` / `"none of the above"` option when the taxonomy may be incomplete.

| Response field | Type | Notes |
|---|---|---|
| `choice` | string | The option with the highest probability. |
| `probabilities` | object | Option → 0–1, summing to 1. |
| `confidence` | number 0–1 | High when the mass is concentrated on one option. |

```json
{
  "state": "My running shoes arrived in the wrong size. Can I swap them for a size 10?",
  "model": "jev-latest",
  "questions": {
    "department": {
      "type": "choice",
      "instructions": "Which team should handle this?",
      "criteria": {
        "returns": "Exchanges, wrong or damaged items",
        "shipping": "Delivery status, delays, lost packages",
        "billing": "Charges, invoices, payment problems"
      }
    }
  }
}
```
Response: `{"type":"choice","choice":"returns","confidence":1.0,"probabilities":{"shipping":0.0,"returns":1.0,"billing":0.0}}`.

Documented practice:
- Supply the complete taxonomy, not a shortlist.
- Route low confidence to manual review. The docs suggest a threshold around 0.3–0.5 for Choice.
- For deep taxonomies, chain Choice questions one level at a time and beam-search over the probabilities.

## Score: a position on an ordered rubric

> Source: https://docs.typesafe.ai/primitives/score.md

| Request field | Type | Required | Notes |
|---|---|---|---|
| `type` | `"score"` | yes | |
| `instructions` | string \| object \| array | yes | What is being rated. |
| `criteria` | array | yes | Ordered level descriptions, lowest first. **2–10 levels.** |

| Response field | Type | Notes |
|---|---|---|
| `score` | number | Probability-weighted position from 0 to the top level. It can be fractional. |
| `confidence` | number 0–1 | Derived from how concentrated the probability is. |
| `probabilities` | object | Level number (as a string on the wire, as an int key in the Python SDK) → 0–1. |
| `legend` | object | Level number → its description. |

Formula: `score = Σ(level_i × probability_i)`. Example: levels 0/1/2 at probabilities 0.0/0.57/0.43 give a score of 1.43. Each level is judged independently against the state. The model does not see level numbers or neighbouring levels.

Writing levels:
- **Do:** describe concrete situations ("Broken or degraded feature, but workaround exists"), keep one dimension per question, and give rare but critical extremes their own level.
- **Avoid:** numeric-only labels ("0", "1", "2"), relative wording ("worse than the previous level"), and overlapping or multi-dimensional criteria.

Reading a score:
- An integer score means all the mass sits on one level. A fractional score means the mass is split.
- Identical scores can come from different distributions, so always inspect `probabilities` and `confidence`.
- Round to the nearest level when you need a discrete outcome.
- Low confidence usually signals overlapping levels, a multi-dimensional judgment, or thin state.

Composite scoring: use one Score per dimension, normalize each with `score / (len(criteria) - 1)`, weight in code, and sum.

SDK note: since SDK 0.6.0 (both languages), `Score.criteria` is an ordered sequence. It is no longer an int-keyed dict. See `versions/jev-1.13.md`.

## Noul: yes/no, where the probability is the answer

> Source: https://docs.typesafe.ai/primitives/noul.md

| Request field | Type | Required | Notes |
|---|---|---|---|
| `type` | `"noul"` | yes | |
| `instructions` | string \| object \| array | yes | The yes/no question or statement. |
| `criteria` | `{ "true": ..., "false": ... }` | **no** | Clarifies a subtle yes/no boundary. |

Response: `{"type":"noul","noul":0.99}`. `noul` is the probability that the answer is yes. There is **no `confidence` field**: the single number is the whole signal. A value near 0.5 means uncertain, not "medium". Vendor wording: "A Noul value runs from 0 to 1, but it's not a scale of the thing you asked about."

Practice: ask one condition per Noul, so "angry AND wants refund" becomes two Nouls. Add `criteria.true`/`criteria.false` when the boundary is subtle. Batch several Nouls in one request. Apply thresholds in code, not in the prompt.

## Structured (JSON) content inside questions

> Source: https://docs.typesafe.ai/primitives/advanced.md

Four positions accept a string, an object, an array or `null` in place of plain text: `instructions` (all primitives), Choice `criteria` values, Score `criteria` entries, and Noul `criteria.true`/`criteria.false`. The SDKs call this type `EntryType` (JS) and `JSONContent` (Python).

Use structure when a question has labelled parts, or when the source data is already structured. Documented shapes:
- An `instructions` object with `question` + `focus`.
- Choice options as `{what, not_for, examples}`.
- Score levels as `{summary, signals}`.
- A decision tree of sequential Choice questions, one per taxonomy level.

Structured `instructions` can reference state fields in backticks (source: https://docs.typesafe.ai/api.md).

## Machine-checked JSON Schemas (Cloudflare-published)

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/schema-input.json
> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/schema-output.json

These are JSON Schema 2020-12 documents for the evaluation payload.

**Input:**
- Top level is `{state, questions}`, both required, with `additionalProperties: false`. There is no `model` property.
- `state` accepts string, object, array or `null`.
- Each question is `oneOf` noul / choice / score. Every variant has `additionalProperties: false`.
- Noul: `criteria` may be `{true?, false?}` or `null`. Required fields are `type` and `instructions`.
- Choice: required fields are `type`, `instructions` and `criteria` (an object).
- Score: required fields are `type`, `instructions` and `criteria` (an array, `minItems: 2`).

The schema does **not** encode the 255-option or 10-level maxima. Those limits exist only in the prose docs, so enforce them yourself before sending.

**Output:**
- Top level is `{model, answers, usage}`, all required.
- noul answer: `{type, noul}`, with `noul` between 0 and 1.
- choice answer: `{type, choice, probabilities, confidence}`.
- score answer: `{type, score, legend, probabilities, confidence}`. `score` has no min/max in the schema.
- `usage` is `{input_tokens, output_tokens}`, both non-negative integers.

## Full multi-primitive example (Cloudflare model card)

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "is_urgent": { "type": "noul", "noul": 0.95 },
    "department": { "type": "choice", "choice": "billing", "confidence": 0.8,
      "probabilities": { "billing": 0.87, "sales": 0, "technical": 0.13 } },
    "frustration": { "type": "score", "score": 1.04, "confidence": 0.94,
      "legend": { "0": "Calm", "1": "Frustrated", "2": "Very angry" },
      "probabilities": { "0": 0, "1": 0.96, "2": 0.04 } }
  },
  "usage": { "input_tokens": 426, "output_tokens": 73 }
}
```

## Confidence

> Source: https://docs.typesafe.ai/confidence.md

Confidence is a 0–1 statistic derived from the Choice or Score distribution. It is near 1 when one option dominates and near 0 when the distribution is flat. The exact formula is not published: the docs say only that it considers how far the top probability exceeds chance, relative to the number of options.

Vendor starting bands:
- **>0.9**: act automatically.
- **0.5–0.9**: confirm or flag for review.
- **<0.5**: route to a human.

Scale thresholds with the consequence of the action. Start conservative and tune on your own data.

## Sources
- https://docs.typesafe.ai/api.md
- https://docs.typesafe.ai/concepts/state.md
- https://docs.typesafe.ai/primitives/choice.md
- https://docs.typesafe.ai/primitives/score.md
- https://docs.typesafe.ai/primitives/noul.md
- https://docs.typesafe.ai/primitives/advanced.md
- https://docs.typesafe.ai/confidence.md
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://developers.cloudflare.com/ai/models/typesafe/jev/schema-input.json
- https://developers.cloudflare.com/ai/models/typesafe/jev/schema-output.json

Fetched: 2026-09-23
