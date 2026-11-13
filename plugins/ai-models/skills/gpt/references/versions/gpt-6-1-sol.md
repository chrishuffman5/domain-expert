# GPT-6.1 Sol

**Canonical ID:** `gpt-6.1-sol`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: frontier.
- Status: current.
- Release date: 2026-09-29.
- Availability: OpenAI API (Chat Completions, Responses, Batch; tool calling requires Responses); Amazon Bedrock `openai.gpt-6.1-sol` (`global.` / `us.` profiles; Standard Global $2/$10, US and in-Region +10%); Microsoft Foundry (GA, version 2026-09-29); Google Cloud Vertex AI (private preview).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-sol

## Capabilities and context

- Catalog capabilities: text, image, reasoning, coding, tools, multilingual, vision.
- Context/output limits: 1.05M tokens (922K max input); 128K max output; knowledge cutoff 2026-04-30.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-sol

## Price and availability conditions

$2 input / $0.10 cached / $2.50 cache write / $10 output per MTok (prompts <=272K); >272K: 2x input and cache, 1.5x output; Batch and Flex 50%; Fast 2x; Ultrafast 6x Standard (Bedrock Global Ultrafast $12/$60)

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-sol

## Verified details and changes since the 2026-10-16 snapshot

- Released 2026-09-29 (the snapshot recorded unknown). Single snapshot. "Near-Astra performance for complex work at a lower cost."
- Context 1,050,000; max input 922,000; max output 128,000; knowledge cutoff 2026-04-30; text and image in, text out.
- Reasoning effort: low, medium (default), high, xhigh, max (no `none`). Endpoints: Chat Completions, Responses, Batch; tool calling needs Responses.
- Price per MTok: $2 input, $0.10 cached, $2.50 cache write, $10 output; over 272K 2x input/cache and 1.5x output; Batch/Flex -50%; Fast 2x.
- 2026-10-08: Ultrafast mode in the Responses API, priced separately (6x Standard; OpenAI gives no absolute figure, Bedrock lists Global Ultrafast $12/$60).
- 2026-10-20: 12-hour prompt cache writes cost 2.5x the input price.
- Named replacement for gpt-5, gpt-5-pro, o3 and o3-pro, which shut down 2026-12-11 (the earlier replacement was gpt-5.6-sol).

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-sol
> Source: https://developers.openai.com/api/docs/changelog
> Source: https://developers.openai.com/api/docs/deprecations

## Cloud availability

- Amazon Bedrock: `openai.gpt-6.1-sol`, launched 2026-09-29, Active, EOL not announced; follows OpenAI's 6-month GA deprecation notice. Context 1M, max output 131,072. Geo profile `us.openai.gpt-6.1-sol`, global `global.openai.gpt-6.1-sol`; bedrock-mantle in-Region only in us-east-1. Standard Global $2/$10; US CRIS and in-Region +10% ($2.20/$11). Priority, Flex and Reserved not supported.
- Microsoft Foundry: `gpt-6.1-sol` version 2026-09-29, GA, Chat and Responses, 1050K context, 128K output; pay-as-you-go and reserved PTU.
- Google Cloud Vertex AI: private preview only.

> Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html
> Source: https://ai.azure.com/catalog/models/gpt-6.1-sol
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://developers.openai.com/api/docs/models

## Selection notes

**Catalog strengths:** Near-Astra performance at lower cost; reasoning effort low–max (no `none`); Named replacement for gpt-5, gpt-5-pro, o3 and o3-pro (shutdown 2026-12-11).

**Catalog limitations:** Costs more than Luna; no independent comparative adoption data.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://developers.openai.com/api/docs/models/gpt-6.1-sol

## Sources

- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/changelog
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html
- https://ai.azure.com/catalog/models/gpt-6.1-sol
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/deprecations

Fetched: 2026-11-13 UTC.
