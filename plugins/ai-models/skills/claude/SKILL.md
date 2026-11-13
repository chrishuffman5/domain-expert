---
name: claude
description: "Select among Anthropic Claude model identities by workload, reasoning depth, latency, token budget, lifecycle, and access. Use for Claude Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 model suitability, version tradeoffs, lifecycle and deprecations, limited-access Mythos models, and per-cloud Claude model IDs. Do NOT use for model APIs, SDKs, agents/harnesses, routing, training, or evaluation infrastructure; use `ai`. Do NOT use for Gemini or any other provider family; use its family skill."
license: MIT
---

# Claude model selection

This skill covers Claude model identity and suitability. It helps choose a Claude family member, distinguish provider model IDs and versions, and reason about capability, context, cost, and lifecycle. It does not teach API implementation.

Claude is a family, not a single interchangeable endpoint. The catalog has five selected identities: Fable 5.2 (newest, released 2026-11-09), Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 (superseded by Fable 5.2 but still Active). Limited-access models such as Mythos 5.2 have no catalog rows; see the limited-access section. Their release status, API ID, context, prices, limitations, and source links are in the linked reference files. Check a reference before relying on a volatile number.

## Do NOT use
> Source: https://platform.claude.com/docs/en/models/overview


- Do NOT use this skill for Anthropic Messages API mechanics, SDK selection, request/response schemas, authentication, streaming code, or error handling; use the `ai` plugin.
- Do NOT use it to build or configure agent harnesses, tools, MCP servers, memory, orchestration, or computer-use integrations; use the `ai` plugin.
- Do NOT use it for model-provider routing, gateways, load balancing, failover, cloud inference configuration, or deployment endpoints; use the `ai` plugin.
- Do NOT use it to design training, fine-tuning, benchmark, red-team, or evaluation infrastructure; use the `ai` plugin.
- Do NOT use it to choose Gemini, OpenAI, open-weight, or decision-model families; route to their family skill.
- Do NOT treat `ai:jev` as a generative Claude model-selection request. For typed semantic decision output, use the Jev family skill; for Jev API integration, use `ai`.

## Route by task shape
> Source: https://platform.claude.com/docs/en/models/overview


| Workload | First candidate | Compare against | Why |
|---|---|---|---|
| General knowledge work or coding | Claude Opus 5.5 | Sonnet 5.5 | Anthropic recommends Opus as the starting point; Sonnet trades some headroom for speed and lower token price. |
| High-throughput classification, routing, extraction | Claude Haiku 5.5 | Sonnet 5.5 | Haiku is the low-cost, latency-sensitive tier; measure quality on representative examples. |
| Long-running coding agent or knowledge workflow | Claude Opus 5.5 | Fable 5.2 | Start with Opus; move to the more expensive Fable only if evaluation at higher Opus effort falls short. |
| Demanding multistep reasoning or research | Claude Fable 5.2 | Opus 5.5 | Fable is positioned for harder reasoning and long-horizon work; compare quality gain against latency and cost. |
| Existing workload validated on Fable 5.1 | Claude Fable 5.2 | Fable 5.1 | Fable 5.2 is cheaper ($8/$40 vs $10/$50) and newer; re-run the workload because thinking-block, tool-choice and computer-use behavior changed. |
| Budget-constrained task with quality tolerance | Haiku 5.5 | Sonnet 5.5 | Validate the failure cost; the cheapest model is unsuitable when errors have expensive consequences. |
| Multi-modal document work | Opus 5.5 or Sonnet 5.5 | Haiku 5.5 | All listed models support text/image input; compare extraction accuracy and context usage on the actual document set. |

These are starting points, not a leaderboard. The catalog contains no comparable public usage metric for these models. Provider recommendation labels describe intended fit, not independent performance evidence.

## Choosing a model deliberately
> Source: https://platform.claude.com/docs/en/models/overview


