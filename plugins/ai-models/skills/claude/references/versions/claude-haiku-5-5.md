# Claude Haiku 5.5

Canonical model ID: `claude-haiku-5-5`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: general, low-latency, classification.
- Status: active (latest Haiku tier).
- Release: 2026-10-07.
- License/serving model: proprietary API model.
- Availability: Claude API; Amazon Bedrock (bedrock-mantle `anthropic.claude-haiku-5-5`; access gated per account); Google Cloud (Google managed and Anthropic managed): `claude-haiku-5-5`; Microsoft Foundry (Azure-hosted and Anthropic-hosted); Claude Platform on AWS: `claude-haiku-5-5`.

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-haiku-5-5`.
- No separate dated snapshot id is recorded; check the model page's alias and snapshot rows before pinning. Partner platforms add their own prefixes or profiles (see Platform IDs).
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

- Catalog price: Prompts up to 100K: $0.10/MTok input, $0.50 output (cache writes $0.125/$0.20 5m/1h, read $0.01); over 100K: $0.50/$2.50 (cache writes $0.625/$1, read $0.05); batch 50% discount; the 1.1x US data-residency multiplier applies to both tiers.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Partner platforms set their own prices. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Lifecycle and verified details

- Released 2026-10-07 (the snapshot recorded unknown); retirement not sooner than 2027-10-07. Default effort `medium`; knowledge cutoff June 2026.
- Cache prices: up to 100K prompt 5m $0.125, 1h $0.20, read $0.01; over 100K 5m $0.625, 1h $1, read $0.05. Batch 50% off; Batch API 300K-output beta applies.
- The 1.1x US data-residency multiplier also applies to the higher (over-100K) price tier.
- Returns 400 for `budget_tokens`, temperature/top_p/top_k, prefill and `computer_20250124`, which Haiku 4.5 accepted. `claude-haiku-4-5-20251001` is still Active (not sooner than 2026-10-15; no retirement announced as of 2026-11-13).

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview
> Source: https://platform.claude.com/docs/en/about-claude/pricing
> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations

## Platform IDs

| Platform | Model ID |
|---|---|
| Claude API | `claude-haiku-5-5` |
| Amazon Bedrock (bedrock-mantle; access gated per account in the console) | `anthropic.claude-haiku-5-5` |
| Google Cloud (Google managed and Anthropic managed) | `claude-haiku-5-5` |
| Microsoft Foundry (Azure-hosted and Anthropic-hosted) | `claude-haiku-5-5` |
| Claude Platform on AWS | `claude-haiku-5-5` |

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
> Source: https://platform.claude.com/docs/en/models/overview

## Selection tradeoffs

### Strengths
- high-volume, latency-sensitive classification, extraction, routing and subagent tasks
- fastest current mainline Claude tier per provider

### Limitations and unknowns
- different tokenizer from Haiku 4.5; same text counts about 30% more tokens per provider
- thinking blocks are account-bound or usable in linked account
- returns 400 for budget_tokens, temperature/top_p/top_k, prefill and computer_20250124 that Haiku 4.5 accepted
- retirement not sooner than 2027-10-07

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-11-13.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview

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

- https://platform.claude.com/docs/en/models/haiku-5-5/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed

Fetched: 2026-11-13
