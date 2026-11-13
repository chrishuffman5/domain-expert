# GPT-6 Luna

**Canonical ID:** `gpt-6-luna`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: general.
- Status: current.
- Release date: 2026-09-22.
- Availability: OpenAI API (Responses; Chat Completions function calling only at effort `none`); OpenAI Decisions API (`POST /v1/decisions`; GA 2026-10-22; only supported model); Amazon Bedrock `openai.gpt-6-luna`; Microsoft Foundry (version 2026-09-22, Decisions API support); Google Cloud Vertex AI (private preview).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://developers.openai.com/api/docs/models

## Capabilities and context

- Catalog capabilities: text, image, reasoning, coding, tools, multilingual, vision.
- Context/output limits: 1.05M tokens (922K max input); 128K max output; knowledge cutoff 2026-05-18.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://developers.openai.com/api/docs/models

## Price and availability conditions

$0.10 input / $0.01 cached / $0.125 cache write / $0.50 output per MTok (prompts <=272K); Batch and Flex half; Fast 2x; regional +10%; >272K costs more. Decisions API: output tokens not charged

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/models

## Verified details and changes since the 2026-10-16 snapshot

- Released 2026-09-22 (the snapshot recorded unknown). "Our most efficient model for focused, high-volume tasks."
- Context 1,050,000; max input 922,000; max output 128,000; knowledge cutoff 2026-05-18; text and image in, text out.
- Reasoning effort: none, low, medium (default), high, xhigh, max. Chat Completions function calling only when effort is `none`. EU data residency for Standard, Fast, Flex and Batch.
- Price per MTok: $0.10 input, $0.01 cached, $0.125 cache write, $0.50 output; Batch/Flex half; Fast 2x; regional +10%; prompts over 272K cost more.
- 2026-09-25: image-encoding bug fix affecting gpt-6-sol and gpt-6-luna; rerun image-input evals from before that date.
- Named replacement for gpt-5-nano (shutdown 2026-12-11), gpt-5.4-nano (2027-04-01) and the gpt-4o, gpt-4o-mini, gpt-4.1 and gpt-4.1-mini dated snapshots (2027-01-14).

> Source: https://developers.openai.com/api/docs/models/gpt-6-luna
> Source: https://developers.openai.com/api/docs/changelog
> Source: https://developers.openai.com/api/docs/deprecations

## Decisions API

- Beta 2026-10-06; general availability 2026-10-22. `POST /v1/decisions`; gpt-6-luna is the only supported model; OpenAI describes it as about 10x faster than the Responses API.
- Question types: predicate (probability 0-1), choice (distribution plus confidence), score (probability-weighted level index, 2-10 levels); 1-400 questions per request, each with a unique `name`.
- Inputs: text or a message array including images (base64 data URL or http URL) and input_json; file IDs not supported.
- Pricing: uncached input $0.10/MTok; cache hits discounted; cache writes charged; output tokens are not charged. Shared input cached by default (reusable prefix of at least 1,024 tokens). ZDR and HIPAA for eligible customers.
- Selection boundary: this is a probability-returning decision endpoint on a general model; typed semantic decision families (Jev, Perplexity Decider) remain separate catalog skills.

> Source: https://developers.openai.com/api/docs/guides/decisions
> Source: https://developers.openai.com/api/docs/changelog

## Cloud availability

- Amazon Bedrock: `openai.gpt-6-luna`. Microsoft Foundry: `gpt-6-luna` version 2026-09-22 with Decisions API support. Google Cloud: `gpt-6-luna` private preview.

> Source: https://developers.openai.com/api/docs/models/gpt-6-luna
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

## Adoption evidence

**Signal:** Observed platform usage: OpenRouter ranked GPT-6 Luna 7th in the displayed tokens-processed table with 7.1T tokens and +10%; usage data was through 2026-10-13.

**Scope and caveat:** OpenRouter public-routed traffic, prompt plus completion tokens in UTC buckets. Excludes private traffic and direct/other-router use; tokens are not users, spend, task preference, or quality.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Selection notes

**Catalog strengths:** Cost-efficient focused high-volume tasks; reasoning effort none–max (default medium); Typed predicate/choice/score questions through the Decisions API; Named replacement for gpt-5-nano, gpt-5.4-nano and gpt-4o/gpt-4.1 dated snapshots.

**Catalog limitations:** Not positioned as the top choice for most demanding work.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://developers.openai.com/api/docs/models

## Sources

- https://developers.openai.com/api/docs/models
- https://openrouter.ai/rankings?benchmark=intelligence
- https://developers.openai.com/api/docs/models/gpt-6-luna
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/decisions
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://developers.openai.com/api/docs/deprecations
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

Fetched: 2026-11-13 UTC.
