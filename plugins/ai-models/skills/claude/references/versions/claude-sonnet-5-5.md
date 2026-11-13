# Claude Sonnet 5.5

Canonical model ID: `claude-sonnet-5-5`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: general, coding, agentic.
- Status: active (latest Sonnet tier).
- Release: 2026-09-28.
- License/serving model: proprietary API model.
- Availability: Claude API; Amazon Bedrock (bedrock-mantle `anthropic.claude-sonnet-5-5`; access gated per account); Google Cloud (Google managed and Anthropic managed): `claude-sonnet-5-5`; Microsoft Foundry (Azure-hosted and Anthropic-hosted); Claude Platform on AWS: `claude-sonnet-5-5`.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-sonnet-5-5`.
- No separate dated snapshot id is recorded; check the model page's alias and snapshot rows before pinning. Partner platforms add their own prefixes or profiles (see Platform IDs).
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

- Catalog price: $2/MTok input, $10/MTok output; cache writes $2.50/$4 (5m/1h), read $0.10 (cut from $0.20 on 2026-10-07).
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Partner platforms set their own prices. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Lifecycle and changes since the 2026-10-16 snapshot

- Released 2026-09-28 (the snapshot recorded unknown); retirement not sooner than 2027-09-28. Default effort `high`; knowledge cutoff June 2026.
- 2026-10-07: cache read price cut from $0.20 to $0.10 per MTok (0.05x base); other prices unchanged. Cache writes: 5m $2.50, 1h $4.
- Named replacement for `claude-sonnet-4-5-20250929`, deprecated 2026-09-30 and retiring 2026-11-30.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
> Source: https://platform.claude.com/docs/en/release-notes/overview
> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations

## Request-parameter constraints

- Thinking `disabled` is rejected; use `thinking: {type: "between_tools"}` at high effort or below. Forced `tool_choice` any/tool returns 400. Sampling parameters (temperature/top_p/top_k) are rejected at the model level.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
> Source: https://platform.claude.com/docs/en/api/migration-2026-10-21

## Platform IDs

| Platform | Model ID |
|---|---|
| Claude API | `claude-sonnet-5-5` |
| Amazon Bedrock (bedrock-mantle; access gated per account in the console) | `anthropic.claude-sonnet-5-5` |
| Google Cloud (Google managed and Anthropic managed) | `claude-sonnet-5-5` |
| Microsoft Foundry (Azure-hosted and Anthropic-hosted) | `claude-sonnet-5-5` |
| Claude Platform on AWS | `claude-sonnet-5-5` |

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
> Source: https://platform.claude.com/docs/en/models/overview

## Selection tradeoffs

### Strengths
- provider-described best speed/intelligence combination
- software engineering and agentic workflow usability

### Limitations and unknowns
- breaking differences from Sonnet 5 include tool-use, thinking-block and computer-use behavior; test migration
- cannot use older computer_20251124 tool on Claude API and Google Cloud
- thinking `disabled` is rejected (use `between_tools` at high effort or below); forced tool_choice any/tool returns 400
- retirement not sooner than 2027-09-28

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-11-13.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview

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

- https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/api/migration-2026-10-21
- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed

Fetched: 2026-11-13
