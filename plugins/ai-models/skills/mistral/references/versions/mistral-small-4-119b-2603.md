# Mistral Small 4 119B A6B

**Canonical checkpoint ID:** `mistralai/Mistral-Small-4-119B-2603`  
**Status:** available; current open-weight hybrid model  
**Release:** 2026-03-06  
**Weight license:** Apache 2.0

## Intended role and capability boundary

Mistral Small 4 119B A6B is cataloged as open-weight, general, reasoning, code, multimodal. The recorded task capabilities are general instruction following, reasoning, coding, image input, function calling. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://docs.mistral.ai/models/mistral-small-4-0-26-03

## Context and deployment constraints

256K context in official Mistral docs; confirm max sequence length and memory on selected engine.

119B total weights still require large memory despite low active count; NVFP4 and full-precision variants have different hardware requirements; model is too large for most consumer GPUs without substantial quantization/offload.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://docs.mistral.ai/models/mistral-small-4-0-26-03, https://huggingface.co/mistralai/Mistral-Small-4-119B-2603

## Availability, license and cost

Availability recorded for this identity: Hugging Face, Mistral model catalog, vLLM and compatible runtimes. The weight license is **Apache 2.0**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: Mistral API: $0.15/M input, $0.015/M cached input, $0.60/M output (USD; provider-hosted standard tier, subject to price changes); self-host cost varies.

> Source: https://docs.mistral.ai/models/mistral-small-4-0-26-03, https://huggingface.co/mistralai/Mistral-Small-4-119B-2603, https://huggingface.co/collections/mistralai/mistral-small-4, https://docs.mistral.ai/inference/pricing

## Adoption evidence and interpretation

Official Mistral HF collection showed 74.9K downloads and 452 likes on the main checkpoint listing at retrieval; download window is HF-defined and not unique users Scope: Mistral official Hugging Face model collection. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/mistralai/Mistral-Small-4-119B-2603

## Selection notes

**Strengths recorded:** 119B total / 6.5B active hybrid MoE model unifies instruction, reasoning and coding; Multimodal text/image input and tool calling; current alternative after Mistral Small 3.x retirements; community deployment artifacts.

**Limitations recorded:** 119B total weights still require large memory despite low active count; NVFP4 and full-precision variants have different hardware requirements; model is too large for most consumer GPUs without substantial quantization/offload.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Sources

- https://docs.mistral.ai/models/mistral-small-4-0-26-03
- https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
- https://huggingface.co/collections/mistralai/mistral-small-4
- https://docs.mistral.ai/inference/pricing

Fetched: 2026-10-16
