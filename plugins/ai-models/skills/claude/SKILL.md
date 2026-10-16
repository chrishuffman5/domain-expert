---
name: claude
description: "Select among Anthropic Claude model identities by workload, reasoning depth, latency, token budget, lifecycle, and access. Use for Claude Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 model suitability and version tradeoffs. Do NOT use for model APIs, SDKs, agents/harnesses, routing, training, or evaluation infrastructure; use `ai`. Do NOT use for Gemini or any other provider family; use its family skill."
license: MIT
---

# Claude model selection

This skill covers Claude model identity and suitability. It helps choose a Claude family member, distinguish provider model IDs and versions, and reason about capability, context, cost, and lifecycle. It does not teach API implementation.

Claude is a family, not a single interchangeable endpoint. The catalog has four selected identities: Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1. Their release status, API ID, context, prices, limitations, and source links are in the linked reference files. Check a reference before relying on a volatile number.

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
| Long-running coding agent or knowledge workflow | Claude Opus 5.5 | Fable 5.1 | Start with Opus; move to the more expensive Fable only if evaluation at higher Opus effort falls short. |
| Demanding multistep reasoning or research | Claude Fable 5.1 | Opus 5.5 | Fable is positioned for harder reasoning and long-horizon work; compare quality gain against latency and cost. |
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

### Sonnet 5.5
> Source: https://platform.claude.com/docs/en/models/sonnet-5-5/overview


Choose Sonnet 5.5 when a balanced speed/intelligence profile matters. Anthropic positions it as its best combination of speed and intelligence. The selected reference lists 1M context, 128K maximum output, and base rates of $2 input / $10 output per million tokens.

Use Sonnet as a practical comparator for Opus on coding, analysis, and agentic tasks. Test the quality gap on the hard tail; do not assume a model name or family tier predicts your own workload result.

Sonnet 5.5 has breaking differences from Sonnet 5 in thinking, tool-use, computer-use compatibility, and advisor-tool acceptance. Recheck prior conversation replay, tool constraints, and outputs between tool calls when migrating.

### Haiku 5.5
> Source: https://platform.claude.com/docs/en/models/haiku-5-5/overview


Choose Haiku 5.5 for high-volume, latency-sensitive work such as classification, extraction, routing, and subagent tasks. It is the fastest mainline Claude tier in the inspected provider comparison.

Its price is input-length dependent: the catalog records $0.10/$0.50 per million input/output tokens for prompts up to 100K, and $0.50/$2.50 for prompts over 100K. Check how the provider counts the full prompt and output before estimating batch costs.

Haiku 5.5 uses a newer tokenizer than Haiku 4.5. Equivalent text can consume roughly 30% more tokens, so carry tokenization changes into both context planning and budget estimates. It supports a 1M context and up to 128K output, but a large window does not make long prompts inexpensive.

Thinking blocks from Haiku 5.5 work only in the account that produced them or an account linked to it. Avoid assuming they can be replayed across unrelated accounts or providers.

### Fable 5.1
> Source: https://platform.claude.com/docs/en/models/fable-5-1/overview


Choose Fable 5.1 for demanding reasoning and long-horizon agentic work when Opus 5.5 at higher effort still misses the task’s acceptance bar. Provider positioning also includes multistep research and complex document, spreadsheet, and slide work.

Fable costs $10 per million input tokens and $50 per million output tokens in the catalog, with a 1M context and 128K output. It is slower and materially more expensive than Opus 5.5. Use a measured quality gate before paying the premium broadly.

Adaptive thinking is always on; steer effort rather than assuming thinking can be disabled. Forced tool use errors, and thinking blocks have stricter model/conversation continuity than older workflows. Check the exact reference for cache prices and batch modifiers.

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

## Migration and workload checks
> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations


When changing a Claude model, compare more than final answer text. Check tool selection, tool argument shape, tool refusal/error behavior, structured output, streaming progress, and multi-turn continuity.

Test prompts that contain hidden assumptions, conflicting instructions, malformed attachments, and empty or partial tool results. Strong models can still follow a mistaken premise or produce confident unsupported claims.

Confirm downstream code does not assume that all intermediate content appears in ordinary text blocks. Anthropic documents changes where between-tool text may be represented in thinking blocks, affecting applications that display progress.

Check whether a prior workflow relied on manual thinking controls, specific tool-use modes, or the `computer_20251124` tool. Version upgrades can invalidate these assumptions.

For long-running tasks, set a completion criterion and a reasonable time/cost limit outside the model. Retry policy, cancellation, logs, and escalation are integration concerns owned by `ai`.

A successful model migration is measured by the end-to-end task: quality, completion rate, review burden, latency, and total cost. Do not declare success from a single benchmark score.

## Tradeoff cases
> Source: https://platform.claude.com/docs/en/models/overview


### Coding work
> Source: https://platform.claude.com/docs/en/models/overview


For a small patch with clear acceptance tests, begin by comparing Sonnet 5.5 and Opus 5.5. The difference in token price is material across large call volumes, so measure whether Opus meaningfully reduces incomplete changes or review time.

For a repository-wide change with multiple interacting components, start with Opus 5.5. Compare Fable 5.1 only if Opus still fails the required reasoning or planning checks. Fable's higher cost should be justified by a repeatable quality gain, not a single impressive example.

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
- Treating an unknown adoption field as no usage or as a negative recommendation.
- Treating a provider capability description as a quality guarantee for a specific task.

## Routing table
> Source: https://platform.claude.com/docs/en/models/overview


| Catalog model | Reference | Use when |
|---|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) | [version details](references/versions/claude-opus-5-5.md) | Default starting point for demanding general, coding, or long-running agentic work. |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | [version details](references/versions/claude-sonnet-5-5.md) | Speed/intelligence balance for general and coding tasks. |
| Claude Haiku 5.5 (`claude-haiku-5-5`) | [version details](references/versions/claude-haiku-5-5.md) | Latency-sensitive, high-volume classification, extraction, and routing. |
| Claude Fable 5.1 (`claude-fable-5-1`) | [version details](references/versions/claude-fable-5-1.md) | Higher-effort reasoning and long-horizon tasks that justify higher cost. |

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
- [Claude Fable 5.1](references/versions/claude-fable-5-1.md)
- [Anthropic model overview](https://platform.claude.com/docs/en/models/overview)
- [Anthropic model lifecycle](https://platform.claude.com/docs/en/about-claude/model-deprecations)

Fetched: 2026-10-16
