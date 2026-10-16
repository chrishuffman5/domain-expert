# Claude Fable 5.1

Canonical model ID: `claude-fable-5-1`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: reasoning, agentic, coding.
- Status: active (latest).
- Release: 2026-09-01.
- License/serving model: proprietary API model.
- Availability: Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, Claude Platform on AWS.

> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-fable-5-1`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview

## Context and capabilities

- Context/output: 1M tokens; 128K max output.
- Documented capabilities:
- text and image input
- text output
- adaptive thinking
- tool use
- 1M context

> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview

## Price and billing conditions

- Catalog price: $10/MTok input, $50/MTok output; cache writes $12.50/$20, read $0.25; batch input/output 50% discount.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Selection tradeoffs

### Strengths
- demanding reasoning and long-horizon agentic coding
- multistep research and document, spreadsheet, slide work

### Limitations and unknowns
- slower and materially more expensive than Opus 5.5; select only where evals justify it
- forced tool use now errors; thinking blocks model-specific; migration changes can be breaking

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Sources

- https://platform.claude.com/docs/en/models/fable-5-1/overview
- https://platform.claude.com/docs/en/about-claude/pricing

Fetched: 2026-10-16