Start by describing the output and the cost of error. A quick route/classify task and a long-horizon software change have different failure modes. Do not choose by tier label alone.

1. State whether the task needs text only, image understanding, tools, long context, or extended reasoning.
2. Estimate input and output token volume using the serving platform’s tokenizer and the real prompt shape.
3. Decide the acceptable latency and the consequence of an incorrect answer.
4. Choose the least costly candidate that meets those needs in representative task checks.
5. Compare a stronger alternative on examples where the baseline failed, not only on easy cases.
6. Record the exact model ID, serving platform, status check date, and relevant price tier with the decision.
7. Revisit the choice after a model release, a material prompt change, or a change in workload mix.

Prefer a small paired evaluation over assumptions based on general benchmarks. Include routine cases, edge cases, ambiguous inputs, long inputs, and cases where the correct response is to abstain or ask for more information. Score task correctness separately from style, response time, and token consumption.

A larger model may reduce retries or downstream review, but this is workload-dependent. A smaller model may be cheaper per token while producing longer answers, requiring more tool calls, or causing additional human review. Compare total task cost, not just a single input-token rate.

When tasks vary substantially, use a clear rule for splitting them before calling a model: easy/high-volume work can use Haiku, while uncertain or high-impact cases can go to Sonnet or Opus after an application-level check. This is a selection pattern; implementing router logic belongs in `ai`.

Avoid routing based only on prompt length. A short question may require difficult reasoning. A long repetitive document may need careful extraction but not deeper reasoning. Evaluate both semantic difficulty and context size.

## Claude tier guidance
> Source: https://platform.claude.com/docs/en/models/overview


### Opus 5.5
> Source: https://platform.claude.com/docs/en/models/opus-5-5/overview


Choose Opus 5.5 for long-running agentic coding and knowledge work, and as Anthropic’s documented first choice for most workloads. Its reference lists a 1M-token context window and 128K max output. Its listed base rate is $4 per million input tokens and $20 per million output tokens.

Adaptive thinking is always on. The `effort` setting controls thinking depth; greater effort can change latency and token use. The default effort is medium. Account for thinking tokens in output consumption and set an output ceiling appropriate to the task.

Opus 5.5 is more expensive than Sonnet 5.5. Keep it when evaluation shows a meaningful quality or completion advantage on difficult work. Consider Sonnet for routine high-volume work where the quality difference does not justify Opus cost.

Opus 5.5 changes behavior from Opus 5. Forced tool use can error, thinking blocks are tied to model and conversation, and the older computer-use tool is not accepted on some listed platforms. Review the version reference and test migration-sensitive workflows before switching.

Fast mode for Opus 5.5 left research preview on 2026-10-15 (no beta header) at $8/$40 per million tokens and is available on Microsoft Foundry (`claude-opus-5-5-fast`) and Google Cloud (Anthropic managed). Choose it when latency matters more than the 2x token price. Opus 5.5 is also the named migration target for Opus 4.8 fast mode, which is removed on 2026-11-30.

### Sonnet 5.5
> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview


Choose Sonnet 5.5 when a balanced speed/intelligence profile matters. Anthropic positions it as its best combination of speed and intelligence. The selected reference lists 1M context, 128K maximum output, and base rates of $2 input / $10 output per million tokens.

Sonnet 5.5 was released 2026-09-28. Its cache read price fell from $0.20 to $0.10 per million tokens on 2026-10-07 (cache writes $2.50 for 5 minutes, $4 for 1 hour), which matters for repeated long system prompts. Default effort is `high`; thinking cannot be set to `disabled` (use `between_tools` at high effort or below).

Use Sonnet as a practical comparator for Opus on coding, analysis, and agentic tasks. Test the quality gap on the hard tail; do not assume a model name or family tier predicts your own workload result.

Sonnet 5.5 has breaking differences from Sonnet 5 in thinking, tool-use, computer-use compatibility, and advisor-tool acceptance. Recheck prior conversation replay, tool constraints, and outputs between tool calls when migrating.

