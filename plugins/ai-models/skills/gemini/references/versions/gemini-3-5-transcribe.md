# Gemini 3.5 Transcribe

Canonical model ID: `gemini-3.5-transcribe`

## Identity and status

- Provider: Google.
- Family: `gemini`.
- Catalog role: audio, speech-to-text.
- Status: stable.
- Release: unknown.
- License/serving model: proprietary hosted model.
- Availability: Gemini API, Google AI Studio.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `gemini-3.5-transcribe`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe

## Context and capabilities

- Context/output: Audio transcription model; general context limits not listed in inspected excerpt.
- Documented capabilities:
- speech transcription
- 85+ languages
- language detection
- speaker diarization
- word timestamps
- custom vocabulary biasing

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe

## Price and billing conditions

- Catalog price: See Gemini API audio pricing; modality and batch tier conditions apply.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Selection tradeoffs

### Strengths
- specialist transcription with speaker/timing annotations and domain vocabulary support

### Limitations and unknowns
- speech-to-text specialist; not a general text generation model
- verify live vs file-transcription endpoint requirements

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Gemini API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://ai.google.dev/gemini-api/docs/pricing.md

## Sources

- https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe
- https://ai.google.dev/gemini-api/docs/models.md
- https://ai.google.dev/gemini-api/docs/pricing.md

Fetched: 2026-10-16
