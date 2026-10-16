# Claude Sonnet 5.5

Canonical model ID: `claude-sonnet-5-5`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: general, coding, agentic.
- Status: active (latest).
- Release: unknown.
- License/serving model: proprietary API model.
- Availability: Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, Claude Platform on AWS.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-sonnet-5-5`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

## Context and capabilities

- Context/output: 1M tokens; 128K max output.
- Documented capabilities:
- text and image input
- text output
- adaptive thinking
- tool use
- 1M context

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

## Price and billing conditions

- Catalog price: $2/MTok input, $10/MTok output.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/models/overview

## Selection tradeoffs

### Strengths
- provider-described best speed/intelligence combination
- software engineering and agentic workflow usability

### Limitations and unknowns
- breaking differences from Sonnet 5 include tool-use, thinking-block and computer-use behavior; test migration
- cannot use older computer_20251124 tool on Claude API and Google Cloud

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://platform.claude.com/docs/en/models/overview

## Sources

- https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- https://platform.claude.com/docs/en/models/overview

Fetched: 2026-10-16
