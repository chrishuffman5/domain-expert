# GPT-5.6 Sol

**Canonical ID:** `gpt-5.6-sol`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: frontier.
- Status: current/api GA.
- Release date: 2026-07-09.
- Availability: OpenAI API / Codex (alias `gpt-5.6`); Amazon Bedrock `openai.gpt-5.6-sol`; Microsoft Foundry (version 2026-07-09).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://openai.com/index/gpt-5-6/

## Capabilities and context

- Catalog capabilities: text, reasoning, coding, tool use, professional work, science.
- Context/output limits: 1.05M context (922K max input); 128K max output; knowledge cutoff 2026-02-16.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://openai.com/index/gpt-5-6/

## Price and availability conditions

Promotional $4 input / $0.40 cached / $20 output per MTok through 2026-11-30 per the pricing and model pages (the 2026-08-21 changelog said 'at least through November 21, 2026'); launch price $5/$0.50/$30

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/pricing.md

## Verified details and changes since the 2026-10-16 snapshot

- Alias `gpt-5.6`. Context 1.05M; max input 922K; max output 128K; knowledge cutoff 2026-02-16.
- Promotional price $4 input / $0.40 cached / $20 output per MTok (launch: $5/$0.50/$30). The pricing page and model page both say the promotion runs through 2026-11-30; the 2026-08-21 changelog entry said "at least through November 21, 2026". The two current primary pages agree on 2026-11-30.
- 2026-08-13: Ultrafast announced for gpt-5.6-sol (limited preview). 2026-08-05: fast mode for prompts over 272K on gpt-5.6-sol, -terra and -luna.
- No deprecation row. The OpenAI models index no longer foregrounds gpt-5.6 models; it was the replacement for the 2026-12-11 gpt-5/o3 shutdowns until those replacements moved to gpt-6.1-sol.

> Source: https://developers.openai.com/api/docs/models/gpt-5.6-sol
> Source: https://developers.openai.com/api/docs/pricing.md
> Source: https://developers.openai.com/api/docs/changelog
> Source: https://developers.openai.com/api/docs/deprecations

## Cloud availability

- Amazon Bedrock: `openai.gpt-5.6-sol`. Microsoft Foundry: version 2026-07-09.

> Source: https://developers.openai.com/api/docs/models/gpt-5.6-sol
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://openai.com/index/gpt-5-6/

## Selection notes

**Catalog strengths:** Flagship GPT-5.6; complex coding, knowledge work and research.

**Catalog limitations:** Promotional price ends 2026-11-30; confirm the post-promotion rate before budgeting; No deprecation listed on OpenAI's deprecations page as of 2026-11-13.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://openai.com/index/gpt-5-6/

## Sources

- https://openai.com/index/gpt-5-6/
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/pricing.md
- https://developers.openai.com/api/docs/changelog
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://developers.openai.com/api/docs/deprecations

Fetched: 2026-11-13 UTC.
