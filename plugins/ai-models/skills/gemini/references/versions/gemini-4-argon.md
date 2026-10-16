# Gemini 4 Argon

Canonical model ID: `gemini-4-argon`

## Identity and status

- Provider: Google.
- Family: `gemini`.
- Catalog role: frontier, reasoning, coding, agentic.
- Status: stable.
- Release: 2026-10.
- License/serving model: proprietary hosted model.
- Availability: Gemini API, Google AI Studio; no free tier / Google AI Pro.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `gemini-4-argon`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon

## Context and capabilities

- Context/output: 1,048,576 shared input/output tokens; max output 65,536 synchronous and up to 1,048,576 long decode.
- Documented capabilities:
- text/image/video/audio/PDF input
- text output
- tool use
- thinking low/medium/high
- 1M context and long decode
- search grounding
- code execution

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon

## Price and billing conditions

- Catalog price: Intro through 2026-11-30: $2/1M input, $10/1M output; from 2026-12-01 $4/$20; implicit cache hits 95% discount; no free tier.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Selection tradeoffs

### Strengths
- hard software engineering, math/science and multi-step agent work
- supports multimodal inputs and up to 1M long decode

### Limitations and unknowns
- long tasks can take minutes; explicit caching unsupported; sampling params ignored
- preview computer use; shared context budget includes input, thought and output tokens

- Adoption evidence: New release; public usage metric unknown.
- Scope/date: Gemini API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Sources

- https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- https://ai.google.dev/gemini-api/docs/latest-model
- https://ai.google.dev/gemini-api/docs/pricing.md

Fetched: 2026-10-16
