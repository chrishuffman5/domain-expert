---
name: jev
description: "TypeSafe AI Jev/System One API and SDK operations: Jev 1.14/1.13, Choice/Score/Noul/Box schemas, state design, probability gates, image and long-context headers, direct /v1/systemone HTTP, typesafe-sdk (Python) and @typesafe-ai/sdk (JS), third-party purchase routes (Cloudflare typesafe/jev, Vercel AI Gateway, OpenRouter, DigitalOcean, Databricks), 401-vs-403 and other errors, limits, pricing, weaknesses, and porting jev code to wire-compatible APIs (Gemini/OpenAI Decisions shape differences, local /v1/systemone servers such as Kev and Ollama). WHEN: Jev, Jev 1.14, Jev 1.13, TypeSafe, typesafe.ai, systemone, system_one, typesafe/jev, typesafe-sdk, @typesafe-ai/sdk, Noul, Box question, jev-latest, Jev API/SDK/integration. DO NOT use for prompt-injection threat modeling (`ai-security`), MCP (`mcp`), agent loops/CLI harnesses, generic provider routing (`inference-providers`), general LLM choice (`model-selection`), LLM-as-judge (`evals`), Lightbend Typesafe/Scala, or deciding whether Jev fits versus other models and source-traced catalog comparisons; route model identity and suitability to `ai-models-specialist` when `ai-models` is installed."
license: MIT
---

# Jev (TypeSafe AI)

Jev is TypeSafe AI's hosted "System One" model. You send one `state` plus a map of typed questions; it returns typed answers with calibrated probabilities that your code acts on. It does not generate text. TypeSafe's own framing: "Jev makes judgments, code makes decisions." This skill covers choosing primitives, calling jev on every documented route, acting on probabilities, cost and failure handling, its weaknesses, and porting jev code to wire-compatible APIs or local servers. For a source-traced comparison of Jev against other models or a decision about whether Jev fits a workload, use `ai-models-specialist` when installed; use this skill once Jev is selected and the task is its API, SDK, or integration mechanics.

## Volatility rule

Every fact here is a snapshot as of **2026-11-13**. Jev shipped 2026-09-15 and 1.14 followed on 2026-10-14; aliases, prices ("may be subsidized"), per-org rate limits, gateway surfaces (several `alpha`, `experimental` or preview) and competitor products all moved within weeks.
- Always re-check the cited URL before committing a model id, price or limit to config.
- Never state a figure this skill marks **not stated** or **unverified**. Say so and point to the page to check.

## Routing

| Request | Load |
|---|---|
| Field-level schemas, Box, images/assets, confidence formulas, sample responses | `references/primitives-and-schemas.md` |
| Runnable code: triage, gating, guardrails, LLM-output checks, moderation, scoring, Box, images, async, TS, AI SDK, LangChain, Pydantic AI | `references/examples.md` |
| Raw HTTP, Python `typesafe-sdk`, JS `@typesafe-ai/sdk`, env vars, retries, compression, pointing an SDK elsewhere | `references/api-and-sdks.md` |
| Buying jev outside TypeSafe: Vercel, OpenRouter, DigitalOcean, Databricks, Netlify, Requesty, LiteLLM, Portkey, "is it on Bedrock/Azure/Vertex?" | `references/purchase-routes.md` |
| `env.AI.run('typesafe/jev')`, Cloudflare REST, Cloudflare AI Gateway, Cloudflare billing questions | `references/cloudflare-workers-ai.md` |
| Fan-out, Noul screen, companion Noul, confidence/probability routing, composite scoring, hybrid with an LLM | `references/patterns.md` |
| Jaggedness, 1.14 caveats, injection evidence, tool-call gating, privacy, DPA, MCA, Trust Center, status | `references/limitations-and-security.md` |
| Cost math, 64k/32k/262k limits, 32 MiB rules, full error table, 401-vs-403 defect, retry defaults | `references/pricing-limits-errors.md` |
| Which APIs are wire-compatible with jev's, porting jev code to or from Gemini/OpenAI Decisions shapes, running local `/v1/systemone` servers (Kev, Ollama ≥ 0.35) | `references/decision-model-alternatives.md` |
| Which framework wraps jev, community tools, company and funding | `references/ecosystem-and-alternatives.md` |
| Model ids, alias targets, SDK release history, 1.14 vs 1.13 | `references/versions/jev-1.14.md`, `references/versions/jev-1.13.md` |
| Whether Jev is the right model versus another decision or chat model; model-family comparisons | `ai-models-specialist` when the `ai-models` plugin is installed |

