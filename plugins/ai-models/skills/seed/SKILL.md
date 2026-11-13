---
name: seed
description: "ByteDance Seed selection across hosted Seed2.1 Pro/Turbo regional endpoints and Seed-OSS-36B-Instruct weights. Use for modality, local versus hosted, market-specific IDs and terms. Do NOT use for AI API/SDK mechanics, harnesses, evaluation infrastructure, inference routing, or other families."
license: MIT
---

# Seed model selection

## Scope and decision boundary

This skill covers model identity, model-level capability, lifecycle, regional endpoints, licenses and task fit. It excludes API implementation, harnesses, evaluation and cross-family routing.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Model routing table

| Model | Choose it for | Key constraint | Reference |
|---|---|---|---|
| Seed2.1 Pro — `doubao-seed-2-1-pro-260628` | Complex hosted agent, code, office and video work | Verify Volcano Engine region/access and tariff | [version](references/versions/doubao-seed-2-1-pro-260628.md) |
| Seed2.1 Turbo — `dola-seed-2-1-turbo-260628` | Hosted Turbo service tier | BytePlus ID; service-specific rates | [version](references/versions/dola-seed-2-1-turbo-260628.md) |
| `ByteDance-Seed/Seed-OSS-36B-Instruct` | Local instruction, code, math and agent research | Older weights; confirm numeric limits | [version](references/versions/seed-oss-36b-instruct.md) |

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Hosted tiers

Pro is positioned for complex or high-value tasks. Turbo is a distinct endpoint tier; verify actual pricing and performance before assuming it is faster or cheaper. Keep these identities separate.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Regional identity

Volcano Engine’s ID is `doubao-seed-2-1-pro-260628`; BytePlus ModelArk lists `dola-seed-2-1-turbo-260628`. Product names differ by market and plan. Use the exact ID documented by the service that will host the request.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Capability fit

Seed2.1 is positioned for agentic productivity, coding, reasoning, visual and video understanding. Benchmarks on the official page are provider-reported. Test Chinese/English language mix, file types, image/video and tool sequences relevant to the workload.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Context and price

Catalog evidence records 256K context for both hosted tiers, with Turbo’s ModelArk record also listing input/output ceilings. Rates depend on region and prompt length; coding plan and API charges can differ. Confirm whether reasoning tokens count toward output.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Open checkpoint

Seed-OSS-36B-Instruct is the instruction-tuned 36B option for local assistant-style work. The catalog records Apache-2.0 terms from official release and model card. No current hosted API endpoint is established.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Serving needs

A 36B checkpoint still requires meaningful GPU memory and compute. Confirm model-card context, runtime, precision and hardware before planning. Do not apply hosted Seed2.1 prices to local OSS inference.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Adoption evidence

Hugging Face likes/discussions are repository-engagement proxies. Product launch and model listings indicate distribution and availability, not quantified use.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Lifecycle hygiene

Keep Pro and Turbo distinct. Determine if endpoint is a fixed dated snapshot or rolling name. Recheck region and product-level status whenever changing model ID.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Selection workflow

Clarify hosted versus local, target service and region, task modality and price envelope. Verify exact endpoint, context and terms. For local use Instruct, then check weight license, model card, runtime and compute.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Migration and reliability

Keep a task-specific quality test set and rerun it when the underlying snapshot changes. Provider benchmark results do not predict every workload or language. Validate model behavior on real agent traces.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Freshness

Facts were captured on 2026-10-16. Recheck ByteDance, Volcano Engine, BytePlus and Hugging Face sources before stating current price, ID, context, availability or license.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

## Sources

- https://seed.bytedance.com/en/seed2_1
- https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity
- https://seed.bytedance.com/en/blog/seed-2-0-official-launch
- https://seed.bytedance.com/en/models
- https://seed.bytedance.com/en/seed_model_portfolio
- https://www.volcengine.com/article/2608790
- https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-list
- https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-pricing
- https://ai.byteplus.com/ark/region:ap-southeast-1/docs/quick-start
- https://seed.bytedance.com/en/blog/seed-oss-open-source-models-release
- https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct
- https://research.doubao.com/en/models

Fetched: 2026-10-16
## Decision checks before selecting a Seed model

- Ask which product and region will serve the hosted model.
- Use the exact endpoint ID listed by the target provider.
- Keep Pro and Turbo separate rather than assuming a naming alias.
- Confirm which tariff applies to the user’s product or coding plan.
- Check whether context includes reasoning tokens in the selected service.
- Use Pro for complex tasks only where its quality merits the tariff.
- Validate a presumed Turbo efficiency advantage with current evidence.
- For local assistant work, start with OSS-36B-Instruct rather than the base checkpoint.
- Check the card for numeric context and runtime details before sizing a deployment.
- Keep hosted service prices separate from local compute costs.
- Review the exact Apache-2.0 source before redistribution.
- Retest whenever the dated snapshot or regional ID changes.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

> Source: https://seed.bytedance.com/en/models

## Claims to keep bounded

- Provider-published benchmarks are not independent confirmation.
- Launch on a consumer product demonstrates distribution, not measured use.
- Hugging Face likes are engagement signals, not active deployments.
- Pro and Turbo names alone do not establish comparative latency.
- One market’s ID cannot be assumed to work in another market.
- Hosted context limits do not establish the OSS checkpoint context.
- Apache-2.0 for OSS does not apply to hosted Seed2.1 service terms.
- Instruction tuning makes Instruct more assistant-oriented than Base; it does not prove quality for every task.
- Video understanding should be validated on the selected service and content type.
- Unknown current API support for OSS must stay unknown.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

> Source: https://seed.bytedance.com/en/models

## Review checklist for a recommendation

- Record provider product, deployment region, and exact model ID.
- Compare Pro and Turbo on the workload and the current regional tariff.
- State whether the model is hosted or downloadable.
- Confirm language, modality, context, and output conditions.
- Use Instruct for assistant tasks unless there is a specific fine-tuning need.
- Check weight license and hosting rights independently.
- Test migration against realistic agent traces.
- Attribute adoption and benchmark statements to their sources.

> Source: https://seed.bytedance.com/en/seed2_1

> Source: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity

> Source: https://seed.bytedance.com/en/blog/seed-2-0-official-launch

> Source: https://seed.bytedance.com/en/models

