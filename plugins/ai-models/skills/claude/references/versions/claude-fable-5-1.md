# Claude Fable 5.1

Canonical model ID: `claude-fable-5-1`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: reasoning, agentic, coding.
- Status: active (superseded by claude-fable-5-2 on 2026-11-09; retirement not sooner than 2027-09-01).
- Release: 2026-09-01.
- License/serving model: proprietary API model.
- Availability: Claude API; Amazon Bedrock (bedrock-mantle `anthropic.claude-fable-5-1`, open access); Google Cloud (Google managed): `claude-fable-5-1`; Microsoft Foundry (Anthropic-hosted only); Claude Platform on AWS: `claude-fable-5-1`.

> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-fable-5-1`.
- No separate dated snapshot id is recorded; check the model page's alias and snapshot rows before pinning. Partner platforms add their own prefixes or profiles (see Platform IDs).
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
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Partner platforms set their own prices. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Lifecycle and changes since the 2026-10-16 snapshot

- No longer latest: superseded by `claude-fable-5-2` on 2026-11-09. Still Active; retirement not sooner than 2027-09-01. The models overview lists it under "All models" only.
- Price unchanged at $10/$50 per MTok, cache read $0.25. Fable 5.2 costs $8/$40.
- Fable 5.1 drops Fable 5.2 thinking blocks; Fable 5.2 can read Fable 5.1 blocks. Plan one-way migration.
- Limited-access companion `claude-mythos-5-1` ($10/$50, verification required) launched the same day; it has no catalog row.

> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations
> Source: https://platform.claude.com/docs/en/models/overview
> Source: https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2

## Platform IDs

| Platform | Model ID |
|---|---|
| Claude API | `claude-fable-5-1` |
| Amazon Bedrock (bedrock-mantle, open access) | `anthropic.claude-fable-5-1` |
| Google Cloud (Google managed) | `claude-fable-5-1` |
| Microsoft Foundry (Anthropic-hosted only) | `claude-fable-5-1` |
| Claude Platform on AWS | `claude-fable-5-1` |

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws

## Selection tradeoffs

### Strengths
- demanding reasoning and long-horizon agentic coding
- multistep research and document, spreadsheet, slide work

### Limitations and unknowns
- superseded by Fable 5.2, which costs less ($8/$40 vs $10/$50); prefer 5.2 for new work unless a pinned workload needs 5.1
- slower and materially more expensive than Opus 5.5; select only where evals justify it
- forced tool use now errors; thinking blocks model-specific; Fable 5.1 drops Fable 5.2 thinking blocks

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected.
- Scope/date: Anthropic model API / 2026-11-13.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview

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

- https://platform.claude.com/docs/en/models/fable-5-1/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws

Fetched: 2026-11-13
