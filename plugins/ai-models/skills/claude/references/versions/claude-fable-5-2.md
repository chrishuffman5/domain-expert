# Claude Fable 5.2

Canonical model ID: `claude-fable-5-2`

## Identity and status

- Provider: Anthropic.
- Family: `claude`.
- Catalog role: reasoning, agentic, coding.
- Status: active (latest).
- Release: 2026-11-09.
- License/serving model: proprietary API model.
- Availability: Claude API; Amazon Bedrock (bedrock-runtime only: `global.anthropic.claude-fable-5-2` or `us.anthropic.claude-fable-5-2`; not on bedrock-mantle); Google Cloud (Google managed and Anthropic managed): `claude-fable-5-2`; Microsoft Foundry (Anthropic-hosted only; fast-mode id `claude-fable-5-2-fast`); Claude Platform on AWS: `claude-fable-5-2`.

> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview

## Canonical ID, version and aliases

- Canonical API/model identifier recorded by this catalog: `claude-fable-5-2`.
- No separate dated snapshot id is recorded; check the model page's alias and snapshot rows before pinning. Partner platforms add their own prefixes or profiles (see Platform IDs).
- If a deployment interface presents a different profile, regional route, or alias, verify it against that platform’s current model list before substituting it; aliases can have distinct lifecycle and billing.

> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview

## Context and capabilities

- Context/output: 1M tokens; 128K max output (not on the Batch API 300K-output beta list).
- Documented capabilities:
- text and image input
- text output
- adaptive thinking (always on; effort low/medium/high/xhigh/max, default high)
- tool use
- 1M context
- fast mode

> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview

## Price and billing conditions

- Catalog price: $8/MTok input, $40/MTok output; cache writes $10/$16 (5m/1h), read $0.20; batch 50% discount ($4/$20); fast mode $16/$80.
- Treat rates as provider- and tier-specific; modality, region, cache, batch, long-context, and contract modifiers may apply. Partner platforms set their own prices. Confirm current terms before budgeting.

> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Lifecycle and changes from Fable 5.1

- Released 2026-11-09; status Active (latest); retirement not sooner than 2027-11-09.
- `claude-fable-5-2` is a dateless pinned snapshot; the alias row on the model page repeats the same id.
- Price cut from Fable 5.1: $10/$50 to $8/$40 per MTok (-20%); cache read $0.25 to $0.20. Fable 5.1 keeps its own price.
- Adaptive thinking is always on and cannot be disabled; default effort `high`; levels low, medium, high, xhigh, max.
- Input text and images, output text. Reliable knowledge cutoff and training-data cutoff: June 2026. Latency: moderate.
- Uses the tokenizer introduced with Opus 4.7 (about 555k words per 1M tokens).
- Requires 30-day data retention; not available under zero data retention unless expressly authorized. Listed as a Covered Model.

> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview
> Source: https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
> Source: https://platform.claude.com/docs/en/about-claude/pricing

## Breaking changes to test before migrating

- Thinking-block prefix check is enforced on every account: editing system, tools or earlier messages and then replaying a thinking block returns 400 ("The block is bound to a different conversation"). Stopgap: beta `thinking-binding-controls-2026-08-01` with `thinking.block_binding.prefix_mismatch_behavior: "drop_block"`.
- Only Fable 5.2 and Mythos 5.2 read Fable 5.2 thinking blocks; other models, including Opus 5.5 and Fable 5.1, drop them. Fable 5.2 reads blocks from Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1, Mythos 5.1, Opus 5, Fable 5 and Mythos 5 on the Claude API and Google managed.
- `computer_20251124` returns 400 on every platform except Bedrock; use `computer_toolset_20260801`.
- Advisor tool: a Fable 5.2 executor accepts only a Fable 5.2 or Mythos 5.2 advisor; every executor accepts Fable 5.2 as advisor.
- `tool_choice` any/tool returns 400 (use auto plus strict tool use); thinking enabled/disabled returns 400; omit temperature, top_p and top_k.
- Beta features: compaction on demand (`compact-2026-09-04`) and mid-conversation tool changes (`inline-tools-2026-09-15`). Server-side fallback targets permitted: Opus 4.8 and Opus 5.

