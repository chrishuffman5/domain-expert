---
name: deepseek
description: "DeepSeek model selection across current hosted V4 endpoints and downloadable R1 weights. Use for task-fit, lifecycle, licensing and identity comparisons. Do NOT use for AI API or SDK mechanics, harnesses, evaluation infrastructure, inference routing, or choosing other model families."
license: MIT
---

# Deepseek model selection

## Scope and decision boundary

This skill owns DeepSeek model identity, model-level capability, lifecycle, pricing shape, license facts and task selection. It provides selection guidance rather than implementation instructions.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Model routing table

| Model | Choose it for | Key constraint | Reference |
|---|---|---|---|
| `deepseek-flash` — V4.1-Flash | Low-cost hosted reasoning, image input, tools, long context | Peak/off-peak and cache pricing; input-only vision | [version](references/versions/deepseek-flash.md) |
| `deepseek-v4-pro` — V4-Pro-0813 | Hosted text reasoning and coding when Flash is insufficient | Higher price; no image input | [version](references/versions/deepseek-v4-pro.md) |
| `DeepSeek-R1` | Open-weight reasoning research or self-hosting | 671B total parameters; current API support unconfirmed | [version](references/versions/deepseek-r1.md) |

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Choosing among the three

First decide whether you need hosted service or downloadable weights. The official current API list contains Flash and Pro. R1 is a separately distributed checkpoint. Do not use the historical R1 launch API mention as proof of a current hosted endpoint.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Reasoning and code

Flash and Pro both support thinking and non-thinking modes and tool calls. Prefer Pro when text-only difficult reasoning or coding justifies higher price. Prefer Flash for image input or lower listed rate. FIM completion is documented only in non-thinking mode for both.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Multimodal fit

Only Flash accepts image input among the current hosted DeepSeek IDs. Its vision is input-only and output is text. Do not route a screenshot task to Pro or R1 based on family name alone.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Context and output

Hosted Flash and Pro each list 1M context and 384K maximum output. These are endpoint ceilings, not a guarantee that every prompt fits or that quality is uniform across the context. Check token budgeting and current limits.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Pricing interpretation

Prices are per million tokens and split into cache-hit input, cache-miss input and output. Both have peak and off-peak rates; the source says off-peak is half-price, with Chinese public holidays treated as off-peak. Compute with the actual traffic mix.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Identity and aliases

Use `deepseek-flash` for V4.1-Flash. Legacy `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are retired names routed to that model. Do not count them as distinct identities. Pro is API ID `deepseek-v4-pro`, displayed version V4-Pro-0813.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## R1 weights and license

The R1 card and license identify MIT terms for the base model. The catalog records 671B total / 37B activated parameters and 128K context. Check terms for a particular derivative separately; this entry represents base R1.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Deployment tradeoffs

Full R1 weights require substantial infrastructure. It is older than the current hosted V4 entries. The model card also says the reasoning pattern may be skipped on some queries. Choose managed service if local capacity and operating overhead outweigh weight control.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Adoption evidence

Flash has a dated OpenRouter public-routing tokens-processed signal, which excludes direct and private traffic and is not users, spend or quality. R1 likes and discussions on Hugging Face are repository engagement proxies. Pro adoption is unknown where no comparable measured signal was found.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Selection workflow

Check image input need, hosted versus local requirement, task difficulty and traffic mix. Compare live cache/time rates; confirm model ID and lifecycle; then test representative coding, reasoning and visual tasks. Do not select solely from aggregate benchmark ranking.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Operational caveats

Very high output caps can increase cost and response time. Validate structured output with the exact endpoint. A million-token prompt can still lose relevant detail among distractors. Recheck context and output semantics before deploying long-context workflows.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Questions that change the recommendation

Ask whether images are involved, whether weights must run locally, expected input/output volume, cache reuse, peak-time sensitivity, and required completion length. If open-weight hosting is not required, compare Flash and Pro on the the actual quality/cost target.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Freshness

All captured facts are dated 2026-10-16. Reopen official model and pricing pages before quoting current IDs, price schedules, output limits or legacy alias behavior.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Sources

- https://api-docs.deepseek.com/quick_start/pricing/
- https://api-docs.deepseek.com/api/list-models/
- https://openrouter.ai/rankings?benchmark=intelligence
- https://api-docs.deepseek.com/news/news250120/
- https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/README.md
- https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/LICENSE
- https://huggingface.co/deepseek-ai/DeepSeek-R1

Fetched: 2026-10-16
## Decision checks before selecting a tier

- For image understanding, choose Flash; Pro and R1 are not documented as image-input choices here.
- For text-only code and reasoning, compare Pro against Flash at representative difficulty before accepting Pro’s higher tariff.
- For offline or controlled infrastructure, assess R1 hardware and MIT terms; do not assume a hosted R1 endpoint is current.
- If a workflow still names a V4-Flash alias, map it to `deepseek-flash` and retest its behavior.
- Estimate cache-hit and cache-miss input separately; cache reuse materially changes the quoted rate.
- Calculate peak/off-peak rates using UTC time and the provider’s stated holiday calendar.
- Budget output separately because long answers are billed at output rates and can dominate total cost.
- Use the current model list to confirm input modality, context and output before releasing a change.
- Check that the requested effort level is supported when using thinking mode.
- If you rely on FIM, keep the request in non-thinking mode as documented.
- Check concurrency against the desired traffic pattern; the pricing page lists different model limits.
- Keep the exact displayed version string with the API ID in deployment records.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

> Source: https://api-docs.deepseek.com/news/news250120/

## Claims to keep bounded

- Router token volume describes traffic through that router only.
- Router traffic is not direct DeepSeek API usage, unique developers, spend or quality.
- An open-weight license does not guarantee a particular inference engine performs well.
- Activated parameters should not be treated as a full memory requirement.
- A large context ceiling does not imply equal recall throughout a long prompt.
- A listed feature is not automatically supported across every protocol or endpoint.
- Availability in an API list does not establish a stable price for future periods.
- Provider descriptions and self-reported benchmarks should retain attribution.
- An old accepted model string can silently route to a new release; confirm the resolved identity.
- If a source does not disclose license or adoption, state that it is unknown.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

> Source: https://api-docs.deepseek.com/news/news250120/

## Review checklist for a recommendation

- Name the exact current model ID and the date it was checked.
- State if the model accepts images and whether output is text-only.
- Distinguish hosted service from local checkpoint deployment.
- Quote cache, time and token conditions next to each rate.
- Name any historical alias and explain its current mapping.
- State the R1 context and hardware concern when suggesting local hosting.
- Include a task-specific comparison plan for reasoning and coding quality.
- Preserve the source scope when citing adoption evidence.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

> Source: https://api-docs.deepseek.com/news/news250120/

