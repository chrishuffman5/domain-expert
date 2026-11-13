# GPT-6 Astra

**Canonical ID:** `gpt-6-astra`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: frontier.
- Status: current.
- Release date: 2026-09-29 (OpenAI changelog; Microsoft Foundry lists model version 2026-09-03).
- Availability: OpenAI API (tool calling requires the Responses API); Microsoft Foundry (model version 2026-09-03); Google Cloud Vertex AI (private preview).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://developers.openai.com/api/docs/models/gpt-6-astra

## Capabilities and context

- Catalog capabilities: text, image, reasoning, coding, tools, multilingual, vision.
- Context/output limits: 1.05M tokens (922K max input); 128K max output; knowledge cutoff 2026-04-30.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://developers.openai.com/api/docs/models/gpt-6-astra

## Price and availability conditions

$10 input / $1 cached / $12.50 cache write / $50 output per MTok (prompts <=272K); >272K: 2x input and cache, 1.5x output ($20/$75); Batch and Flex 50%; Fast 2x ($20/$100); Ultrafast about 6x Standard (US data residency only)

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/pricing

## Verified details and changes since the 2026-10-16 snapshot

- Release date: OpenAI changelog says "New model gpt-6-astra released" on 2026-09-29; the Microsoft Foundry catalog lists model version 2026-09-03. The OpenAI model page states no date. This catalog uses the first-party date and keeps the conflict visible. The snapshot recorded unknown.
- Only snapshot is the default id. Context 1,050,000; max input 922,000; max output 128,000; knowledge cutoff 2026-04-30; text and image in, text out.
- Reasoning effort: low, medium, high, xhigh, max (no `none`). No custom temperature/top_p, no logprobs; tool calling needs the Responses API.
- Price per MTok: $10 input, $1 cached, $12.50 cache write, $50 output; prompts over 272K bill 2x input/cache and 1.5x output for the full request ($20/$75). Batch $5/$25; Fast $20/$100.
- 2026-09-29: Ultrafast mode for gpt-6-astra (US data residency only), about 6x Standard; not listed on the model page.

> Source: https://developers.openai.com/api/docs/models/gpt-6-astra
> Source: https://developers.openai.com/api/docs/changelog
> Source: https://developers.openai.com/api/docs/pricing
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure

## Cloud availability

- Microsoft Foundry: `gpt-6-astra`, version 2026-09-03.
- Google Cloud Vertex AI: private preview only (global and `us` multi-region endpoints; access via account team).
- Amazon Bedrock: not established in the inspected sources (OpenAI's Bedrock id list does not include Astra).

> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://developers.openai.com/api/docs/models

## Selection notes

**Catalog strengths:** Most capable model for demanding work; reasoning effort low–max (no `none`).

**Catalog limitations:** Premium-priced; avoid for routine high-volume work; No `none` effort, custom temperature/top_p or logprobs; Release date conflict: OpenAI changelog 2026-09-29 vs Azure version 2026-09-03; the first-party date is used.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://developers.openai.com/api/docs/models/gpt-6-astra

## Sources

- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/pricing
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai
- https://developers.openai.com/api/docs/models

Fetched: 2026-11-13 UTC.
