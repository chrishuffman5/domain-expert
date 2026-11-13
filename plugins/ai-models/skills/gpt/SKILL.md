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
| Hardest current reasoning or coding | [GPT-6 Astra](references/versions/gpt-6-astra.md) | Most capable OpenAI model for demanding work | Premium: $10/$50 per MTok, 2x/1.5x over 272K |
| Strong capability at lower cost | [GPT-6.1 Sol](references/versions/gpt-6-1-sol.md) | Near-Astra performance at $2/$10; replacement for gpt-5, gpt-5-pro, o3, o3-pro | No `none` effort; evaluate actual task quality against Astra |
| Visual reasoning, computer use, natural writing at mid cost | [GPT-6.1 Terra](references/versions/gpt-6-1-terra.md) | Newest tier (2026-10-26) at $1/$5; replacement for gpt-5-mini | No Realtime, fine-tuning or embeddings endpoint |
| High-volume, cost-sensitive tasks | [GPT-6 Luna](references/versions/gpt-6-luna.md) | Lowest listed GPT-6 rate ($0.10/$0.50); only model on the Decisions API | Router usage data is scoped and does not prove global preference |
| Existing workload validated on the first GPT-6 Sol | [GPT-6 Sol](references/versions/gpt-6-sol.md) | Coding/agentic tier; replacement for gpt-5.1 and gpt-5.3-codex; supports `none` effort | Superseded by 6.1 Sol at the same base rate |
| GPT-5.6 balance tier or compatible deployment | [GPT-5.6 Terra](references/versions/gpt-5-6-terra.md) | Balanced everyday-work tier within the GPT-5.6 family | Costs more than 6.1 Terra ($2/$12 vs $1/$5); no deprecation yet |
| Lower-cost GPT-5.6 tasks | [GPT-5.6 Luna](references/versions/gpt-5-6-luna.md) | Most cost-efficient GPT-5.6 tier by family positioning | Older generation; costs more than GPT-6 Luna |
| GPT-5.6 flagship capability | [GPT-5.6 Sol](references/versions/gpt-5-6-sol.md) | GPT-5.6 flagship for complex coding, research, and knowledge work | Promotional $4/$20 ends 2026-11-30 |
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

A release post’s launch price can become stale after price changes. The 2026-11-13 references carry current pricing-page rates; GPT-5.6 Sol is on a promotional $4/$20 that the pricing and model pages say ends 2026-11-30 (the August changelog said "at least through November 21").

Price modifiers that change model choice (OpenAI pricing page, 2026-11-13):

- Prompts over 272K tokens bill the whole request at a higher rate; for GPT-6 models this is 2x input and cache, 1.5x output.
- Batch about 50% off; Flex near Batch; Fast about 2x; Ultrafast about 6x Standard, offered for gpt-6-astra (US data residency only) and gpt-6.1-sol (Responses API).
- 12-hour prompt cache writes cost 2.5x the input price (since 2026-10-20).
- Models released on or after 2026-03-05 carry a 10% regional / FedRAMP uplift.
- Usage tiers are now Build, Launch, and Grow (since 2026-10-06); rate limits differ by tier.

## Match the reasoning tier

Use the least expensive candidate that clears the quality bar on representative examples.

For difficult work, compare the current flagship with a lower-priced tier and record which errors differ.

For routine extraction or rewriting, test whether a smaller or cheaper tier reaches the same acceptance threshold.

Separate task reasoning from answer length. A concise output can require substantial internal reasoning; a long output can be mostly formatting.

Models may expose different reasoning controls. Do not assume all controls or values are shared across GPT generations. GPT-6 Astra and GPT-6.1 Sol accept effort low through max but not `none`; GPT-6 Sol, GPT-6.1 Terra, and GPT-6 Luna accept `none` through max with `medium` as default. Astra also rejects custom temperature/top_p and logprobs.

Check the exact model reference and current provider documentation for reasoning options before designing a workflow.

Use explicit acceptance criteria such as field correctness, code tests, citation coverage, or policy adherence.

Recheck ambiguous or high-impact outputs with a separate process suited to the domain.

## Context and multimodal inputs

A large advertised context window is a maximum, not a guarantee of perfect use of every token.

Include relevant context only. Very large prompts increase cost and can bury important instructions or evidence.

Test retrieval from different positions in a long document and across multiple related documents.

Check whether the chosen API identity accepts the exact input modality needed.

