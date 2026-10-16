# DeepSeek-V4.1-Flash

Canonical model ID: `deepseek-flash`

## Identity and status

- Provider: DeepSeek.
- Family: `deepseek`.
- Role: reasoning.
- Status: Current hosted API model; legacy V4-Flash aliases route to this model.
- Release: unknown.
- Availability: DeepSeek API; OpenAI-compatible and Anthropic-compatible API.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

## Canonical ID, versions and aliases

- Canonical catalog ID: `deepseek-flash`.
- Display name: DeepSeek-V4.1-Flash.
- Version/checkpoint date: unknown.
- Alias and region note: `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are retired names routed to this model, not distinct releases.
- Region-specific IDs: No additional regional ID confirmed in the catalog sources; verify the target region.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Capabilities and context

- Capabilities: text and image input; thinking and non-thinking modes; tool calls; JSON output; FIM completion in non-thinking mode.
- Context/output: 1,048,576 tokens; maximum output 393,216 tokens.
- Strengths: Current low-cost multimodal DeepSeek offering; Long context and unusually high output ceiling; Thinking mode plus tool calling.
- Limitations: Vision is input-only; Pricing varies by peak/off-peak schedule; Legacy model IDs may obscure that old V4-Flash variants are retired and routed here.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Pricing and access

- Price: Per 1M tokens: cache-hit input $0.003 off-peak/$0.006 peak; cache-miss input $0.15/$0.30; output $0.60/$1.20. Off-peak is half-price under published weekday/time/holiday rules.
- Recheck live price, account eligibility, service region, context mode and cache/peak conditions before budgeting.
- Self-host costs are separate from hosted API rates and depend on hardware and workload.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## License and use

- License/terms: Hosted API; model-weight license not stated in inspected API docs.
- Do not infer weight rights from API availability, code repository license, or the words open weights.
- For hosted models, service terms govern access; a weight license applies only where weights are explicitly distributed under it.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Adoption evidence and caveats

- Evidence: Observed platform usage: OpenRouter ranked DeepSeek V4.1 Flash first in the displayed tokens-processed table with 40.5T tokens and +37%; usage data was through 2026-10-13. The selected current API ID aliases to this release per DeepSeek docs.
- Scope: OpenRouter public-routed traffic, prompt plus completion tokens in UTC buckets. Excludes private traffic and direct/other-router use; tokens are not users, spend, task preference, or quality.
- Date: 2026-10-16
- Repository engagement, routed traffic and API availability have different denominators; none establishes total global use or quality.

> Source: https://openrouter.ai/rankings?benchmark=intelligence

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Selection guidance

Use this entry when the task matches its documented strengths: Current low-cost multimodal DeepSeek offering; Long context and unusually high output ceiling; Thinking mode plus tool calling. Compare other entries in the family on modality, price, reasoning, context, terms and hosting. Confirm the exact model string and live lifecycle before use.

> Source: https://api-docs.deepseek.com/quick_start/pricing/

> Source: https://api-docs.deepseek.com/api/list-models/

> Source: https://openrouter.ai/rankings?benchmark=intelligence

## Sources

- https://api-docs.deepseek.com/quick_start/pricing/
- https://api-docs.deepseek.com/api/list-models/
- https://openrouter.ai/rankings?benchmark=intelligence

Fetched: 2026-10-16
