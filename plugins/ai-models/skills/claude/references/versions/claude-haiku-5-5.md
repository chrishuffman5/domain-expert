# Claude Haiku 5.5

Canonical model ID: `claude-haiku-5-5`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: general, low-latency, classification.
- Status: active (latest).
- Release: unknown.
- License/serving model: proprietary API model.
- Availability: Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, Claude Platform on AWS.

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-haiku-5-5`.
- No alternate alias or pinned snapshot identifier is recorded in this catalog entry.
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview

## Context and capabilities

- Context/output: 1M tokens; 128K max output.
- Documented capabilities:
- text and image input
- text output
- adaptive thinking
- tool use
- 1M context

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview

## Price and billing conditions

- Catalog price: $0.10/MTok input and $0.50/MTok output for prompts up to 100K; $0.50/$2.50 for prompts over 100K.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Selection tradeoffs

### Strengths
- high-volume, latency-sensitive classification, extraction, routing and subagent tasks
- fastest current mainline Claude tier per provider

### Limitations and unknowns
- different tokenizer from Haiku 4.5; same text counts about 30% more tokens per provider
- thinking blocks are account-bound or usable in linked account

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-10-16.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview

## Lifecycle and verification

- Recheck the provider’s current status before new deployment or a migration; catalog status is a research snapshot, not a service guarantee.
- Validate the exact model ID, access scope, context/output caps, pricing tier, and retirement schedule on the platform that will serve requests.
- This reference describes model identity and selection. Integration procedures belong to the `ai` plugin.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Sources

- https://platform.claude.com/docs/en/models/haiku-5-5/overview
- https://platform.claude.com/docs/en/about-claude/pricing

Fetched: 2026-10-16
