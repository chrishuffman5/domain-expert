# Gemini 3.8 Flash

Canonical model ID: `gemini-3.8-flash`

## Identity and status

- Provider: Google.
- Family: `gemini`.
- Catalog role: general, coding, agentic, multimodal.
- Status: stable.
- Release: 2026-09-02.
- License/serving model: proprietary hosted model.
- Availability: Gemini API, Google AI Studio.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `gemini-3.8-flash`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash

## Context and capabilities

- Context/output: 1,048,576 input tokens; 65,536 output tokens.
- Documented capabilities:
- text/image/video/audio/PDF input
- text output
- tool use
- agentic video understanding

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash

## Price and billing conditions

- Catalog price: Paid Gemini API list: $0.50/1M input and $3/1M output (standard tier, see pricing page for conditions).
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Selection tradeoffs

### Strengths
- long-horizon software engineering, autonomous agents and enterprise workflows with Flash speed/cost profile

### Limitations and unknowns
- provider identifies 3.8 Flash as new stable; benchmark against Pro/Argon for difficult tasks

- Adoption evidence: Provider labels stable; comparable usage/adoption metric unknown.
- Scope/date: Gemini API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://ai.google.dev/gemini-api/docs/deprecations

## Sources

- https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash
- https://ai.google.dev/gemini-api/docs/models.md
- https://ai.google.dev/gemini-api/docs/pricing.md
- https://ai.google.dev/gemini-api/docs/deprecations

Fetched: 2026-10-16
