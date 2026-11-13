# GPT-5.6 Luna

**Canonical ID:** `gpt-5.6-luna`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: general.
- Status: current/api GA.
- Release date: 2026-07-09.
- Availability: OpenAI API / Codex (listed under More models); Microsoft Foundry (version 2026-07-09).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://openai.com/index/gpt-5-6/

## Capabilities and context

- Catalog capabilities: text, reasoning, coding, tool use.
- Context/output limits: 1M context window per family launch page.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://openai.com/index/gpt-5-6/

## Price and availability conditions

$0.20 input / $0.02 cached / $1.20 output per MTok (Standard, prompts <=272K)

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/pricing.md

## Verified details as of 2026-11-13

- Standard price per MTok (prompts up to 272K): $0.20 input, $0.02 cached, $1.20 output.
- Listed under "More models" on the OpenAI models index; no deprecation row.
- Microsoft Foundry: version 2026-07-09.
- Context, cutoff and model-page details were not re-fetched in this pass; the 1M figure comes from the family launch page.

> Source: https://developers.openai.com/api/docs/pricing.md
> Source: https://developers.openai.com/api/docs/models/all
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure

## Adoption evidence

**Signal:** Observed platform usage: OpenRouter ranked GPT-5.6 Luna 7th in the 30-day tokens-processed table with 25T tokens and -45%; newest bucket shown was 2026-10-13.

**Scope and caveat:** OpenRouter public-routed traffic, prompt plus completion tokens in UTC buckets. Excludes private traffic and direct/other-router use; tokens are not users, spend, task preference, or quality.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Selection notes

**Catalog strengths:** Most cost-efficient GPT-5.6 tier.

**Catalog limitations:** Positioned for efficiency; no deprecation listed as of 2026-11-13; Costs more than gpt-6-luna ($0.10/$0.50).

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://openai.com/index/gpt-5-6/

## Sources

- https://openai.com/index/gpt-5-6/
- https://openrouter.ai/rankings?benchmark=intelligence
- https://developers.openai.com/api/docs/pricing.md
- https://developers.openai.com/api/docs/models/all
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure

Fetched: 2026-11-13 UTC.