## Models at a glance

| | `jev-1.14.0` (current) | `jev-1.13.0` (superseded, still callable) |
|---|---|---|
| Aliases | `jev-latest` and `jev-preview` both resolve here | — |
| Price | $0.042 / 1M input, output free | same |
| Context | 64k request / 32k per question; 262k with long-context header | same |
| Images (PNG/JPEG) | yes, behind `TypeSafe-Danger-Zone-Images: true` | yes, same header |
| Box | yes | **no** (400) |

- **Pin a versioned id** (`jev-1.14.0`) for anything audited, gated or threshold-tuned, and log `response.model` on every call. The date `jev-latest` moved to 1.14 is undocumented, and the vendor's deprecation notice (60 days for 1.13, 30 for 1.14) is a blog promise, not a published policy.
- **No jev-1.14 jaggedness page exists.** Never invent 1.14-specific weaknesses; cite only the unversioned jaggedness page and the 1.14 blog caveats.
- Never copy `"model": "jev-1.13.0"` or `release_date 2026-09-15` from the quickstart or primitive pages as current output: those samples are stale.

## Mental model

- **One call** = one `state` + N named questions, evaluated **in parallel and in isolation** against the same state; answers come back keyed by name.
- **Output is data**: a choice, a score, a probability or a box, plus a distribution. No text, no explanation, nothing to parse.
- **Input**: string, JSON object (recommended) or array as one shared context, plus PNG/JPEG images behind a header. No audio or video. English is most accurate; 1.14 improved multilingual support.
- **No customization surface**: no fine-tuning or LoRA, no temperature. You steer with the wording of `state`, `instructions` and `criteria`.
- **Code stays in control.** Control flow, arithmetic, dates and thresholds live in code; jev answers atomic judgments inside it.

Always put facts in `state` and judgments in `questions`. Never embed the question in the state.

## Choosing a primitive

| Need | Primitive | Request | Response | Limit |
|---|---|---|---|---|
| One option from an unordered set | **Choice** | `criteria`: `{option: description}` | `choice`, `probabilities`, `confidence` | 1–255 options; reliable to ~240 |
| A position on an ordered rubric | **Score** | `criteria`: `[level0, level1, ...]`, lowest first | `score` (fractional), `probabilities`, `legend`, `confidence` | 2–10 levels (spec says 1–10) |
| Is this true? | **Noul** | `criteria` optional `{true, false}` | `noul` = P(yes); **no `confidence`** | — |
| Where is it in the image? | **Box** (1.14) | `instructions` only, no `criteria` | `box` {top, bottom, left, right} 0–1; `confidence` may be `null` | one target; needs image + header |

Primitives mix freely in one request.
- **Choice for categories, Score for degree, Noul for one condition, Box for location.** Pick by the shape your code branches on.
- **Pair a Choice with a companion Noul** ("does any option fit?") instead of relying on an `other` option. CHANGED: TypeSafe now says `other` "falls short" because it competes for probability; a Choice always picks something, even a desk lamp as `desk_pro` at 0.96.
- **Pair every Box with a Noul.** Box has no "not found" answer; ignore the box when the Noul is low.
- **Give the complete taxonomy**, and name option keys meaningfully: jev reads the keys.
- **Write Score levels as concrete situations**, one dimension per Score. Never use bare numbers or relative wording; each level is judged alone.
- **One condition per Noul.** Split "angry AND wants a refund" into two. Noul 0.5 means uncertain, never "medium".
- **Never read a Score as a magnitude.** Threshold or rank it; normalise with `score / (len(criteria) - 1)` before weighting.
- **Validate limits client-side** and use structured JSON (`{what, not_for, examples}`) in criteria when options need scope boundaries.

## Designing state and questions

