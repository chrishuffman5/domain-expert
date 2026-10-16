# Command A Reasoning (`command-a-reasoning-08-2025`)

Status: active in Cohere's model overview. Official release date: 2025-08-21. Canonical API ID: `command-a-reasoning-08-2025`. No alias mapping is listed on the inspected source. Do not confuse this reasoning model with `command-a-03-2025` (general Command A) or `command-a-plus-05-2026` (multimodal MoE tier).

## Behavior and limits

Command A Reasoning is Cohere's reasoning-first Command model for complex, nuanced problems and agentic workflows. It supports tool use, RAG and multilingual work; the overview lists 23 languages. The model page describes it as a 111B model with 256K context and says its production hardware target is 4 H100 GPUs; 4 A100s are mentioned for non-production tryouts/evaluations. The family overview lists maximum output at 32K and text input. Do not borrow the 64K output or image input specs from A+.

> Source: https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/models ; https://docs.cohere.com/changelog/2025-08-21-command-a-reasoning (inspected 2026-10-16)

## Price, availability and license

Pricing is unknown in the inspected model-specific documentation. Cohere's general pricing overview says generative models are token-priced, but does not give a current Command A Reasoning rate in the inspected material. Cohere API access can depend on key type/rate limits; production deployment is through Cohere's commercial Model Vault offering. Check the current account entitlement and contract instead of copying A's published rate.

The catalog records proprietary hosted API/model deployment. The inspected model page did not identify a public downloadable checkpoint license for this reasoning variant; do not assume it inherits Apache 2.0 from the different Command A+ W4A4 release.

> Source: https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/models (inspected 2026-10-16)

## When to select it

Choose Command A Reasoning when the task benefits from deliberate reasoning, multistep tool use, RAG and 256K context, and the production hardware/cost envelope is acceptable. This is the selected Command family reasoning entry. For image inputs plus tool use, A+ is the family alternative. For image/document perception without tool calls, use A Vision. For routine throughput-sensitive workloads, assess compact alternatives before paying for a large reasoning model.

Do not assume reasoning improves every prompt. Compare answer quality, completion length, latency and total task cost against a non-reasoning route on the workload's eval set. Explicitly set and document the applicable thinking/reasoning controls if the API offers them; don't infer a request parameter from another provider's API.

> Source: https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/models (inspected 2026-10-16)

## Adoption and change control

No model-specific usage or download metric was published by Cohere in the inspected sources. Adoption remains unknown. The 2025-08-21 date is the documented release date, unlike a page-modified timestamp. Recheck active status, current model ID, output limit, key eligibility, production deployment requirements and current pricing before use. Do not swap version IDs without evaluating behavior and lifecycle.

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/changelog/2025-08-21-command-a-reasoning (inspected 2026-10-16)

## Sources

- https://docs.cohere.com/docs/command-a-reasoning
- https://docs.cohere.com/docs/models
- https://docs.cohere.com/changelog/2025-08-21-command-a-reasoning

Fetched: 2026-10-16
