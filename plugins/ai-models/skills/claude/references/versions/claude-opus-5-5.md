# Claude Opus 5.5

Canonical model ID: `claude-opus-5-5`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: frontier, general, coding, agentic.
- Status: active (latest).
- Release: 2026-09-22.
- License/serving model: proprietary API model.
- Availability: Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, Claude Platform on AWS.

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-opus-5-5`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
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

- Catalog price: $4/MTok input, $20/MTok output; cache writes $5/$8 MTok (5m/1h), reads $0.20; batch input/output 50% discount.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Selection tradeoffs

### Strengths
- long-running agentic coding and knowledge work
- Anthropic recommends Opus 5.5 as the starting point for most workloads; Sonnet 5.5 is its speed/intelligence-balance choice

### Limitations and unknowns
- adaptive thinking always on; effort controls depth
- breaking migration changes from Opus 5 include model-bound thinking blocks and changed computer-use tool compatibility

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Sources

- https://platform.claude.com/docs/en/models/opus-5-5/overview
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/about-claude/pricing

Fetched: 2026-10-16