### Haiku 5.5
> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview


Choose Haiku 5.5 for high-volume, latency-sensitive work such as classification, extraction, routing, and subagent tasks. It is the fastest mainline Claude tier in the inspected provider comparison.

Its price is input-length dependent: the catalog records $0.10/$0.50 per million input/output tokens for prompts up to 100K, and $0.50/$2.50 for prompts over 100K. Check how the provider counts the full prompt and output before estimating batch costs.

Haiku 5.5 uses a newer tokenizer than Haiku 4.5. Equivalent text can consume roughly 30% more tokens, so carry tokenization changes into both context planning and budget estimates. It supports a 1M context and up to 128K output, but a large window does not make long prompts inexpensive.

Thinking blocks from Haiku 5.5 work only in the account that produced them or an account linked to it. Avoid assuming they can be replayed across unrelated accounts or providers.

Haiku 5.5 (released 2026-10-07) returns 400 for `budget_tokens`, sampling parameters, prefill, and `computer_20250124`, all of which Haiku 4.5 accepted. Haiku 4.5 is still Active, so migration is optional today; test these request shapes before switching.

### Fable 5.2
> Source: https://platform.claude.com/docs/en/models/fable-5-2/overview


Choose Fable 5.2 (`claude-fable-5-2`, released 2026-11-09) for demanding reasoning and long-horizon agentic work when Opus 5.5 at higher effort still misses the acceptance bar. It is Anthropic's newest model and replaces Fable 5.1 at a lower price: $8 input / $40 output per million tokens (Fable 5.1 is $10/$50), cache read $0.20, batch 50% off, fast mode $16/$80. It is still twice Opus 5.5's token rate, so keep a measured quality gate.

Adaptive thinking is always on with default effort `high`. Fable 5.2 returns 400 for thinking enabled/disabled, forced `tool_choice`, sampling parameters, and `computer_20251124` (except on Bedrock). It enforces a thinking-block prefix check: replaying a thinking block after editing earlier system, tool, or message content fails. Only Fable 5.2 and Mythos 5.2 can read its thinking blocks, so a mid-conversation switch to another model drops them.

Fable 5.2 requires 30-day data retention and is not available under zero data retention unless expressly authorized; check this before choosing it for regulated workloads. Anthropic's announcement reports faster output than Fable 5.1 and benchmark gains over Opus 5.5; those figures are vendor-reported, not independent evidence.

On Amazon Bedrock it is reachable only through bedrock-runtime (`global.anthropic.claude-fable-5-2` or `us.anthropic.claude-fable-5-2`), not bedrock-mantle; on Microsoft Foundry it is Anthropic-hosted only. See the cloud ID table below.

### Fable 5.1 (superseded)
> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations


Fable 5.1 (`claude-fable-5-1`, released 2026-09-01) is no longer the latest Fable. It remains Active with retirement not sooner than 2027-09-01, at $10 input / $50 output per million tokens and cache read $0.25. Do not choose it for new work: Fable 5.2 is newer and cheaper.

Keep Fable 5.1 only where a workload is validated on it and has not yet been re-evaluated, or where a platform route needs it (for example Bedrock bedrock-mantle, which carries `anthropic.claude-fable-5-1` but not Fable 5.2). Fable 5.1 drops Fable 5.2 thinking blocks, so treat a Fable 5.1 to 5.2 switch as one-way within a conversation.

## Limited-access and specialist Claude models
> Source: https://platform.claude.com/docs/en/models/mythos-5-2/overview


These models have no catalog rows because access is restricted. Mention them only when the requester can qualify.