> Source: https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2

## Fast mode

- `speed: "fast"` in the Messages API, no beta header: $16 input / $80 output per MTok, up to 2.5x output tokens per second.
- Available on the Claude API, Google Cloud (Anthropic managed and Google managed; Google sets its own prices) and Microsoft Foundry (Anthropic-hosted, separate id `claude-fable-5-2-fast`). Not on Claude Platform on AWS, which offers no fast mode.

> Source: https://platform.claude.com/docs/en/build-with-claude/fast-mode
> Source: https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws

## Platform IDs

| Platform | Model ID |
|---|---|
| Claude API | `claude-fable-5-2` |
| Amazon Bedrock (bedrock-runtime only; not on bedrock-mantle) | `global.anthropic.claude-fable-5-2` or `us.anthropic.claude-fable-5-2` (base `anthropic.claude-fable-5-2`; eu/jp/apac profiles: No) |
| Google Cloud (Google managed) | `claude-fable-5-2` |
| Google Cloud (Anthropic managed) | `claude-fable-5-2` |
| Microsoft Foundry (Anthropic-hosted only, not Azure-hosted) | `claude-fable-5-2` (fast: `claude-fable-5-2-fast`) |
| Claude Platform on AWS | `claude-fable-5-2` |

> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry

## Vendor announcement claims

- Announced 2026-11-09 with Mythos 5.2. Anthropic says outputs are up to 30% faster than Fable 5.1 / Mythos 5.1, that Fable and Mythos are the same underlying model with Fable carrying stronger cyber/bio safeguards, and that classifiers block about 55% fewer queries than on Fable 5.1.
- Self-reported results vs Opus 5.5: FrontierSWE v2 69.9% vs 62.3%; Terminal-Bench-Science 0.1 74.6% vs 58.7%; OSWorld 2.1 89.3% vs 87.2%; HLE with tools 74.2% vs 67.7%. Vendor-reported, not independently verified; run workload evals instead of relying on them.

> Source: https://www.anthropic.com/claude-fable-and-mythos-5-2

## Limited-access twin (no catalog row)

- `claude-mythos-5-2` has the same specs and price as Fable 5.2 but is "Active (verification required)": only organizations verified through Anthropic programs (Cyber Verification Program; the announcement also names a Life Sciences Verification Program). It is not listed for Claude Platform on AWS.

> Source: https://platform.claude.com/docs/en/models/mythos-5-2/overview
> Source: https://www.anthropic.com/claude-fable-and-mythos-5-2

## Selection tradeoffs

### Strengths
- demanding reasoning and long-horizon agentic work
- 20% lower token price than Fable 5.1; vendor reports outputs up to 30% faster than Fable 5.1
- vendor-reported benchmark gains over Opus 5.5 (not independently verified)

### Limitations and unknowns
- costs twice Opus 5.5's token rate; select only where evals justify it
- requires 30-day data retention; not available under zero data retention unless expressly authorized
- thinking enabled/disabled, forced tool_choice and temperature/top_p/top_k return 400; computer_20251124 returns 400 except on Bedrock
- thinking-block prefix check enforced: replaying a thinking block after editing earlier context returns 400

- Adoption evidence: Unknown; no comparable public usage/adoption metric inspected (released 2026-11-09).
- Scope/date: Anthropic model API / 2026-11-13.
- Do not infer zero use from unknown public telemetry or compare unlike proxies as a shared rank.

> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview

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

- https://platform.claude.com/docs/en/models/fable-5-2/overview
- https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/build-with-claude/fast-mode
- https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
- https://www.anthropic.com/claude-fable-and-mythos-5-2
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/models/mythos-5-2/overview
- https://platform.claude.com/docs/en/about-claude/model-deprecations

Fetched: 2026-11-13
