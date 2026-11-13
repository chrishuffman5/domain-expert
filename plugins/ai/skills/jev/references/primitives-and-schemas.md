# Primitives and schemas: Choice, Score, Noul, Box, state, images, confidence

Field-level reference for the jev request payload. Read this when writing or debugging a `questions` map, choosing a primitive, attaching images, or interpreting an answer. The payload is the same on every System One transport; only the envelope differs (direct API: `model` inside the body; Cloudflare: `model` beside `input`). Envelopes: `api-and-sdks.md`, `cloudflare-workers-ai.md`.

## Request shape

> Source: https://docs.typesafe.ai/api/system-one.md
> Source: https://api.typesafe.ai/openapi.json
> Source: https://docs.typesafe.ai/concepts/state.md

One request = one `state` + a map of named `questions`. Every question is evaluated against the same state, **in parallel and in isolation**; answers come back keyed by the same names.

| Field | Type | Notes |
|---|---|---|
| `model` | string, required | No enum in the spec (examples `jev-latest`, `jev-preview`); versioned ids such as `jev-1.14.0` accepted. |
| `state` | string \| object \| array, required | Text and images; audio and video unsupported. |
| `questions` | object, ≥ 1 entry | Discriminated by `type`: `noul`, `choice`, `score`, `box`. |
| `assets` | object, optional (≥ 1 if present) | Image assets keyed by reference string; see Images. |

- Headers: `TypeSafe-Danger-Zone-Images: true` (required for any `assets` or `box`), `TypeSafe-Danger-Zone-Long-Context: true` (raises 64k/32k to 262k).
- State shapes: a string; an **object** (recommended: named fields keep ticket, order and policy unambiguous, and structured `instructions` can reference fields in backticks, e.g. "``Is `message.text` toxic?``"); an array (a message thread or several records as *one* context, not a batch).
- English is most accurate. 1.14's headline change is better multilingual support; still test non-English input before relying on it.
- OpenAPI `info.version` is 0.2.0 and carries no model version.

## Choice: one option from an unordered set

> Source: https://docs.typesafe.ai/primitives/choice.md
> Source: https://docs.typesafe.ai/patterns/companion-noul.md
> Source: https://docs.typesafe.ai/cookbooks/classification_using_confidence.md

| Request field | Type | Notes |
|---|---|---|
| `type` | `"choice"` | |
| `instructions` | string \| object \| array \| null | The question. |
| `criteria` | object, 1–255 entries | Option key → description (string, `null`, object or array). Jev sees the keys, so name them meaningfully (`desk_pro`, not `opt3`). |

Response: `choice` (top option), `probabilities` (option → 0–1, sum ≈ 1), `confidence`.

- Give the complete taxonomy. A Choice "works reliably up to roughly 240 options"; deeper taxonomies chain one Choice per level and beam-search over the probabilities (hierarchical-classification cookbook).
- **A Choice always picks something**, sometimes with high probability, even when nothing fits (a desk lamp routed to `desk_pro` at 0.96). CHANGED: the vendor now recommends a **companion Noul** ("does any option fit?") over an `other` option, because `other` competes for probability and splits mixed inputs. Use the Choice only when the Noul is a clear yes.
- When an input can match several options, ask one Noul per option instead of one Choice.

## Score: a position on an ordered rubric

> Source: https://docs.typesafe.ai/primitives/score.md
> Source: https://docs.typesafe.ai/patterns/confidence-routing.md

| Request field | Type | Notes |
|---|---|---|
| `type` | `"score"` | |
| `instructions` | string \| object \| array \| null | What is rated. |
| `criteria` | array, lowest first | **2–10 levels** in prose; the OpenAPI spec and API reference say 1–10. Use ≥ 2. |

Response: `score` (Σ level × probability; fractional), `confidence`, `probabilities` (level index → 0–1; string keys on the wire, int keys in the Python SDK), `legend` (index → description).