- **Claude Mythos 5.2** (`claude-mythos-5-2`, 2026-11-09): same model, specs, and price as Fable 5.2 ($8/$40, fast mode $16/$80), status "Active (verification required)". Only organizations verified through Anthropic programs can call it (the Cyber Verification Program; the announcement also names a Life Sciences Verification Program). Fable carries stronger cyber/bio safeguards than Mythos. IDs: Claude API, Google Cloud and Foundry (Anthropic-hosted) `claude-mythos-5-2` (Foundry fast `claude-mythos-5-2-fast`); Bedrock bedrock-runtime `global.anthropic.claude-mythos-5-2` or `us.anthropic.claude-mythos-5-2`. Not available on Claude Platform on AWS.
- **Claude Mythos 5.1** (`claude-mythos-5-1`, 2026-09-01): limited companion to Fable 5.1 at $10/$50; Bedrock mantle `anthropic.claude-mythos-5-1` requires verification.
- `claude-mythos-preview` has been deprecated since 2026-06-09.

For an unverified organization, select Fable 5.2 instead. Do not plan a workload around Mythos access you do not have.

## API version 2026-10-21 and sampling parameters
> Source: https://platform.claude.com/docs/en/api/migration-2026-10-21


The `anthropic-version` header `2026-10-21` is the default for the latest SDK majors and appears in Bedrock mantle, Google managed, and Foundry examples. It changes what a model choice can rely on:

- `temperature`, `top_p`, and `top_k` return 400 even at default values. Models that still accept other values (for example Sonnet 4.6) lose the ability to lower temperature under this version, with no replacement. If a workload depends on low temperature, keep those requests on `2023-06-01` or move the control into prompt design and evaluation.
- `document` blocks directly in assistant messages and `citations` on user-message text blocks return 400.
- Bedrock models 4.6 and lower do not support `2026-10-21`; they need the older SDK major.
- Separately from the version, Fable 5.2, Opus 5.5, Sonnet 5.5, and Haiku 5.5 reject sampling parameters and forced `tool_choice` at the model level; Fable 5.2 and Opus 5.5 also reject thinking enabled/disabled; Haiku 5.5 also rejects prefill and `budget_tokens`.

Selection consequence: do not choose a current Claude model on the assumption that you can tune randomness per request. Measure output variance in evaluation instead. SDK upgrade steps belong to the `ai` plugin.

## Context, output, and cost
> Source: https://platform.claude.com/docs/en/about-claude/pricing


Context capacity is an upper bound, not a recommended prompt size. Include system instructions, history, supplied documents, tool results, and generated output in the budget. Leave headroom for the answer and for reasoning where the model uses adaptive thinking.

Claude’s listed token price excludes product-level costs outside the model’s base inference, such as downstream tools, review, and application retries. Cache writes, cache reads, batch discounts, long-context pricing, and data residency can change the effective rate.

The current research notes that Claude 4.6 and later may apply a 1.1x multiplier for US-only inference on Anthropic-operated platforms. Partner platforms set their own prices. The catalog references provide exact model rates and conditions; consult the provider page for current terms.

Do not compare a prompt under 100K with one over 100K without including the Haiku 5.5 price step. Measure at least median and high-percentile prompt length. Include output length and thinking tokens if reported.

For large document workflows, compare retrieval or staged summarization against one huge context. This is a workload design decision; validate that staged processing preserves required evidence and citations.

If a model is used for high-impact outputs, include a human review path or a separate deterministic validation step. A larger context or stronger model does not guarantee factual correctness.

## IDs, versions, and lifecycle
> Source: https://platform.claude.com/docs/en/models/overview


Use the exact canonical IDs in the table and reference files. The catalog records un-dated current aliases such as `claude-opus-5-5`; do not silently replace them with a guessed date-stamped ID. This selected catalog does not record separate snapshot IDs or alternate aliases.

Anthropic documents model IDs, aliases, and pinned snapshots separately. If reproducibility requires a pinned version, locate the actual identifier in current official docs and record it explicitly in deployment configuration. Do not infer a snapshot from the model’s release date.

