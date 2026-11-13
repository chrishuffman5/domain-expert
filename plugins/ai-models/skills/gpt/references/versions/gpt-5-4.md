# GPT-5.4

**Canonical ID:** `gpt-5.4`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: frontier.
- Status: current/API (listed under More models; no deprecation).
- Release date: 2026-03-05.
- Availability: API; Codex; ChatGPT product also exists, but entry is API ID.
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://openai.com/index/introducing-gpt-5-4/

## Capabilities and context

- Catalog capabilities: text, image, reasoning, coding, tool use, computer use, professional work.
- Context/output limits: 272K standard; experimental 1M in Codex only.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://openai.com/index/introducing-gpt-5-4/

## Price and availability conditions

$2.50 input / $0.25 cached / $15 output per MTok (Standard, prompts <=272K)

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/pricing.md

## Verified details as of 2026-11-13

- Standard price per MTok (prompts up to 272K): $2.50 input, $0.25 cached, $15 output, matching the launch price.
- Listed under "More models" on the OpenAI models index; no deprecation row. Sibling gpt-5.4-nano is deprecated (shutdown 2027-04-01, replacement gpt-6-luna); gpt-5.4-mini is priced at $0.75/$4.50.

> Source: https://developers.openai.com/api/docs/pricing.md
> Source: https://developers.openai.com/api/docs/models/all
> Source: https://developers.openai.com/api/docs/deprecations
> Source: https://developers.openai.com/api/docs/pricing

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://openai.com/index/introducing-gpt-5-4/

## Selection notes

**Catalog strengths:** General reasoning, professional knowledge work, coding and agents.

**Catalog limitations:** 1M context noted for Codex experimental setup, not standard API; price evolved.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://openai.com/index/introducing-gpt-5-4/

## Sources

- https://openai.com/index/introducing-gpt-5-4/
- https://developers.openai.com/api/docs/pricing.md
- https://developers.openai.com/api/docs/models/all
- https://developers.openai.com/api/docs/deprecations
- https://developers.openai.com/api/docs/pricing

Fetched: 2026-11-13 UTC.
