# Gemini 3.5 Flash-Lite

Canonical model ID: `gemini-3.5-flash-lite`

## Identity and status

- Provider: Google.
- Family: `gemini`.
- Catalog role: low-cost, high-volume, agentic.
- Status: stable.
- Release: unknown.
- License/serving model: proprietary hosted model.
- Availability: Gemini API, Google AI Studio.

> Source: https://ai.google.dev/gemini-api/docs/models.md

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `gemini-3.5-flash-lite`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://ai.google.dev/gemini-api/docs/models.md

## Context and capabilities

- Context/output: unknown in inspected model detail.
- Documented capabilities:
- high-volume agentic tasks
- translation
- simple data processing
- multimodal input

> Source: https://ai.google.dev/gemini-api/docs/models.md

## Price and billing conditions

- Catalog price: $0.30/1M input, $2.50/1M output, caching $0.03 (Gemini API paid tier as displayed; modality/tiers vary).
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Selection tradeoffs

### Strengths
- cost efficient high-volume processing; suitable when latency/cost outweigh maximum reasoning quality

### Limitations and unknowns
- not intended as default for hard reasoning; validate quality on task-specific evals

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Gemini API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://ai.google.dev/gemini-api/docs/models.md

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Sources

- https://ai.google.dev/gemini-api/docs/models.md
- https://ai.google.dev/gemini-api/docs/pricing.md

Fetched: 2026-10-16
