# Claude Opus 5.5

Canonical model ID: `claude-opus-5-5`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: frontier, general, coding, agentic.
- Status: active (latest Opus tier).
- Release: 2026-09-22.
- License/serving model: proprietary API model.
- Availability: Claude API; Amazon Bedrock (bedrock-mantle `anthropic.claude-opus-5-5`; access gated per account); Google Cloud (Google managed and Anthropic managed): `claude-opus-5-5`; Microsoft Foundry (Azure-hosted and Anthropic-hosted; fast-mode id `claude-opus-5-5-fast`); Claude Platform on AWS: `claude-opus-5-5`.

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-opus-5-5`.
- No separate dated snapshot id is recorded; check the model page's alias and snapshot rows before pinning. Partner platforms add their own prefixes or profiles (see Platform IDs).
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview

## Context and capabilities

- Context/output: 1M tokens; 128K max output.
- Documented capabilities:
- text and image input
- text output
- adaptive thinking
- tool use
- 1M context

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview

## Price and billing conditions

- Catalog price: $4/MTok input, $20/MTok output; cache writes $5/$8 MTok (5m/1h), reads $0.20; batch input/output 50% discount; fast mode $8/$40 (GA 2026-10-15, no beta header).
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Partner platforms set their own prices. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Lifecycle and changes since the 2026-10-16 snapshot

- Released 2026-09-22; retirement not sooner than 2027-09-22. Default effort `medium`; knowledge cutoff June 2026.
- Fast mode left research preview on 2026-10-15 (no beta header; default fast rate limit in Start/Build/Scale tiers) and reached Microsoft Foundry (Azure-hosted) the same day; Google Cloud (Anthropic managed) on 2026-10-22. Fast price $8/$40 per MTok; Foundry fast id `claude-opus-5-5-fast`.
- 2026-10-30: Opus 5.5 is the named migration target for Opus 4.8 fast mode, which is removed 2026-11-30.
- Since 2026-11-09 Claude Fable 5.2 is the newest Claude model; Opus 5.5 remains the latest Opus tier.

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview
> Source: https://platform.claude.com/docs/en/release-notes/overview
> Source: https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Request-parameter constraints

- Opus 5.5 rejects temperature/top_p/top_k, forced `tool_choice` and thinking enabled/disabled at the model level, independent of API version `2026-10-21` (which removes the sampling parameters for every model).

> Source: https://platform.claude.com/docs/en/api/migration-2026-10-21

## Platform IDs

| Platform | Model ID |
|---|---|
| Claude API | `claude-opus-5-5` |
| Amazon Bedrock (bedrock-mantle; access gated per account in the console) | `anthropic.claude-opus-5-5` |
| Google Cloud (Google managed and Anthropic managed) | `claude-opus-5-5` |
| Microsoft Foundry (Azure-hosted and Anthropic-hosted) | `claude-opus-5-5` (fast: `claude-opus-5-5-fast`) |
| Claude Platform on AWS | `claude-opus-5-5` |

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
> Source: https://platform.claude.com/docs/en/models/overview

## Selection tradeoffs

### Strengths
- long-running agentic coding and knowledge work
- Anthropic recommends Opus 5.5 as the starting point for most workloads; Sonnet 5.5 is its speed/intelligence-balance choice

### Limitations and unknowns
- adaptive thinking always on; effort controls depth (default medium); thinking enabled/disabled, forced tool_choice and temperature/top_p/top_k return 400
- breaking migration changes from Opus 5 include model-bound thinking blocks and changed computer-use tool compatibility
- retirement not sooner than 2027-09-22

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-11-13.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Anthropic lifecycle dates apply to Anthropic-operated surfaces (Claude API, Claude Platform on AWS, Foundry); Bedrock and Google Cloud (Google managed) set their own dates.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed

## Sources

- https://platform.claude.com/docs/en/models/opus-5-5/overview
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/build-with-claude/fast-mode
- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/api/migration-2026-10-21
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed

Fetched: 2026-11-13
