# GPT-6 Sol

**Canonical ID:** `gpt-6-sol`  
**Family:** `gpt`  
**Provider:** OpenAI  
**Catalog snapshot:** 2026-11-13

## Identity and status

- Category: frontier.
- Status: current (superseded by gpt-6.1-sol; no deprecation listed).
- Release date: 2026-09-22.
- Availability: OpenAI API; Amazon Bedrock `openai.gpt-6-sol`; Microsoft Foundry (version 2026-09-22).
- License: unknown.

This file records one distinct catalog identity. A product label, API endpoint, alias, regional endpoint, or serving profile does not become a second model unless the provider documents a separate underlying model identity.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol

## Capabilities and context

- Catalog capabilities: text, image, reasoning, coding, tools, vision.
- Context/output limits: 1.05M tokens (922K max input); 128K max output; knowledge cutoff 2026-04-20 (as stated on the model page).

These fields reflect the catalog snapshot. Unknown or missing values should stay unknown until a current provider source supplies them. Do not infer a capability from a family name or from another tier in this family.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol

## Price and availability conditions

$2 input / $0.20 cached / $10 output per MTok (prompts <=272K)

Read this alongside the provider's current pricing page and model availability before making a deployment decision. Promotional prices, cached-token rates, long-context pricing, service tiers, regional surcharges and project eligibility can change the effective cost. No rate should be carried over from a sibling model.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol

## Identity and lifecycle

- Released 2026-09-22 together with gpt-6-luna. "Built for complex coding and agentic workflows." Missing from the 2026-10-16 snapshot; added 2026-11-13.
- The model page says "See GPT-6.1 Sol for the newer Sol model". gpt-6-sol is not an alias of gpt-6.1-sol and has no deprecation listed.
- Context 1,050,000; max input 922,000; max output 128,000; knowledge cutoff 2026-04-20 as stated on the page; text and image in, text out.
- Reasoning effort: none, low, medium (default), high, xhigh, max. Price per MTok: $2 input, $0.20 cached, $10 output (prompts up to 272K).
- 2026-09-25: image-encoding bug fix affecting gpt-6-sol and gpt-6-luna; rerun image-input evals from before that date.
- Named replacement for gpt-5.3-codex and gpt-5.1, which shut down 2027-04-01.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol
> Source: https://developers.openai.com/api/docs/changelog
> Source: https://developers.openai.com/api/docs/deprecations

## Cloud availability

- Amazon Bedrock: `openai.gpt-6-sol` (per the OpenAI model page). Microsoft Foundry: `gpt-6-sol` version 2026-09-22. Google Cloud Vertex AI: not in its private-preview list.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai

## gpt-6-sol or gpt-6.1-sol

- Both list $2/$10 base rates; 6.1 Sol has cheaper cached input ($0.10 vs $0.20) and no `none` effort, while 6 Sol supports `none`. Prefer gpt-6.1-sol for new work and keep gpt-6-sol where an existing workload has been validated on it or needs `none` effort.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol
> Source: https://developers.openai.com/api/docs/models/gpt-6.1-sol

## Adoption evidence

**Signal:** Unknown. No model-specific comparable public usage signal was established in the catalog.

**Scope and caveat:** No comparable official usage/adoption telemetry found in inspected sources.

The signal is evidence about the stated platform or reporting window only. It does not establish global preference, quality, active users, spend, or use outside the covered channel. Unknown means unavailable in the inspected evidence, not zero adoption.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol

## Selection notes

**Catalog strengths:** Built for complex coding and agentic workflows; reasoning effort none–max (default medium); Named replacement for gpt-5.1 and gpt-5.3-codex (shutdown 2027-04-01).

**Catalog limitations:** Superseded by gpt-6.1-sol at the same $2/$10 base rate; 6.1 Sol has cheaper cached input ($0.10); An image-encoding bug affecting gpt-6-sol was fixed 2026-09-25; rerun image-input evals from before that date.

Use this model when a representative workload demonstrates that its documented strengths matter enough to justify its price, availability constraints, and operating profile. Compare it with its nearest family alternative using the same prompts, context length, tools, latency target, and output budget. The family guide explains the selection branch; it does not replace workload testing.

> Source: https://developers.openai.com/api/docs/models/gpt-6-sol

## Sources

- https://developers.openai.com/api/docs/models/gpt-6-sol
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/deprecations
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai
- https://developers.openai.com/api/docs/models/gpt-6.1-sol

Fetched: 2026-11-13 UTC.