- Each level is judged independently; the model never sees level numbers or neighbours. Write levels as concrete situations ("Major with no workaround: users cannot complete a core task"), one dimension per question, rare-but-critical extremes as their own level. Avoid numeric-only and relative wording.
- Identical scores can hide different distributions; read `probabilities`.
- **Adjacent-level trap**: Score confidence treats mass on a neighbouring level as only a small spread, so an answer split across a threshold boundary can pass a confidence check and land on the wrong side. When an action depends on a boundary, sum the probabilities on the side that matters (`p[3] + p[4] >= 0.3`).
- Normalise for composite scoring with `score / (len(criteria) - 1)`. Never read a Score as a magnitude ("weak numerical calibration").

## Noul: yes/no, where the probability is the answer

> Source: https://docs.typesafe.ai/primitives/noul.md
> Source: https://docs.typesafe.ai/confidence.md

| Request field | Type | Notes |
|---|---|---|
| `type` | `"noul"` | |
| `instructions` | string \| object \| array \| null | A question or a statement. |
| `criteria` | `{true, false}`, optional | Clarifies a subtle boundary; list concrete cases in `false` ("newsletters, receipts, a thank-you note that needs no reply"). |

Response: `{"type":"noul","noul":0.99}`, P(yes). **No `confidence` field.** 0.5 means uncertain, not "medium". Suggested starting thresholds: **> 0.7 yes, < 0.3 no**, with the band between as its own outcome. An optional certainty measure is `|2p − 1|`.

Never write criteria where `true` describes a "no" (jaggedness item 7).

## Box: where is it in the image (Jev 1.14, "dreamer-ready")

> Source: https://docs.typesafe.ai/primitives/box.md
> Source: https://docs.typesafe.ai/api/system-one.md

- Request: `type: "box"` and `instructions` (what to find, and in which image). **No `criteria`.** Needs an image in the request and the Images header. Box requires `jev-1.14.0`; 1.13 rejects it.
- Answer: `box` = `{top, bottom, left, right}`, each a 0–1 fraction of image height or width from the top-left (left < right, top < bottom), resolution-independent; plus `confidence`, which is **nullable** (`null` when the model does not provide it). The confidence page does not cover Box.
- **No "not found" answer**: a box always comes back. Pair every Box with a Noul ("Is there a coffee mug in `photo`?") and ignore the box when the Noul is low.
- One target per question. Small targets in large images can be missed: locate the region first, then Box on a tile and convert coordinates back.
- Docs pattern: crop with PIL by multiplying edges by width and height; pad low-confidence boxes (example values `PAD = 0.05`, `MIN_CONFIDENCE = 0.6`; no recommended threshold).

## Images (1.13 and 1.14, "dreamer-ready")

> Source: https://docs.typesafe.ai/images.md

- Opt in per request with `TypeSafe-Danger-Zone-Images: true`. Not recommended for production.
- Images go anywhere text can: `state`, `instructions`, Choice option descriptions, Score levels, Noul `true`/`false`.
- Top-level `assets` map: each asset has `type: "image"` and either `part` (a multipart file name; wins if both) or `data_base64` + `format` (`png`, `jpg`, `jpeg`; real format detected from bytes). Base64 is standard with padding, no whitespace, no `data:` prefix.
- References are matched as **plain text** anywhere in string values (object keys are not replaced): ≤ 1,024 bytes each, 65,536 total. Use UUIDs or delimited names like `<product>`. **Every asset must be referenced**, or 400.
- Multipart is recommended (base64 adds ~33%): first part `request` (JSON), then one uniquely named file part per image, each used by exactly one asset.
- Limits: PNG/JPEG stills (animated PNG rejected), 16 MiB per file, each side 280–1,568 px, 78,400–2,458,624 total pixels, 32 MiB body. Never resized; EXIF orientation not applied; convert GIF/WebP/HEIC first.
- **An image in `instructions` is sent once per question that uses it.** Put shared images in `state` and refer to them by field name.
- Billing: image tokens are ordinary input tokens. No separate rate limits.

## Structured content inside questions

