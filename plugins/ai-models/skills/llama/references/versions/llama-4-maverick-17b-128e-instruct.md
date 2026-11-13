# Llama 4 Maverick Instruct

**Canonical checkpoint ID:** `meta-llama/Llama-4-Maverick-17B-128E-Instruct`  
**Status:** available; gated download  
**Release:** 2025-04-05  
**Weight license:** Llama 4 Community License (custom terms; not an OSI-approved open-source license)

## Intended role and capability boundary

Llama 4 Maverick Instruct is cataloged as open-weight, general, multimodal. The recorded task capabilities are text generation, image understanding, multilingual, assistant/chat. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

## Context and deployment constraints

128K context reported in the official model card/release materials; treat provider maximum as implementation-specific.

400B total parameters create substantial storage and serving requirements even though 17B are active; requires distributed or high-memory serving; community license and gated download; Meta describes benchmark superiority as vendor-reported; evaluate independently.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/, https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct

## Availability, license and cost

Availability recorded for this identity: Hugging Face (gated), llama.com, third-party inference providers. The weight license is **Llama 4 Community License (custom terms; not an OSI-approved open-source license)**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API rate recorded; self-hosting costs depend on hardware, quantization and expert placement.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/, https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct, https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md

## Adoption evidence and interpretation

Official HF repository card lists active community and usage integrations; exact current downloads not captured in inspected source, so count unknown Scope: Official Hugging Face repository. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct

## Selection notes

**Strengths recorded:** Multimodal, multilingual general assistant; 17B active parameters while retaining broad expert capacity; a useful stronger generalist comparator within the Llama ecosystem.

**Limitations recorded:** 400B total parameters create substantial storage and serving requirements even though 17B are active; requires distributed or high-memory serving; community license and gated download; Meta describes benchmark superiority as vendor-reported; evaluate independently.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md

## Sources

- https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct
- https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md

Fetched: 2026-10-16
