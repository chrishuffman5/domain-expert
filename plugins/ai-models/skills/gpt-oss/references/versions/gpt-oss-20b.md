# gpt-oss-20b

**Canonical ID:** `gpt-oss-20b`  
**Family:** `gpt-oss`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: open-weight.
- Status: released; weights available.
- Release date: 2025-08-05.
- Availability: Weights via official Hugging Face; self-hosted deployment; Microsoft Foundry (Preview, managed compute).
- License: Apache-2.0 (subject to OpenAI usage policy).

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://openai.com/index/introducing-gpt-oss/

## Capabilities and context

- Catalog capabilities: text, reasoning, coding, tool use, edge inference.
- Context/output limits: 128K tokens.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://openai.com/index/introducing-gpt-oss/

## Price and availability conditions

No OpenAI hosted API price; self-host compute costs vary

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://openai.com/index/introducing-gpt-oss/

## Verified details as of 2026-11-13

- No newer gpt-oss model was found; gpt-oss-20b is unchanged. Listed under "Open-weight models" on the OpenAI models index with no deprecation row.
- Microsoft Foundry: Preview, managed compute.
- The gpt-oss-20b model page was not re-fetched in this pass; parameter, context and memory figures come from the 2025 release post.

> Source: https://developers.openai.com/api/docs/models/all
> Source: https://developers.openai.com/api/docs/deprecations
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://openai.com/index/introducing-gpt-oss/

## Selection notes

**Catalog strengths:** 21B total / 3.6B active parameters; can run with 16GB memory per launch page.

**Catalog limitations:** Lower capability ceiling than larger tier; English-focused, text-only training; deployment burden remains.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://openai.com/index/introducing-gpt-oss/

## Sources

- https://openai.com/index/introducing-gpt-oss/
- https://developers.openai.com/api/docs/models/all
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://developers.openai.com/api/docs/deprecations

Fetched: 2026-11-13 UTC.
