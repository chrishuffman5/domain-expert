# Command A+ (`command-a-plus-05-2026`)

Status: active. Cohere lists release date 2026-05-20. Canonical Cohere Chat model ID: `command-a-plus-05-2026`. The separate Hugging Face artifact selected by Cohere for open distribution is `CohereLabs/command-a-plus-05-2026-w4a4`; that is a W4A4 checkpoint artifact of the A+ model, not a second catalog identity. No alias mapping is listed on the inspected model page.

## Capabilities and limits

Command A+ accepts text and image inputs and produces text. It combines multimodal perception, tool use, reasoning and multilingual agent behavior. Cohere describes 48 supported languages. The model page reports a sparse mixture-of-experts architecture with 218B total parameters and 25B active parameters. Context window: 128,000 tokens. Maximum output: 64,000 tokens.

Cohere positions A+ as its fastest and most capable Command A family model for agentic/multimodal tasks. This is provider positioning. Benchmark evidence and task-level accuracy should be tested using representative workloads.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/models (inspected 2026-10-16)

## Pricing, access and license

The model page says trial and production API keys can use Command A+ free until rate limits are reached. This does not establish a generally free production service: production Model Vault is commercial and governed by customer terms; the inspected source does not list a production token rate. Record current pricing as unknown unless the active account's Cohere rate card supplies it.

The released Hugging Face W4A4 checkpoint carries Apache 2.0. This license applies to that model artifact. The hosted Cohere API and Model Vault remain subject to their service/commercial terms; do not conflate the checkpoint license with API access rights. The checkpoint is quantized; its compute and quality tradeoffs may differ from an unquantized hosted route. The docs say the model can fit on one B200 or two H100 GPUs at W4A4. Verify the exact hardware/runtime recipe for the artifact version you plan to serve.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4 (inspected 2026-10-16)

## Selection guidance

Choose A+ when one hosted or self-managed Command model needs both vision input and agentic/tool-use capability, broad language coverage, and long output allowance. It is the current selected Command family general/frontier-like option. Its 128K context is shorter than Command A Reasoning's 256K. Use Reasoning when explicit reasoning-first behavior and longer context matter more than vision input. Use Vision when the workload is document/image understanding but tool use is unnecessary; the Vision model explicitly lacks tool use.

Tool use is an interface for proposing actions, not permission to perform them. Validate arguments, enforce policy and permissions in application code, and require review for consequential actions. For visual document tasks, check the number/size/format limits in Cohere image-input docs before sending scans or many pages.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Adoption and lifecycle

Cohere did not publish model-level usage or download totals in the inspected source. Adoption is unknown; model release and availability are not usage proxies. Recheck the current Cohere model overview, Model Vault deployment conditions, endpoint ID and rate card before selecting or budgeting. No retirement date is listed in the inspected sources.

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/docs/command-a-plus (inspected 2026-10-16)

## Sources

- https://docs.cohere.com/docs/command-a-plus
- https://docs.cohere.com/docs/models
- https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4

Fetched: 2026-10-16
