# GPT-6.1 Terra

**Canonical ID:** `gpt-6.1-terra`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: general.
- Status: current.
- Release date: 2026-10-26.
- Availability: OpenAI API (Chat Completions, Responses, Batch; not Realtime, fine-tuning or embeddings); Amazon Bedrock `openai.gpt-6.1-terra`; Microsoft Foundry (version 2026-10-26); Google Cloud Vertex AI (private preview).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra

## Capabilities and context

- Catalog capabilities: text, image, reasoning, coding, tools, vision, computer use, writing.
- Context/output limits: 1.05M tokens (922K max input); 128K max output; knowledge cutoff 2026-06-01.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra

## Price and availability conditions

$1 input / $0.05 cached / $1.25 cache write (30 min) or $2.50 (12 h) / $5 output per MTok (prompts <=272K); >272K: 2x input and cache, 1.5x output; Batch and Flex 50%; Fast 2x; regional +10%

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra

## Identity and lifecycle

- Released 2026-10-26: "New model gpt-6.1-terra for visual reasoning, computer use, and writing." Only snapshot is the default id.
- "A fast, efficient model for visual reasoning, precise computer use, and clear, natural writing."
- Context 1,050,000; max input 922,000; max output 128,000; knowledge cutoff 2026-06-01; text and image in, text out.
- Reasoning effort: none, low, medium (default), high, xhigh, max.
- Endpoints: Chat Completions, Responses, Batch; not Realtime, fine-tuning or embeddings. Responses tools include web and file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP and tool search.
- Standard rate limits: Build 5,000 RPM / 1M TPM; Launch 10,000 / 4M; Grow 15,000 / 40M.
- Named replacement for gpt-5-mini, which shuts down 2026-12-11.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra
> Source: https://developers.openai.com/api/docs/changelog
> Source: https://developers.openai.com/api/docs/deprecations

## Cloud availability

- Amazon Bedrock: `openai.gpt-6.1-terra`. Microsoft Foundry: `gpt-6.1-terra` version 2026-10-26. Google Cloud Vertex AI: `gpt-6.1-terra` private preview.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra

## Selection notes

**Catalog strengths:** Fast, efficient model for visual reasoning, precise computer use and clear, natural writing; reasoning effort none–max (default medium); Named replacement for gpt-5-mini (shutdown 2026-12-11).

**Catalog limitations:** List price sits between gpt-6.1-sol ($2/$10) and gpt-6-luna ($0.10/$0.50); no provider positioning statement was captured; No Realtime, fine-tuning or embeddings endpoint.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-terra

## Sources

- https://developers.openai.com/api/docs/models/gpt-6.1-terra
- https://developers.openai.com/api/docs/changelog
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai
- https://developers.openai.com/api/docs/deprecations

Fetched: 2026-11-13 UTC.
