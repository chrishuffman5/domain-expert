---
name: gpt
license: MIT
description: Select among OpenAI GPT API models by reasoning demand, latency, context, modality, price, and documented availability. Use when a user asks which OpenAI hosted GPT model or tier fits a workload. Do NOT use for API or SDK mechanics, harnesses, eval infrastructure, or inference routing; use ai. Do NOT use for OpenAI downloadable open-weight models; use gpt-oss. Do NOT use for ChatGPT subscription or model-picker questions.
---

# OpenAI GPT model selection

This skill helps choose a hosted OpenAI GPT model for a concrete task. It covers model identity, tier differences, capabilities, selection tradeoffs, and evidence limits. It does not specify how to call an API or build an agent harness.

## Start with the workload

Name the task before naming a model. Separate the required answer quality from optional complexity.

Ask what a correct result looks like and how errors will be found.

Decide whether the model must reason over images, long text, code, or tools.

Estimate typical and worst-case context size, output length, and request frequency.

State the latency, cost, data, and availability constraints.

Use a representative sample to compare candidates when the decision matters.

Do not use broad benchmark rank as a substitute for testing the user’s workload.

## Routing table

| Need | Start with | Why | Main tradeoff |
|---|---|---|---|
| Hardest current reasoning or coding | [GPT-6 Astra](references/versions/gpt-6-astra.md) | Catalog positions it as the most capable choice for demanding work | Premium tier; current price is not stated in the catalog snapshot |
| Strong capability at lower cost | [GPT-6.1 Sol](references/versions/gpt-6-1-sol.md) | Catalog describes near-Astra performance with a lower cost | Still more expensive than Luna; evaluate actual task quality |
| High-volume, cost-sensitive tasks | [GPT-6 Luna](references/versions/gpt-6-luna.md) | Catalog positions it for focused high-volume use and documents the lowest listed GPT-6 rate here | Router usage data is scoped and does not prove global preference |
| GPT-5.6 balance tier or compatible deployment | [GPT-5.6 Terra](references/versions/gpt-5-6-terra.md) | Balanced everyday-work tier within the GPT-5.6 family | Current exact rates and endpoint lifecycle need rechecking |
| Lower-cost GPT-5.6 tasks | [GPT-5.6 Luna](references/versions/gpt-5-6-luna.md) | Most cost-efficient GPT-5.6 tier by family positioning | Older generation; price changed after launch |
| GPT-5.6 flagship capability | [GPT-5.6 Sol](references/versions/gpt-5-6-sol.md) | GPT-5.6 flagship for complex coding, research, and knowledge work | Current price is affected by dated updates |
| Current agentic coding and knowledge work | [GPT-5.5](references/versions/gpt-5-5.md) | Release page emphasizes coding, research, data analysis, documents, and tools | Validate cost and current status before new deployment |
| Hard tasks where added performance is worth high price | [GPT-5.5 Pro](references/versions/gpt-5-5-pro.md) | Pro tier is described for higher-accuracy work | Very high token price; compare against standard model |
| Earlier mainline reasoning and professional tasks | [GPT-5.4](references/versions/gpt-5-4.md) | API release combines reasoning and coding capability | Do not treat Codex experimental context as standard API context |
| Older high-accuracy GPT-5 option | [GPT-5.4 Pro](references/versions/gpt-5-4-pro.md) | Pro tier targets maximum performance on complex tasks | High price and unspecified context in the catalog |

The table narrows candidates. The exact model reference documents identity, catalog facts, availability and sources. A suggested starting point is not a guarantee of best quality or lowest total cost.

## Compare cost and quality together

A per-token rate does not equal total task cost. Reasoning length, retries, input size, cached input, output budget, tools, and service tier can change the bill.

Use the provider’s current pricing page for rates. The reference files preserve snapshot prices or mark them unknown where the catalog did not supply a current figure.

Estimate spend from the expected input and output distribution. Include long-context examples rather than multiplying a short prompt estimate.

Compare quality at a fixed budget as well as at a fixed task completion threshold.

If a lower-cost tier needs many more tokens, tool calls, or retries, its apparent rate advantage may not survive a full workflow comparison.

If a higher tier reduces costly human review or failure recovery, measure that difference explicitly instead of assuming it.

Do not infer a model’s latency from price or from a different family tier.

A release post’s launch price can become stale after price changes. GPT-5.6 references deliberately distinguish changed launch prices from current unknown rates.

## Match the reasoning tier

Use the least expensive candidate that clears the quality bar on representative examples.

For difficult work, compare the current flagship with a lower-priced tier and record which errors differ.

For routine extraction or rewriting, test whether a smaller or cheaper tier reaches the same acceptance threshold.

Separate task reasoning from answer length. A concise output can require substantial internal reasoning; a long output can be mostly formatting.

Models may expose different reasoning controls. Do not assume all controls or values are shared across GPT generations.