The GPT-6 catalog lists text and image input, text output, a 1.05M context (922K max input), and 128K max output for all five GPT-6 candidates. Knowledge cutoffs differ: Astra and 6.1 Sol 2026-04-30, 6 Sol 2026-04-20, Luna 2026-05-18, 6.1 Terra 2026-06-01.

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

GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Sol, and GPT-6 Luna are distinct current API identities. GPT-6 Sol is not an alias of GPT-6.1 Sol.

GPT-6 Astra's release date conflicts by source: the OpenAI changelog says 2026-09-29, Microsoft Foundry lists version 2026-09-03. The catalog uses the first-party date.

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

## Decisions API with GPT-6 Luna
> Source: https://developers.openai.com/api/docs/guides/decisions

The Decisions API (`POST /v1/decisions`) entered beta on 2026-10-06 and reached general availability on 2026-10-22. GPT-6 Luna is the only supported model. It answers predicate (probability), choice (distribution plus confidence), and score (probability-weighted level) questions, 1 to 400 per request, and does not charge output tokens. Choose it when a workload needs probabilities from a general model at Luna cost.

It is not a typed semantic decision model. Compare Jev or Perplexity Decider through their family skills when the requirement is typed decisions or structured decision probabilities from a dedicated decision model.

## Specialist and limited-access OpenAI models
> Source: https://developers.openai.com/api/docs/changelog

These models have no catalog rows: they are restricted, or they serve a modality other than general text reasoning. Mention them only when the requester's workload and access fit.

- **Cyber (trusted access):** `gpt-6-cyber` (2026-11-05) needs Daybreak Red access and approval; 1.05M context, 128K output; $20 input / $2 cached / $25 cache write / $100 output per MTok up to 272K ($40/$4/$150 above). Earlier: `gpt-5.6-cyber`, `gpt-daybreak-blue-latest` and `gpt-daybreak-red-latest` (2026-08-07; red needs separate approval). `gpt-5.5-cyber-preview` shuts down 2027-02-01; `gpt-5.4-cyber` shut down 2026-10-01.
- **Life sciences (trusted access):** `gpt-6-rosalind` (changelog 2026-10-30) at $15 / $1.50 cached / $75; `gpt-rosalind-research` (GA 2026-09-08, billed from 2026-10-05) and `gpt-rosalind-discovery` (release date not found) at $5 / $0.50 / $25. Per-model pages return 404; the models index shows one GPT-Rosalind entry.
- **Image generation:** `gpt-image-2.6-sunburst` (detailed visual work) and `gpt-image-2.6-flare` (interactive, fast) from 2026-11-04 add adjustable complexity, SVG and animated GIF output; text input $5 (cached $1.25), image input $8 (cached $2), image output $30 per MTok; images endpoints only. `gpt-image-2.5-sunburst` and `-flare` shipped 2026-09-08. `gpt-image-2` and `gpt-image-2-2026-04-21` shut down 2027-02-10 (replacement: the 2.6 models). Azure lists image models through 2.5.
- **Voice and realtime:** `gpt-live-1` (GA 2026-09-10) is a full-duplex voice model at $0.05 per minute on `v1/live/sessions`. `gpt-realtime-2.1` costs audio $32/$64, text $4/$24, image input $5 per MTok; `gpt-realtime-2.1-mini` audio $10/$20, text $0.60/$2.40; `gpt-realtime-2`, `gpt-realtime-translate`, and `gpt-realtime-1.5` are also listed.
- **Transcription:** `gpt-transcribe` $0.0045 per minute; `gpt-live-transcribe` and `gpt-realtime-whisper` $0.017 per minute. Release dates were not stated.

> Source: https://developers.openai.com/api/docs/pricing.md
> Source: https://developers.openai.com/api/docs/models/gpt-6-cyber
> Source: https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst
> Source: https://developers.openai.com/api/docs/models/gpt-live-1

## Deprecations and shutdowns
> Source: https://developers.openai.com/api/docs/deprecations

OpenAI's notice policy is at least 6 months for GA models, 3 months for specialised variants, and about 2 weeks for previews. None of the cataloged GPT-5.4, GPT-5.5, GPT-5.6, or GPT-6 models has a deprecation row as of 2026-11-13.