Status can differ between Anthropic-operated API and partner-operated platforms. Anthropic's deprecation page says lifecycle dates apply to Anthropic-operated surfaces; Bedrock and Google Cloud maintain their own schedules. Recheck the exact serving platform before migration.

Anthropic says it notifies customers with active deployments at least 60 days before retirement for publicly released models. That notice does not remove the need to plan upgrades: run the replacement against production-shaped examples before the deadline.

The catalog is a dated selection snapshot. An `active` status is not a promise of future availability. Revalidate status, ID, price, context, region, and account eligibility for any new production choice.

### Deprecations, retirements, and replacements (as of 2026-11-13)
> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations


| Model or feature | Status | Date | Replacement |
|---|---|---|---|
| `claude-sonnet-4-5-20250929` | Deprecated 2026-09-30 | Retires 2026-11-30 | `claude-sonnet-5-5` |
| Opus 4.8 fast mode (`speed: "fast"`) | Deprecated 2026-10-30 | Removed 2026-11-30 (requests then error); the model itself stays Active, not sooner than 2027-05-28 | Opus 5.5 fast mode |
| `claude-opus-4-1-20250805` | Retired on the Claude API | 2026-08-05 | `claude-opus-4-8` (release notes recommend Opus 5); still listed on Bedrock and Google managed |
| `claude-haiku-4-5-20251001` | Active | Not sooner than 2026-10-15 (passed; no retirement announced) | Plan for `claude-haiku-5-5` |
| `claude-opus-4-5-20251101` | Active | Not sooner than 2026-11-24 | No replacement announced |
| `claude-fable-5-1` | Active, superseded | Not sooner than 2027-09-01 | `claude-fable-5-2` |

Retirement floors for the catalog models: Fable 5.2 2027-11-09, Haiku 5.5 2027-10-07, Sonnet 5.5 2027-09-28, Opus 5.5 2027-09-22, Fable 5.1 2027-09-01. Sonnet 5 kept its $2/$10 price: the increase to $3/$15 scheduled for 2026-09-01 was cancelled on 2026-08-10.

### Cloud model IDs
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock


Model IDs differ by serving surface. This table is identity information for selection; endpoint configuration belongs to `ai`.