> Source: https://docs.typesafe.ai/primitives/advanced.md

`instructions` and every criteria position accept string, object, array or `null` on all four primitives. SDK type names: `JSONContent` (Python), `EntryType` (JS). Documented shapes: an `instructions` object with `question` + `focus`; Choice options as `{what, not_for, examples}`; Score levels as `{summary, signals}`; a decision tree of sequential Choices.

## Confidence and probabilities

> Source: https://docs.typesafe.ai/confidence.md
> Source: https://docs.typesafe.ai/patterns/probability-routing.md
> Source: https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai

CHANGED: formulas are now published.
- **Choice**: `(p_max − 1/n) / (1 − 1/n)`. It is a function of the top probability, so for a fixed option count a threshold on `confidence` adds nothing over `probabilities[choice]`.
- **Score**: spread from the most likely level weighted by level distance, floored at 0.
- **Noul**: none returned; optional `|2p − 1|`.
- Values are rounded to two decimals, so probabilities may not sum to exactly 1.

Which number to act on (vendor guidance): pick the top option with no threshold when you only need the best option; when code must decide whether to act, threshold the **probability** (`noul`, or `probabilities[choice]`); use **confidence** for Score, plus boundary sums. Starting bands: act automatically above 0.9 on high-stakes actions, confirm in the middle, route to a person below a floor such as 0.5; tune on your own labelled data (third-party data shows 0.9+ is not 90% accuracy, see `limitations-and-security.md`).

## Sample responses (recorded on jev-1.14.0)

> Source: https://docs.typesafe.ai/patterns/confidence-routing.md
> Source: https://docs.typesafe.ai/patterns/companion-noul.md

```json
{"model": "jev-1.14.0",
 "answers": {"severity": {"type": "score", "score": 3.19, "confidence": 0.34,
   "legend": {"0": "Cosmetic: wording, layout, or styling only",
              "1": "Minor: something misbehaves, but users can still do what they wanted",
              "2": "Major with a workaround: a feature is broken, but there is another way to get the job done",
              "3": "Major with no workaround: users cannot complete a core task",
              "4": "Critical: data loss, a security hole, or the product is down for everyone"},
   "probabilities": {"0": 0.01, "1": 0.14, "2": 0.07, "3": 0.19, "4": 0.59}}},
 "usage": {"input_tokens": 435, "output_tokens": 17}}
```
```json
{"model": "jev-1.14.0",
 "answers": {"product": {"type": "choice", "choice": "desk_pro", "confidence": 0.94,
                         "probabilities": {"desk_pro": 0.96, "chair_lite": 0.01, "monitor_arm": 0.03}},
             "about_our_product": {"type": "noul", "noul": 0.02}},
 "usage": {"input_tokens": 549, "output_tokens": 63}}
```
Box answer shape: `{"type":"box","box":{"top":0.2,"bottom":0.66,"left":0.19,"right":0.68},"confidence":null}`.

## Sources
- https://docs.typesafe.ai/api/system-one.md
- https://api.typesafe.ai/openapi.json
- https://docs.typesafe.ai/concepts/state.md
- https://docs.typesafe.ai/introduction.md
- https://docs.typesafe.ai/primitives/choice.md
- https://docs.typesafe.ai/primitives/score.md
- https://docs.typesafe.ai/primitives/noul.md
- https://docs.typesafe.ai/primitives/box.md
- https://docs.typesafe.ai/primitives/advanced.md
- https://docs.typesafe.ai/images.md
- https://docs.typesafe.ai/confidence.md
- https://docs.typesafe.ai/patterns/companion-noul.md
- https://docs.typesafe.ai/patterns/confidence-routing.md
- https://docs.typesafe.ai/patterns/probability-routing.md
- https://docs.typesafe.ai/cookbooks/classification_using_confidence.md
- https://docs.typesafe.ai/cookbooks/hierarchical_classification.md
- https://docs.typesafe.ai/agent-skill.md
- https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai

Fetched: 2026-11-13
