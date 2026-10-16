# gpt-oss-120b

**Canonical ID:** `gpt-oss-120b`  
**Family:** `gpt-oss`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-10-16

## Identity and status

- Category: open-weight.
- Status: released; weights available.
- Release date: 2025-08-05.
- Availability: Weights via official Hugging Face, self-hosted deployment.
- License: Apache-2.0 (subject to OpenAI usage policy).

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://openai.com/index/introducing-gpt-oss/

## Capabilities and context

- Catalog capabilities: text, reasoning, coding, tool use, local inference.
- Context/output limits: 128K tokens.

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://openai.com/index/introducing-gpt-oss/

## Price and availability conditions

No OpenAI hosted API price; self-host compute costs vary

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://openai.com/index/introducing-gpt-oss/

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://openai.com/index/introducing-gpt-oss/

## Selection notes

**Catalog strengths:** 117B total / 5.1B active parameters; near-parity with o4-mini on core reasoning benchmarks.

**Catalog limitations:** Requires substantial local infrastructure; English-focused, text-only training; output behavior can differ from hosted APIs.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://openai.com/index/introducing-gpt-oss/

## Sources

- https://openai.com/index/introducing-gpt-oss/

Fetched: 2026-10-16 UTC.
