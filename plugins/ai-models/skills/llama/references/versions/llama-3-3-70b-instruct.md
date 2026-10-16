# Llama 3.3 70B Instruct

**Canonical checkpoint ID:** `meta-llama/Llama-3.3-70B-Instruct`  
**Status:** available; gated download; prior-generation, still widely used  
**Release:** 2024-12-06  
**Weight license:** Llama 3.3 Community License (custom terms; not OSI-approved)

## Intended role and capability boundary

Llama 3.3 70B Instruct is cataloged as open-weight, general. The recorded task capabilities are text generation, multilingual chat, tool use. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct

## Context and deployment constraints

128K tokens in the official card; standard Llama 3.3 text-only instruct model.

Older text-only generation; higher memory and serving cost than compact models; Meta Llama license terms and attribution requirements; check chat template and tool conventions per runtime.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct, https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main

## Availability, license and cost

Availability recorded for this identity: Hugging Face (gated), llama.com, multiple hosted providers and local runtimes. The weight license is **Llama 3.3 Community License (custom terms; not OSI-approved)**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API rate recorded.

> Source: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct, https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main, https://huggingface.co/meta-llama/collections

## Adoption evidence and interpretation

Official HF card showed 266K downloads and 3.14K likes for repository in the official Meta collection snapshot Scope: Hugging Face official Meta Llama collection; displayed per-model repository metadata. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/meta-llama/collections

## Selection notes

**Strengths recorded:** Mature and broadly supported deployment ecosystem; 70B dense model offers a known baseline for self-hosted general chat; community fine-tunes and quantizations are plentiful.

**Limitations recorded:** Older text-only generation; higher memory and serving cost than compact models; Meta Llama license terms and attribution requirements; check chat template and tool conventions per runtime.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Sources

- https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
- https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main
- https://huggingface.co/meta-llama/collections

Fetched: 2026-10-16
