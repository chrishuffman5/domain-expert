---
name: grok
license: MIT
description: "Select and compare xAI Grok model identities, capabilities, costs, context and lifecycle. WHEN: Grok 4.7 vs Grok Code Fast, xAI model IDs, coding/general Grok fit, current limits or costs. Do NOT use for other model families, xAI API/SDK mechanics, agent harness/tool implementation, cloud or router setup, training, or evaluation infrastructure; use the relevant family skill or existing `ai` plugin."
---

# xAI Grok model selection

This family skill helps identify which selected Grok model fits a workload and what its documented tradeoffs are. It owns model identity, model-level capabilities, selection, price/limit caveats and lifecycle checks. It does not explain how to call the xAI API or wire an agent harness.

## Routing

| Question | Read |
|---|---|
| General xAI flagship, multimodal input, configurable reasoning, broad work | [`grok-4.7`](references/versions/grok-4-7.md) |
| Coding-oriented Grok, alias vs canonical identity, lower listed base rates | [`Grok Code Fast 1 / Grok Build 0.1`](references/versions/grok-build-0-1.md) |
| Current xAI API payloads, auth, SDKs, streaming or function-call execution | Existing `ai` plugin's API/integration guidance and current xAI API docs |
| Agent harness and permissions | Existing `ai` plugin's harness or agent-SDK skill |
| Compare Grok with unrelated model families | `ai-models-specialist` agent, then read each competing family skill |

> Source: https://docs.x.ai/developers/models ; https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Selected model identities

| Canonical identity | Public/API alias | Main fit | Important constraints |
|---|---|---|---|
| `grok-4.7` | none listed | Broad reasoning, coding, agentic and knowledge work | 500K context; over-200K rates; batch unsupported |
| `grok-build-0.1` | `grok-code-fast-1`, `grok-code-fast`, `grok-code-fast-1-0825` | Coding and software-engineering workflows | 256K context; over-200K rates; batch unsupported |

The alias is not another model. Keep `grok-build-0.1` as the canonical identity in a catalog comparison; use the alias required by the particular official API route only after checking the current model list. Do not count aliases, regions or clusters as additional models.

> Source: https://docs.x.ai/developers/models ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Choose by task

- Start with Grok 4.7 if the need includes broad general work, image understanding, tool use or configurable reasoning.
- Start with Grok Code Fast 1 when the work is specifically coding, repository engineering or coding-agent workflow, and a task evaluation supports its fit.
- Use Grok 4.7 when the documented 500K context may be needed; Grok Code Fast is documented at 256K.
- Compare Grok Code Fast's lower listed base rate against Grok 4.7 only after accounting for long-context, cache and output rates.
- Do not choose from model naming alone. “Fast” describes positioning; it does not promise lower latency for every prompt or deployment region.

A practical first-pass choice is:

| Workload condition | First candidate | Check before committing |
|---|---|---|
| General knowledge, mixed tasks or image input | Grok 4.7 | Need for fresh external evidence; 200K pricing threshold |
| Software engineering and code agent | Grok Code Fast 1 | Repository task accuracy and tool-call success |
| Long context above 256K | Grok 4.7 | Long-context rates apply beyond 200K |
| Offline batch processing | Neither by default | Both inspected model pages list batch unsupported |
| Lowest possible cost | Neither by name alone | Compare effective task cost on the chosen region and workload |

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Reasoning, tools and output

Grok 4.7 supports low, medium, high and xhigh reasoning effort, with high listed as the default. The model page describes function calling and structured outputs. Grok Code Fast's page also lists reasoning, function calling and structured outputs. These capabilities do not mean either model has permission to perform an action. The application still needs to validate tool arguments, authorize every operation and handle untrusted model output.

Reasoning effort is a model-level choice; set it based on the complexity and risk of the workload, then measure latency, cost and success on real examples. More reasoning effort is not proof of correctness. For code changes, use tests, review and least-privilege tools rather than treating an accepted function call as a safe result.

Both selected entries accept image input per their inspected model pages and emit text. Neither is an image-generation or video model in this family selection. For real-time information, supply retrieval or another verified source rather than assuming a model's pretrained knowledge is current.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Pricing and context

The quoted rates in each version reference are dated snapshots for the selected region. Grok 4.7's inspected US East rates are $2.00/M input, $0.50/M cached input and $6.00/M output. Grok Code Fast's inspected rate is $1.00/M input, $0.20/M cached input and $2.00/M output. Both model pages state that requests above 200K use a higher-context rate. The higher rate is a material cost boundary; re-open the model-specific rate card rather than extending the base rate to long prompts.

For an estimate, calculate uncached input, cached input and output separately. Include the actual context length and selected region. Check whether agent loops or tool calls multiply model invocations. Batch is unsupported on both inspected pages, so don't include a batch discount in a budget.

Region selectors can change rates, rate limits and availability. The per-model reference includes the captured region facts and source. Confirm current terms before a contract, rollout or price-sensitive migration.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Evidence, unknowns and lifecycle

The inspected xAI catalog does not give comparable model-level usage/download totals for these entries. Adoption is marked unknown. Do not substitute general X audience size, company growth, or model descriptions for API usage evidence.

Grok 4.7's catalog page update date was not treated as its launch date. The inspected sources do not establish a verified Grok 4.7 release date, nor a retirement date for either model. Keep the canonical ID, active status, aliases and current rate conditions attached to their official source and retrieval date. Recheck the catalog before relying on an alias or a lifecycle claim.

> Source: https://docs.x.ai/developers/models ; https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Selection checklist

Before recommending a Grok tier, establish:

1. Whether the task is general or specifically code-focused.
2. Required context length and whether it crosses 200K.
3. Whether image input, tool use, structured outputs or configurable reasoning are needed.
4. Region and account availability, not just the base model ID.
5. Effective cost for uncached input, cached input, output and repeated agent turns.
6. Whether online sources or another freshness mechanism are required.
7. A workload-specific evaluation and a human review path for consequential code or tool actions.

If the user asks how to make an API call, configure a key, stream a response or execute a function call, hand off to the existing `ai` plugin's API/integration material. This skill answers which model and why, not how to operate the endpoint.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Compare effective task cost

Use model-specific, region-specific rates and count all requests in an agent run. For a first comparison, estimate:

- Uncached prompt input.
- Cached input, if the chosen API route supports and reports it.
- Output tokens, including reasoning or intermediate responses if billed as output.
- Number of retries and model turns per user task.
- Tool calls or other separately billed services.
- Context length for the largest request.
- Long-context rate when any request exceeds 200K.

Do not compare the $1/$2 base rates of Grok Code Fast with Grok 4.7's $2/$6 rates while ignoring the total task success rate. A cheaper model that requires many more turns or a stronger reviewer can cost more per successfully completed task. The official pages list separate cached-input rates; use them only for requests actually counted as cached by the service.

No batch discount is available on either selected model in the inspected pages. Region selectors can change model rates, and long-context rows apply above the published threshold. Recheck before producing a budget commitment.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Selection examples

| User requirement | Initial choice | Reason to reconsider |
|---|---|---|
| Multi-purpose assistant that uses image input and tools | Grok 4.7 | Need benchmark or price evidence for this workload |
| Code-writing loop with repository context under 256K | Grok Code Fast | Tool reliability or coding quality fails the eval |
| Prompt likely reaches 300K tokens | Grok 4.7 | Higher-context rate applies after 200K; budget may dominate |
| Need many unattended offline jobs | Neither by default | Batch unsupported on the inspected pages |
| Need a model with verified current web facts | Neither by default | Add retrieval and inspect source citations |
| Need image output or video generation | Neither selected identity | Select a modality-specific family |
| Need an enterprise regional guarantee | No assumption | Confirm supported region, service terms and deployment path |

These are starting points only. The model choice must match the account's region, available features and actual task results.

> Source: https://docs.x.ai/developers/models ; https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Operational risk questions

- Could a prompt or repository context cross the 200K pricing boundary unexpectedly?
- Are image inputs necessary, or can the task work with text-only source material?
- What untrusted instructions can arrive inside repository files, logs or images?
- Which model outputs can trigger tools, file edits, deployments or external messages?
- What validation runs before model-proposed code is applied?
- What tool permissions are minimized and what actions require approval?
- Is current factual information grounded in retrieved sources?
- Can the application detect tool loops, invalid arguments and repeated failures?
- Are API IDs and aliases logged so a later behavior change can be investigated?
- Does the product need a fallback if one region or model alias disappears?

Model selection does not remove injection, authorization or software-quality risks. The existing `ai` plugin owns the detailed harness and security controls.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Facts to recheck before use

Re-open the canonical model page when a user needs a current figure. At minimum verify:

- Exact model name and alias mapping.
- Region and account availability.
- Context window and output limit.
- Current uncached and cached token rates.
- Whether requests above 200K receive higher rates.
- Batch support and rate limits.
- Reasoning effort options and default.
- Release announcement or retirement notice.

A model catalog's page-update timestamp is not a release date. The catalog leaves Grok 4.7 release date unknown because the official page date only established when the page was updated. Grok Code Fast release date is also unknown in the inspected material.

> Source: https://docs.x.ai/developers/models ; https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## What a recommendation should include

A useful response should distinguish identity, fit, constraints and evidence:

- State the canonical ID and any official alias relationship.
- Name the task conditions that favor the selected tier.
- Give context/output/rate information only with source and retrieval date.
- Call out the 200K higher-context price boundary.
- Include cached input and output as different price components.
- Name the selected region when quoting rates or limits.
- State batch support accurately; both current pages say unsupported.
- Mark release date and model-level adoption unknown where the official source is silent.
- Explain that tool use still needs application-level authorization.
- Identify one evaluation that could overturn the recommendation.

Do not call one model categorically better. Phrase the choice conditionally: “For a coding workload, start with Code Fast if it meets the task accuracy target; for broader mixed work or larger context, test Grok 4.7.”

When estimating cost, count cached and uncached input separately and apply the high-context rate whenever the request crosses the documented 200K threshold. Include the expected output length; a low input rate does not imply low total cost.

Keep alias logging separate from identity reporting: record which API alias was requested and the canonical identity to which the official page maps it. This makes behavior changes easier to investigate if alias mappings change.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

> Source: https://docs.x.ai/developers/models ; https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Evaluate coding fit before adoption

For Code Fast, build a repository-task set that includes edits, tests, debugging, shell use and cases where the correct action is to stop and ask for missing context. Measure whether proposed patches pass the project's tests and whether the model preserves unrelated behavior.

Run the same tasks with and without representative repository context. This shows whether the narrower coding identity's cost and latency are useful relative to Grok 4.7's broader context window. Include prompts near the 200K pricing boundary, because long repositories can change the cost profile.

Count tool-call failures and unsafe proposed actions as quality failures. Neither coding specialization nor function-call support removes the need for the caller to validate diffs and control tool permissions.

> Source: https://docs.x.ai/developers/models/grok-code-fast-1 ; https://docs.x.ai/developers/models/grok-4.7 (inspected 2026-10-16)

## Sources

- https://docs.x.ai/developers/models
- https://docs.x.ai/developers/models/grok-4.7
- https://docs.x.ai/developers/models/grok-code-fast-1

Fetched: 2026-10-16