Check the exact model reference and current provider documentation for reasoning options before designing a workflow.

Use explicit acceptance criteria such as field correctness, code tests, citation coverage, or policy adherence.

Recheck ambiguous or high-impact outputs with a separate process suited to the domain.

## Context and multimodal inputs

A large advertised context window is a maximum, not a guarantee of perfect use of every token.

Include relevant context only. Very large prompts increase cost and can bury important instructions or evidence.

Test retrieval from different positions in a long document and across multiple related documents.

Check whether the chosen API identity accepts the exact input modality needed.

The GPT-6 catalog lists text and image input and vision capability for the three current GPT-6 candidates.

Do not transfer that fact to every GPT-5 tier without a matching source.

GPT-5.5 release materials describe image, reasoning, coding, research, tool use, and computer use capabilities.

GPT-5.4’s 1M context note applies to an experimental Codex configuration; its standard context is listed as 272K in the catalog.

A ChatGPT interface may expose an ability that does not exist under the same name or behavior in the API.

Treat model IDs and product labels as separate concepts.

## Tools and agents

A model’s ability to use tools does not supply the tools or safety policy.

Keep permissions, side-effect controls, data boundaries, and action validation in the application.

GPT-5.1 introduced apply_patch and shell tool support in the Responses API, but this is a generation-specific documented feature.

GPT-5.4 and GPT-5.5 release materials describe stronger tool and computer-use performance, but those statements do not define a complete safe agent design.

For tool-using work, measure whether the model selects the right tool, supplies correct arguments, handles errors, and knows when to stop.

Test parallel and sequential tool tasks separately.

Inspect the model’s intermediate actions before allowing consequential operations.

Use human approval for actions whose risk warrants it.

Do not give a model broader permissions than the user’s task requires.

## Make comparisons that answer a decision

Keep a small candidate set: one high-capability model, one lower-cost model, and an existing baseline.

Use the same input examples and scoring rules for each model.

Include examples where the model should abstain or ask a question.

Record the output quality and the effort needed to repair failures.

Track prompt tokens, generated tokens, and any separately billed tool activity.

Measure end-to-end completion time in the actual application context.

Separate a model failure from a missing tool, bad source data, or unclear instruction.

Repeat the comparison when a provider changes a model alias or documents a new snapshot.

Avoid changing model and prompt design in the same experiment when you need to know which change mattered.

Choose a clear migration threshold before comparing results.

A small quality gain may not justify a large cost increase for routine tasks.

A small failure-rate reduction may justify extra cost when errors are expensive.

Do not treat internal benchmark scores as a prediction of a private workload.

## Model identity and lifecycle

Use the exact canonical API ID in the version reference.

Do not treat names such as “Thinking,” “Pro,” or “Codex” as interchangeable API endpoints.

A family can contain different generations and performance tiers that are not aliases.

GPT-5.5 Pro and GPT-5.5 are distinct catalog model identities.

GPT-5.4 Pro and GPT-5.4 are distinct catalog model identities.

GPT-5.6 Sol, Terra, and Luna have separate tier identities within one family.

GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna are distinct current API identities.

Check status, region access, project eligibility, price and deprecation before a production migration.

Pin a dated model version when reproducibility is required and the provider offers one.

Revalidate prompts and tool behavior when moving to a new generation.

Do not assume a new tier preserves refusal patterns, output style, or token use.

## Adoption evidence

The catalog contains observed OpenRouter prompt-plus-completion token traffic for GPT-6 Luna and GPT-5.6 Luna. These counts describe OpenRouter-routed public traffic in a specific window.

They exclude direct provider use, private router requests, and other platforms. They are not counts of users, spend, task preference, or quality.

Other GPT entries keep adoption unknown when no comparable model-specific public usage signal was established.

Unknown is not evidence of low usage.

Provider availability and release prominence are not usage measurements.

Use adoption evidence to understand coverage, not to select a model without considering the task.

## When to choose something else

Choose an OpenAI open-weight model when local deployment or weight access is a requirement; see `gpt-oss`.

Choose a specialist model when the task is not general language reasoning, such as tabular prediction or typed semantic decisions.

Use the `ai` skill for API mechanics, SDKs, harnesses, eval infrastructure, and inference routing.

Use ChatGPT product help for subscription access and model-picker behavior.

## Sources

- OpenAI API model catalog: https://developers.openai.com/api/docs/models
- GPT-5.6: https://openai.com/index/gpt-5-6/
- GPT-5.5: https://openai.com/index/introducing-gpt-5-5/
- GPT-5.4: https://openai.com/index/introducing-gpt-5-4/
- GPT-5.1: https://openai.com/index/gpt-5-1-for-developers/
- OpenRouter rankings: https://openrouter.ai/rankings?benchmark=intelligence

Fetched: 2026-10-16 UTC.