| Model | Claude API, Claude Platform on AWS, Google Cloud | Amazon Bedrock | Microsoft Foundry |
|---|---|---|---|
| Fable 5.2 | `claude-fable-5-2` (Google managed and Anthropic managed) | bedrock-runtime only: `global.anthropic.claude-fable-5-2`, `us.anthropic.claude-fable-5-2` | Anthropic-hosted only; fast `claude-fable-5-2-fast` |
| Opus 5.5 | `claude-opus-5-5` | bedrock-mantle `anthropic.claude-opus-5-5` (access gated) | Azure-hosted and Anthropic-hosted; fast `claude-opus-5-5-fast` |
| Sonnet 5.5 | `claude-sonnet-5-5` | bedrock-mantle `anthropic.claude-sonnet-5-5` (access gated) | Azure-hosted and Anthropic-hosted |
| Haiku 5.5 | `claude-haiku-5-5` | bedrock-mantle `anthropic.claude-haiku-5-5` (access gated) | Azure-hosted and Anthropic-hosted |
| Fable 5.1 | `claude-fable-5-1` (Google managed; not in the models overview's Anthropic managed column) | bedrock-mantle `anthropic.claude-fable-5-1` (open access) | Anthropic-hosted only |

- Bedrock has two endpoints: bedrock-mantle (Messages API) and bedrock-runtime (InvokeModel/Converse). Fable 5.2 and Mythos 5.2 are only on bedrock-runtime; the other 5.x models use the mantle table. Regional endpoints cost 10% more than global.
- Google Cloud has two offerings: Google managed (formerly Vertex AI; Google sets prices and lifecycle dates) and Anthropic managed (same IDs as the Claude API; Google Cloud credentials only, no API keys; billed through Google Cloud Marketplace).
- Claude Platform on AWS uses Claude API IDs with no `anthropic.` prefix, follows Anthropic lifecycle, and offers no fast mode, HIPAA readiness, or Mythos models.
- Foundry follows the Claude API lifecycle and has no Message Batches or Models API.

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
> Source: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws

## Migration and workload checks
> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations


When changing a Claude model, compare more than final answer text. Check tool selection, tool argument shape, tool refusal/error behavior, structured output, streaming progress, and multi-turn continuity.

Test prompts that contain hidden assumptions, conflicting instructions, malformed attachments, and empty or partial tool results. Strong models can still follow a mistaken premise or produce confident unsupported claims.

Confirm downstream code does not assume that all intermediate content appears in ordinary text blocks. Anthropic documents changes where between-tool text may be represented in thinking blocks, affecting applications that display progress.

Check whether a prior workflow relied on manual thinking controls, specific tool-use modes, sampling parameters, or the `computer_20251124` tool. Version upgrades and API version `2026-10-21` can invalidate these assumptions.

For long-running tasks, set a completion criterion and a reasonable time/cost limit outside the model. Retry policy, cancellation, logs, and escalation are integration concerns owned by `ai`.

A successful model migration is measured by the end-to-end task: quality, completion rate, review burden, latency, and total cost. Do not declare success from a single benchmark score.

## Tradeoff cases
> Source: https://platform.claude.com/docs/en/models/overview


### Coding work
> Source: https://platform.claude.com/docs/en/models/overview


For a small patch with clear acceptance tests, begin by comparing Sonnet 5.5 and Opus 5.5. The difference in token price is material across large call volumes, so measure whether Opus meaningfully reduces incomplete changes or review time.

For a repository-wide change with multiple interacting components, start with Opus 5.5. Compare Fable 5.2 only if Opus still fails the required reasoning or planning checks. Fable's higher cost should be justified by a repeatable quality gain, not a single impressive example.

For code review, separate defect discovery from explanation quality. A verbose review is not necessarily more accurate. Include seeded defects, clean code, and misleading comments in the evaluation set.

### Knowledge work
> Source: https://platform.claude.com/docs/en/models/overview


For synthesis across long documents, track whether the model used all relevant evidence and whether each conclusion can be traced to a source. A 1M context is a capacity feature, not a guarantee that all details receive equal attention.

For frequent short summaries, compare Haiku and Sonnet using the same source segments. Include factual omission, unsupported additions, and the cost of a human correction pass in the score.

For a high-impact recommendation, keep the decision criteria explicit and make the model expose uncertainty or missing information. A model choice cannot replace domain review or a documented policy.

### High-volume routing patterns
> Source: https://platform.claude.com/docs/en/models/overview


If a workflow uses Haiku for the first pass, define escalation conditions using observable task properties such as missing required fields, contradictory source facts, or failure of a deterministic schema check.

Do not escalate solely on the model's self-assessed confidence unless that signal has been calibrated for the workload. Compare escalation rates and false negatives against a reviewed sample.

Keep an application-level fallback for unavailable or access-limited models. Choosing which model is the fallback is selection guidance; implementing retry and provider routing belongs to `ai`.

### Cost review
> Source: https://platform.claude.com/docs/en/about-claude/pricing


Compute a cost range from actual prompt and output distributions. Use a percentile above the median because rare long requests can dominate spend.

Include cache creation and reads when repeated system prompts or reference material are reused. A cache is beneficial only when its hit rate and retention duration offset its write and storage costs.

Apply batch discounts only to work that can tolerate batch latency and has a supported request path. Do not assume a batch discount applies to synchronous interactive use.

Recheck the pricing page after a release, contract change, platform migration, or change in inference geography. The catalog rates are evidence from a dated snapshot.

## Common selection mistakes
> Source: https://platform.claude.com/docs/en/models/overview


- Choosing Fable by default because it is the highest-priced tier, without proving that the workload needs it.
- Sending every short request to Haiku even when its semantic difficulty or failure cost is high.
- Comparing only model input prices while ignoring generated tokens, thinking tokens, cache writes, retries, and human review.
- Assuming a shared 1M context means a prompt should contain every available document.
- Assuming a model can preserve tool-state or prior thinking blocks across every model switch.
- Treating an API alias as an immutable snapshot without checking the versioning documentation.
- Keeping Fable 5.1 for new work after Fable 5.2 shipped at a lower price.
- Planning on `temperature` or `top_p` control with a current Claude model or API version `2026-10-21`.
- Assuming a Claude model has the same ID, endpoint, or feature set on Bedrock, Google Cloud, and Foundry.
- Treating an unknown adoption field as no usage or as a negative recommendation.
- Treating a provider capability description as a quality guarantee for a specific task.

## Routing table
> Source: https://platform.claude.com/docs/en/models/overview


| Catalog model | Reference | Use when |
|---|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) | [version details](references/versions/claude-opus-5-5.md) | Default starting point for demanding general, coding, or long-running agentic work. |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | [version details](references/versions/claude-sonnet-5-5.md) | Speed/intelligence balance for general and coding tasks. |
| Claude Haiku 5.5 (`claude-haiku-5-5`) | [version details](references/versions/claude-haiku-5-5.md) | Latency-sensitive, high-volume classification, extraction, and routing. |
| Claude Fable 5.2 (`claude-fable-5-2`) | [version details](references/versions/claude-fable-5-2.md) | Higher-effort reasoning and long-horizon tasks that justify higher cost; newest Claude model. |
| Claude Fable 5.1 (`claude-fable-5-1`) | [version details](references/versions/claude-fable-5-1.md) | Superseded; keep only for validated existing workloads or routes without Fable 5.2. |

