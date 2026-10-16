# Llama 4 Scout Instruct

**Canonical checkpoint ID:** `meta-llama/Llama-4-Scout-17B-16E-Instruct`  
**Status:** available; gated download  
**Release:** 2025-04-05  
**Weight license:** Llama 4 Community License (custom terms; not an OSI-approved open-source license)

## Intended role and capability boundary

Llama 4 Scout Instruct is cataloged as open-weight, general, multimodal, long-context. The recorded task capabilities are text generation, image understanding, multilingual, long-context. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

## Context and deployment constraints

Meta advertises 10M input tokens; the official card documents 256K pre/post-training length and long-context generalization experiments. Effective use of the advertised maximum depends on serving implementation, memory and quality validation.

Total expert weights and long context make memory/serving heavier than active-parameter count suggests; maximum context support is not equivalent to reliable retrieval across the full window; custom license and gated access; validate output quality on target workloads.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/, https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct

## Availability, license and cost

Availability recorded for this identity: Hugging Face (gated), llama.com, third-party inference providers. The weight license is **Llama 4 Community License (custom terms; not an OSI-approved open-source license)**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API rate recorded; self-hosting costs depend on hardware, quantization and context KV cache.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/, https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct, https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original

## Adoption evidence and interpretation

Official HF card showed 5.0M downloads and 700 likes for the Scout family card at retrieval; family-level count and platform-specific proxy, not unique production users Scope: Hugging Face official Meta Llama card. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original

## Selection notes

**Strengths recorded:** 10M advertised context ceiling; multimodal image input; 17B active parameters with 109B total MoE weights; family ecosystem and broad tooling.

**Limitations recorded:** Total expert weights and long context make memory/serving heavier than active-parameter count suggests; maximum context support is not equivalent to reliable retrieval across the full window; custom license and gated access; validate output quality on target workloads.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original

## Sources

- https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct
- https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original

Fetched: 2026-10-16
