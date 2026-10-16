# Gemini 3.8 Live

Canonical model ID: `gemini-3.8-live`

## Identity and status

- Provider: Google.
- Family: `gemini`.
- Catalog role: audio, real-time, voice-agent.
- Status: stable.
- Release: 2026-09-15.
- License/serving model: proprietary hosted model.
- Availability: Gemini API Live API, Google AI Studio.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `gemini-3.8-live`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live

## Context and capabilities

- Context/output: 131,072 input tokens; 65,536 output tokens.
- Documented capabilities:
- streaming audio/video input
- text and audio output
- asynchronous function calling
- interleaved reasoning

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live

## Price and billing conditions

- Catalog price: See modality-based Gemini API pricing; not independently verified for live stream in pricing lines inspected.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Selection tradeoffs

### Strengths
- provider's default for most low-latency voice agents without reasoning-induced delays

### Limitations and unknowns
- specialized real-time interface and modality; do not treat as general text endpoint
- reasoning-heavy live tasks may benefit from extended-thinking companion model

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Gemini API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://ai.google.dev/gemini-api/docs/deprecations

## Sources

- https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live
- https://ai.google.dev/gemini-api/docs/models.md
- https://ai.google.dev/gemini-api/docs/deprecations

Fetched: 2026-10-16