## Cross-family boundaries
> Source: https://platform.claude.com/docs/en/models/overview


Choose the `gemini` skill when the decision concerns a Google Gemini endpoint, especially Gemini's Live audio and transcription models. Choose the `gemma` skill for Google open-weight Gemma models.

Choose `ai` when the task is how to call Claude from code, which SDK to use, how to connect tools, or how to build a provider router. The model references are selection material, not executable integration guides.

Choose `ai` for training, fine-tuning mechanics, benchmark orchestration, or evaluation infrastructure. This skill can suggest what workload to compare, but it does not prescribe a harness implementation.

## Sources

The model-specific references below carry the catalog claims, limitations, adoption evidence, official URLs, and retrieval date for each selected model. Use them as the source set for model-specific decisions.

- [Claude Opus 5.5](references/versions/claude-opus-5-5.md)
- [Claude Sonnet 5.5](references/versions/claude-sonnet-5-5.md)
- [Claude Haiku 5.5](references/versions/claude-haiku-5-5.md)
- [Claude Fable 5.2](references/versions/claude-fable-5-2.md)
- [Claude Fable 5.1](references/versions/claude-fable-5-1.md)
- [Anthropic model overview](https://platform.claude.com/docs/en/models/overview)
- [Anthropic model lifecycle](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Claude Fable 5.2 overview](https://platform.claude.com/docs/en/models/fable-5-2/overview)
- [What's new in Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)
- [Claude Mythos 5.2 overview](https://platform.claude.com/docs/en/models/mythos-5-2/overview)
- [Fable and Mythos 5.2 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anthropic release notes](https://platform.claude.com/docs/en/release-notes/overview)
- [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode)
- [API version 2026-10-21 migration](https://platform.claude.com/docs/en/api/migration-2026-10-21)
- [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
- [Claude on Amazon Bedrock (legacy runtime)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)
- [Claude on Google Cloud, Google managed](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)
- [Claude on Google Cloud, Anthropic managed](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)
- [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)
- [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)

Fetched: 2026-11-13