- **Filter state to what the decision needs.** Irrelevant context lowers accuracy and costs input tokens, the only tokens billed.
- **Ask literally.** Jev reads scoping words and negations exactly and will not infer unstated intent.
- **Never ask jev to count, calculate or compare dates.** Compute in code, then ask about the result.
- **Avoid multi-hop questions**, double negatives, and criteria that contradict their instructions (a Noul whose `true` means "no").
- **Fan out speculatively.** Extra questions in one request barely change latency (144 ms for 1 question vs 151 ms for 45 in TypeSafe's audit demo), and the state is billed once.
- **Mind option order.** Choice "leans toward the option that comes first"; reorder options in testing and check consistency.
- **Never assume cross-question consistency.** P(X) + P(not X) need not equal 1; enforce invariants in code.
- **Keep all question wording and thresholds in one reviewed module.** Question text is production logic.

## Reading answers and gating actions

Act on the right number:
- **Choice**: threshold `probabilities[choice]`. `confidence` is computed from the top probability (`(p_max − 1/n)/(1 − 1/n)`), so it adds no second check.
- **Noul**: threshold the value itself: **> 0.7 yes, < 0.3 no**, and give the middle band its own outcome.
- **Score**: check `confidence` first, then route on `score`; when an action depends on a level boundary, sum the probabilities on that side, because neighbouring-level splits barely lower Score confidence.
- **Scale thresholds with consequence**: one floor for genuine uncertainty, higher bars for risky actions. In the voice-banking pattern, < 0.7 goes to a human, a balance check runs at ≥ 0.7, and a transfer only *opens a confirmation screen* above 0.9.
- **Never treat 0.9 as 90% correct.** A community test of 2,319 labelled issues on jev-1.14.0 found 98.9% mean confidence but 84.3% accuracy in the 0.9+ bucket. Tune thresholds on your own labelled data.
- **Never retry to "fix" an answer.** Repeats mostly return the same result (7 of 13 identical across 5 runs in TypeSafe's cookbook; 23 of 1,500 top answers changed in a community test). Change the question or escalate.
- **Log state, question schema, option order, `response.model` and the probabilities together** for every consequential decision.

## Worked examples

More, in every language and framework: `references/examples.md`.

**1. Support triage with speculative fan-out (Python).** Request constructed to match TypeSafe's fan-out routing code (routing condensed; verbatim in `references/examples.md` §2):
```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient(model="jev-1.14.0")
response = client.system_one(
    state={"ticket": ticket_text, "plan": "business"},
    questions={
        "category": Choice(instructions="What kind of ticket is `ticket`?", criteria={
            "bug_report": "Something in the product is broken", "billing": "Charges, invoices, refunds",
            "feature_request": "Asks for something the product does not do yet"}),
        "bug_severity": Score(instructions="If this is a bug, how severe is it?",
            criteria=["Cosmetic", "Broken but a workaround exists", "Blocks a core task"]),
        "has_reproducible_steps": Noul(instructions="Does the ticket give steps to reproduce the problem?"),
        "refund_requested": Noul(instructions="Is the customer asking for money back?"),
        "frustration": Score(instructions="How frustrated is the customer?",
            criteria=["Calm", "Frustrated but civil", "Very angry"]),
    },
)
category, a = response.answers["category"], response.answers
if category.choice == "bug_report":
    if a["bug_severity"].score > 1.5 and a["has_reproducible_steps"].noul > 0.6:
        escalate_to_engineering(ticket_id, severity="high")
    else:
        add_to_bug_backlog(ticket_id)
elif category.choice == "billing":
    route_to_billing(ticket_id, refund_likely=a["refund_requested"].noul > 0.7)
if a["frustration"].score > 1.5:          # useful regardless of category
    flag_for_priority_response(ticket_id)
```

**2. Companion Noul in TypeScript: act only when an option fits.** Thresholds are TypeSafe's (0.7 / 0.3 / 0.7). The documented `noul()` builder takes instructions only, so the "what counts as no" boundary goes in the instruction text:
```ts
import { choice, noul, TypeSafeClient } from "@typesafe-ai/sdk";
const client = new TypeSafeClient({ defaultModel: "jev-1.14.0" });
const { answers } = await client.systemOne({
  state: { message, products: ["desk_pro: 140 cm standing desk", "chair_lite", "monitor_arm"] },
  questions: {
    product: choice("Which product in `products` is `message` about?",
      { desk_pro: null, chair_lite: null, monitor_arm: null }),
    about_our_product: noul("Is `message` about one of `products`? Another product, a service, " +
      "or something we don't sell counts as no."),
  },
});
const fits = answers.about_our_product.noul;
const p = answers.product.probabilities[answers.product.choice];
if (fits < 0.3) sendToGeneralInbox();
else if (fits > 0.7 && p > 0.7) sendToProductTeam(answers.product.choice);
else sendToGeneralAgent({ suggested: answers.product.choice });
```

**3. Verify an LLM's answer before showing it (Python, verbatim logic).** Three Nouls (`answerable`, `declines`, `supported`) about `{request, paragraphs, candidate_response}`, one request:
```python
if nouls["declines"] >= 0.5:
    risk = nouls["answerable"]        # it declined: risky if the paragraphs do answer
else:
    risk = 1 - nouls["supported"]     # it answered: risky if the paragraphs don't lead there
status = "review" if risk >= 0.2 else "pass"
```
On 1,000 multi-hop answers from `gpt-6-luna`, this passed 73% at 95.7% accuracy and caught 84 of 115 wrong answers.

**4. Vercel AI SDK (TypeScript).** Use `experimental_decide` and `typeSafeAi.decisionModel(id)` (`ai` ≥ 7.0.128); `experimental_evaluate` / `evaluationModel` are deprecated aliases and must not appear in new code:
```ts
import { typeSafeAi } from "@ai-sdk/typesafe-ai";
import { experimental_decide } from "ai";
const result = await experimental_decide({
  model: typeSafeAi.decisionModel("jev-1.14.0"),        // or "typesafe-ai/jev" via AI Gateway
  state: { message: "I was charged twice. Please refund the duplicate." },
  questions: { requestsRefund: { type: "boolean", instructions: "Is the customer requesting money back?" } },
});
if (result.answers.requestsRefund.probability > 0.7) queueRefundReview();
```
The direct provider reads `TYPESAFE_AI_API_KEY` (not `TYPESAFE_API_KEY`). Confidence lives in `result.providerMetadata.typesafe.confidence`.

## Calling jev: pick a route

| Route | Endpoint / call | Credential | Model id |
|---|---|---|---|
| Direct HTTP | `POST https://api.typesafe.ai/v1/systemone` | `Authorization: Bearer $TYPESAFE_API_KEY` | `"model"` **in the body**: `jev-1.14.0`, `jev-latest` |
| Python | `pip install typesafe-sdk` (0.7.5, Py ≥ 3.10); `TypeSafeClient().system_one(...)` | `TYPESAFE_API_KEY` | default `jev-latest` |
| JS/TS | `npm install @typesafe-ai/sdk` (0.7.0, **Node ≥ 22**); `new TypeSafeClient().systemOne(...)` | `TYPESAFE_API_KEY` | default `jev-latest` |
| Cloudflare Workers AI | `env.AI.run('typesafe/jev-1.14.0', {...})`; REST `.../ai/run` with model in the body | binding or CF token | `typesafe/jev` = **1.13**, `typesafe/jev-1.14.0` |
| Vercel AI Gateway | `https://ai-gateway.vercel.sh/typesafe/v1/systemone`, `/v1/decisions`, AI SDK | `AI_GATEWAY_API_KEY` / OIDC | `typesafe-ai/jev`, `typesafe-ai/jev-1.14.0` |
| OpenRouter | `POST https://openrouter.ai/api/alpha/decisions` (alpha) or SDK `base_url="https://openrouter.ai/api"` | `OPENROUTER_API_KEY` | `typesafe/jev-1.14`, `~typesafe/jev-latest` |
| Others | DigitalOcean (1.13 only), Databricks (1.14 only, preview), Netlify, Requesty (experimental), LiteLLM, Portkey, Kong, TrueFoundry, Zuplo, Pydantic AI Gateway | see `references/purchase-routes.md` | varies |

Route directives:
- **Never put `model` inside the Cloudflare payload**, and never append the model to the Cloudflare URL path. On the direct API, `model` is required in the body.
- **Never state a Cloudflare billing path or rate limit for jev.** No Cloudflare page ties jev to Neurons, Workers Paid or Unified Billing credits; say "not stated".
- **jev is not on AWS Bedrock, Microsoft Foundry, Vertex AI, OCI or watsonx** (clean catalog negatives, 2026-11-13). AWS, Azure and GCP Marketplace searches are **unverified**, not denied.
- **Reject the AWS Marketplace "JEV-27B Decision Model" (seller Warp Drive)**: a self-hosted AMI with no TypeSafe connection, not jev. **Never use the `jevai.info` endpoint** from a community AWS article; the only official endpoint is `api.typesafe.ai`.
- **Disable SDK compression for gateways that reject it.** Python 0.7.5 and JS 0.7.0 zstd-compress bodies ≥ 1 KiB by default, and TypeSafe warns "non-official APIs may not support it yet."
- **Never set `dangerouslyAllowBrowser: true`** in production; it exposes the key client-side.
- **Do not plan for streaming or batch.** The OpenAPI spec has only `POST /v1/systemone` and `GET /v1/models`.
- **Never assume SDK parity.** Python has `response_model`; JS has none. Score `criteria` is a list in both since 0.6.0.

## Danger-Zone headers: images, Box, long context

All three are "dreamer-ready": TypeSafe says they have "way too much jaggedness" for production, and multimodal accuracy is below text-only.
- **Images** (1.13 and 1.14): send `TypeSafe-Danger-Zone-Images: true` on every request with images or Box. Put images in `state`, `instructions` or `criteria` via a top-level `assets` map (`data_base64` + `format`, or a multipart `part`); every asset must be referenced or the request fails with 400. PNG/JPEG stills only, 16 MiB per file, each side 280–1,568 px, never resized. Put a shared image in `state`: an image in `instructions` is sent once per question.
- **Box** (1.14 only): one target per question, coordinates are fractions from the top-left, `confidence` can be `null`. For small targets, find the region first, then Box a tile.
- **Long context**: `TypeSafe-Danger-Zone-Long-Context: true` raises both limits (64k request, 32k state + longest question) to **262k** at the same per-token price, "slower and less accurate." The AI SDK exposes it as `providerOptions.typesafe.longContext`; OpenRouter auto-enables it above ~32,000 bytes or with any image; LiteLLM forwards `TypeSafe-Danger-Zone-*` headers. Cloudflare, Vercel's TypeSafe-compatible route and Requesty do not say whether they forward it.

## Errors and retries

| Status | Meaning | Handle |
|---|---|---|
| 400 | Rule broken, images not enabled, unreferenced asset, or `max_tokens_exceeded` (over context) | Fix the payload or shrink state. Never retry. |
| **401** | Invalid key (docs say missing too) | Fix or rotate the key. |
| **403** | **Missing** key, observed (issue typesafe-ai/skills#8, still open) | Treat as a credential error. |
| 413 / 415 | Body over 32 MiB / bad or stacked `Content-Encoding` | Shrink, use multipart, or send one gzip/zstd layer. |
| 422 | Validation failure (issue #1: may arrive as 400) | Fix the payload. Never retry. |
| 429 | Rate limited (`retry_after_ms` / `retryAfterMs`) | Back off; the SDK retries. |
| 529 / 5xx | Overloaded / server failure | Exponential backoff; circuit-break if it persists. |

- **Always catch both 401 and 403 classes** (`TypeSafeAuthenticationError` + `TypeSafePermissionDeniedError`, or JS `AuthenticationError` + `PermissionDeniedError`) when checking credentials, or branch on `body.error_type == "authentication_error"`. Catching only the 401 class misses an unset key.
- **SDK retry defaults are sane**: 2 retries, 0.5 s → 5 s backoff, statuses {408, 429, 500–599}, `Retry-After` honoured. Python adds a 30 s total budget over its 10 s per-attempt timeout; JS has 10 s per attempt and no total budget.
- **Quote `request_id` / `requestId`** (header `x-typesafe-request-id`) to support. Do not log error bodies blindly; they can echo submitted state.

## Limits and pricing

| Item | Value |
|---|---|
| Price (direct) | **$0.042 / 1M input tokens, output free**, both versions; image tokens bill as input |
| Context | 64k per request, 32k for state + longest question; 262k opt-in |
| Body | ≤ 32 MiB; UTF-8 JSON; nesting ≤ 64; finite numbers only (send ids as strings) |
| Questions per request | no documented cap; only context limits it |
| Rate limits | **per organisation, in the console.** CHANGED: the old 250,000 tok/s and 1,200 req/min figures were removed. Never hardcode numbers. |
| SLA | none; `status.typesafe.ai` is informational |

- Batch questions, not requests: one 13-question request was 12.2× cheaper and 11.8× faster than 13 single-question requests in TypeSafe's cookbook, with no change in answers.
- Gateway catalogs show 32,000 (Cloudflare, Vercel: the per-question limit) or 64K (Requesty: the request limit); these are the same defaults, not smaller models.

## Security: jev is not a security boundary

- **Injected text moves verdicts, and the vendor says so.** Jaggedness item: "Jev doesn't treat state as hostile by default." In a press-reported test, a planted "pre-approved" field dropped the block probability for `rm -rf ~/.ssh` from 0.76 to 0.48. Never make jev the sole gate on a destructive or privileged action; pair it with deterministic checks and human approval.
- **Gating discloses.** Tool-call arguments and conversation state reach TypeSafe (or the gateway's provider) whatever the verdict. LangChain and Vercel both say to keep secrets and credentials out of them.
- **Know what each gate does on failure.** LangChain `AutoModeMiddleware` refuses risky calls and never asks for approval (add human-in-the-loop middleware). Vercel eve `auto()` fails closed to human approval but has no probability threshold. The community `jev-guard` fails **open** by default.
- **Enforce permissions in the executor.** Vercel: a classifier "cannot establish that the caller owns those resources"; tenant isolation and network limits belong in code.
- **Test option orderings and adversarial inputs** before deploying, and pin the model version.
- For threat modelling and defence-in-depth design, hand off to `ai-security`.

## Data and legal quick facts

- **No training on input** (privacy policy; MCA requires consent). Retention is "as long as reasonably necessary", no fixed period. MCA Telemetry (logs, hashes, statistics) is kept perpetually.
- **Zero data retention** is enterprise-only, requested through `https://support.typesafe.ai/forms/support-request` (CHANGED: no longer `privacy@typesafe.ai`).
- DPA: 72-hour breach notice, EU SCCs, **UK Addendum** (not "IDTA"), Swiss terms, 15 days to object to subprocessors.
- **Trust Center (`trust.typesafe.ai`) is unfetchable.** Never claim SOC 2, ISO 27001 or any certification for TypeSafe; send users to the Trust Center.
- **The MCA governs API use**: no distillation or competing products from outputs, no reselling, no uptime SLA, liability capped at the greater of 12 months' fees or $50.
- Cloudflare's jev cards list "Zero data retention: Yes"; no source says whether TypeSafe's terms apply identically to routed requests.
- **Not Lightbend.** TypeSafe AI has no relation to Lightbend's former Typesafe (Scala/Akka).

## Porting and wire compatibility

Whether to switch models is a selection question for `ai-models-specialist` when installed. Once a target is chosen, the porting facts are:
- **Same System One shape** (`state` + named question map, `noul`): Cloudflare Clef ("change endpoint and model"), Microsoft-Decision-1 (`/providers/microsoft/v1/systemone`), Liquid d1-ultra, Baseten, Perplexity, and local servers. Usually only `baseURL`/`base_url`, key and `model` change.
- **Gemini Decisions API** (`gemini-decision-1`): named map, but the shared field is `input`, Noul criteria are `true_description`/`false_description`, and Noul returns a `confidence` jev does not.
- **OpenAI Decisions API** (`gpt-6-luna`): `input`, a questions **array** with `name`, `predicate` instead of `noul`, and probabilities as `[{value, probability}]`.
- **AI SDK `experimental_decide`** hides all three shapes behind `boolean`/`choice`/`score`/`box`; calibration is not promised to match across providers, so re-tune thresholds after any port.
- **Local `/v1/systemone` servers**: Kev (`jaredpalmer/kev-*`, `python -m kev.serve`) and Ollama ≥ 0.35 (`ollama pull nimble`, `tev1`) accept TypeSafe SDK requests with a changed base URL.
- **Anthropic decision model: NOT FOUND** as of 2026-11-13; Claude structured outputs are not a decision-model API, so there is nothing wire-compatible to port to.

Shapes, verbatim run commands and fallback facts: `references/decision-model-alternatives.md`.

## Scripts

- `scripts/smoke-test.sh direct|cloudflare` sends one three-primitive request (default model `jev-1.14.0`; override with `JEV_MODEL`) and prints the raw body and HTTP status. **Requires `TYPESAFE_API_KEY`, or `CLOUDFLARE_ACCOUNT_ID` + `CLOUDFLARE_API_TOKEN`, and spends real tokens.** Run it first when a user reports auth or shape errors, to separate credential and transport problems from question-design problems.

## References

- `references/primitives-and-schemas.md`: request and answer fields for all four primitives, images and assets, confidence formulas, 1.14 sample responses.
- `references/examples.md`: 23 sourced recipes with request plus acting code.
- `references/api-and-sdks.md`: HTTP, both SDKs, images in each SDK, retries, performance, alternate base URLs.
- `references/purchase-routes.md`: the full provider matrix, BYOK vs resale, negatives and look-alikes.
- `references/cloudflare-workers-ai.md`: both Cloudflare cards, binding, REST, AI Gateway, what is not stated.
- `references/patterns.md`: the six official patterns plus shortlist-then-score, hierarchy fallback and LLM hybrids.
- `references/limitations-and-security.md`: jaggedness, community calibration data, injection evidence, gating behaviour, privacy, legal, status.
- `references/pricing-limits-errors.md`: cost math, the full limits table, the unified error table.
- `references/decision-model-alternatives.md`: wire compatibility, porting between API shapes, local `/v1/systemone` servers and run commands; fallback facts when `ai-models-specialist` is not installed.
- `references/ecosystem-and-alternatives.md`: integrations, community tools, company news.
- `references/versions/jev-1.14.md`: current model, aliases, SDK release tables. `references/versions/jev-1.13.md`: superseded version notes.

## Sources

- https://docs.typesafe.ai/models.md
- https://docs.typesafe.ai/changelog.md
- https://docs.typesafe.ai/llms.txt
- https://api.typesafe.ai/openapi.json
- https://docs.typesafe.ai/api/system-one.md
- https://docs.typesafe.ai/api/errors.md
- https://docs.typesafe.ai/introduction/quickstart.md
- https://docs.typesafe.ai/concepts/state.md
- https://docs.typesafe.ai/primitives/choice.md
- https://docs.typesafe.ai/primitives/score.md
- https://docs.typesafe.ai/primitives/noul.md
- https://docs.typesafe.ai/primitives/box.md
- https://docs.typesafe.ai/primitives/advanced.md
- https://docs.typesafe.ai/images.md
- https://docs.typesafe.ai/confidence.md
- https://docs.typesafe.ai/patterns/fan-out.md
- https://docs.typesafe.ai/patterns/companion-noul.md
- https://docs.typesafe.ai/patterns/confidence-routing.md
- https://docs.typesafe.ai/patterns/probability-routing.md
- https://docs.typesafe.ai/cookbooks/parallel_questions.md
- https://docs.typesafe.ai/cookbooks/verify_llm_outputs.md
- https://docs.typesafe.ai/demos/content-audit.md
- https://docs.typesafe.ai/model-jaggedness.md
- https://docs.typesafe.ai/sdk/python/usage/basic.md
- https://docs.typesafe.ai/sdk/python/changelog.md
- https://docs.typesafe.ai/sdk/javascript.md
- https://docs.typesafe.ai/sdk/javascript/changelog.md
- https://typesafe.ai/blog/jev-1-14 (vendor blog)
- https://typesafe.ai/blog/dont-call-it-a-decision-model (vendor blog)
- https://github.com/typesafe-ai/skills/issues/8
- https://github.com/typesafe-ai/skills/issues/17 (community)
- https://github.com/typesafe-ai/skills/issues/19 (community)
- https://pypi.org/pypi/typesafe-sdk/json
- https://registry.npmjs.org/@typesafe-ai/sdk
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/
- https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
- https://vercel.com/docs/ai-gateway/modalities/decision
- https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
- https://openrouter.ai/blog/insights/what-is-jev/
- https://aws.amazon.com/marketplace/pp/prodview-cpbvpwpvmgu26
- https://docs.langchain.com/oss/python/integrations/providers/typesafe.md
- https://vercel.com/kb/guide/auto-approve-tool-calls-eve-jev
- https://github.com/leepokai/jev-guard (community)
- https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)
- https://docs.typesafe.ai/legal
- https://typesafe.ai/legal/privacy-policy
- https://typesafe.ai/legal/data-processing
- https://typesafe.ai/legal/mca
- https://trust.typesafe.ai/ (unfetchable; user must check directly)
- https://status.typesafe.ai
- https://aistudio.google.com/docs/decisions-api
- https://developers.openai.com/api/docs/guides/decisions.md
- https://github.com/jaredpalmer/kev
- https://github.com/ollama/ollama/releases/tag/v0.35.0

Fetched: 2026-11-13