| Shutdown | Models | Replacement |
|---|---|---|
| 2026-10-23 (notice 2026-04-22) | gpt-3.5-turbo, gpt-4, gpt-4-turbo, gpt-4-1106-preview, gpt-4.1-nano, gpt-4o-2024-05-13, o1, o1-pro, o3-mini | gpt-5.6-terra / -sol / -luna. The date has passed; the page files these under "Past deprecations" without a post-shutdown confirmation |
| 2026-12-11 (notice 2026-06-11) | gpt-5, gpt-5-pro, o3, o3-pro | gpt-6.1-sol (previously gpt-5.6-sol) |
| 2026-12-11 | gpt-5-mini | gpt-6.1-terra |
| 2026-12-11 | gpt-5-nano | gpt-6-luna |
| 2027-01-14 | gpt-4o, gpt-4o-mini, gpt-4.1, gpt-4.1-mini dated snapshots | gpt-6-luna |
| 2027-04-01 | gpt-5.1, gpt-5.3-codex | gpt-6-sol |
| 2027-04-01 | gpt-5.4-nano | gpt-6-luna |
| 2027-01-06 / 01-20 / 02-26 | tts-1, tts-1-hd, gpt-4o-mini-tts (to gpt-realtime-2.1-mini); older realtime/audio models; whisper-1 and gpt-4o transcribe models | See the specialist section |

The Assistants API shut down on 2026-08-26.

## Cloud availability
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure

| Model | Amazon Bedrock | Microsoft Foundry | Google Cloud Vertex AI |
|---|---|---|---|
| gpt-6-astra | Not established | Version 2026-09-03 | Private preview |
| gpt-6.1-sol | `openai.gpt-6.1-sol` (`global.` / `us.` profiles) | GA, version 2026-09-29 | Private preview |
| gpt-6.1-terra | `openai.gpt-6.1-terra` | Version 2026-10-26 | Private preview |
| gpt-6-luna | `openai.gpt-6-luna` | Version 2026-09-22, Decisions API | Private preview |
| gpt-6-sol | `openai.gpt-6-sol` | Version 2026-09-22 | Not listed |
| gpt-5.6-sol / terra / luna | `openai.gpt-5.6-sol`; Terra and Luna not established | Version 2026-07-09 | Not listed |

Bedrock bills gpt-6.1-sol at $2/$10 for Standard Global, +10% for US or in-Region, and $12/$60 for Ultrafast Global; it follows OpenAI's 6-month GA deprecation notice. Vertex AI access is through the Google account team. Cloud model availability, prices, and lifecycle can differ from the OpenAI API; endpoint configuration belongs to `ai`.

> Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

## When to choose something else

Choose an OpenAI open-weight model when local deployment or weight access is a requirement; see `gpt-oss`.

Choose a specialist model when the task is not general language reasoning, such as tabular prediction or typed semantic decisions. For OpenAI image, voice, transcription, cyber, or life-sciences models, use the specialist section above; they are not interchangeable with the GPT text tiers.

Use the `ai` skill for API mechanics, SDKs, harnesses, eval infrastructure, and inference routing.

Use ChatGPT product help for subscription access and model-picker behavior.

## Sources

- OpenAI API model catalog: https://developers.openai.com/api/docs/models
- OpenAI all-models index: https://developers.openai.com/api/docs/models/all
- OpenAI changelog: https://developers.openai.com/api/docs/changelog
- OpenAI deprecations: https://developers.openai.com/api/docs/deprecations
- OpenAI pricing: https://developers.openai.com/api/docs/pricing.md
- GPT-6 Astra: https://developers.openai.com/api/docs/models/gpt-6-astra
- GPT-6.1 Sol: https://developers.openai.com/api/docs/models/gpt-6.1-sol
- GPT-6.1 Terra: https://developers.openai.com/api/docs/models/gpt-6.1-terra
- GPT-6 Sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- GPT-6 Luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- Decisions API: https://developers.openai.com/api/docs/guides/decisions
- GPT-6 Cyber: https://developers.openai.com/api/docs/models/gpt-6-cyber
- GPT Image 2.6: https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst and https://developers.openai.com/api/docs/models/gpt-image-2.6-flare
- GPT Live 1: https://developers.openai.com/api/docs/models/gpt-live-1
- GPT Transcribe: https://developers.openai.com/api/docs/models/gpt-transcribe
- Microsoft Foundry models sold by Azure: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- Amazon Bedrock GPT-6.1 Sol card: https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html
- Google Cloud OpenAI partner models: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai
- GPT-5.6: https://openai.com/index/gpt-5-6/
- GPT-5.5: https://openai.com/index/introducing-gpt-5-5/
- GPT-5.4: https://openai.com/index/introducing-gpt-5-4/
- GPT-5.1: https://openai.com/index/gpt-5-1-for-developers/
- OpenRouter rankings: https://openrouter.ai/rankings?benchmark=intelligence

Fetched: 2026-11-13 UTC.
