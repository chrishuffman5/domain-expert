# Gemma 3n E4B IT

**Canonical checkpoint ID:** `google/gemma-3n-E4B-it`  
**Status:** available; usage terms apply  
**Release:** 2025-06-26  
**Weight license:** Gemma Terms of Use and prohibited-use policy (custom terms; not OSI-approved)

## Intended role and capability boundary

Gemma 3n E4B IT is cataloged as open-weight, multimodal, on-device. The recorded task capabilities are text, image, audio input, video input, mobile/on-device. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://ai.google.dev/gemma/docs/gemma-3n/model_card

## Context and deployment constraints

32K total input context in official model card; 256/512/768-resolution images encode to 256 tokens each and audio to 6.25 tokens/second.

32K input cap materially shorter than Gemma 3 text/image models; effective parameter counts use per-layer embeddings and do not map directly to ordinary dense parameter footprint; modality preprocessing and hardware support are required.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://ai.google.dev/gemma/docs/gemma-3n/model_card, https://ai.google.dev/gemma/terms/

## Availability, license and cost

Availability recorded for this identity: Hugging Face (terms acceptance), Google AI Edge and supported local runtimes. The weight license is **Gemma Terms of Use and prohibited-use policy (custom terms; not OSI-approved)**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API price captured.

> Source: https://ai.google.dev/gemma/docs/gemma-3n/model_card, https://ai.google.dev/gemma/terms/, https://huggingface.co/google/gemma-3n-E4B-it

## Adoption evidence and interpretation

Official Hugging Face card showed 100 Spaces using the model at retrieval; a platform integration proxy, not usage volume Scope: Hugging Face Spaces ecosystem. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/google/gemma-3n-E4B-it

## Selection notes

**Strengths recorded:** Designed for efficient on-device multimodal inference; audio/video/image input in a compact family; official card reports over 100 HF Spaces using E4B card at retrieval.

**Limitations recorded:** 32K input cap materially shorter than Gemma 3 text/image models; effective parameter counts use per-layer embeddings and do not map directly to ordinary dense parameter footprint; modality preprocessing and hardware support are required.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3n-E4B-it

## Sources

- https://ai.google.dev/gemma/docs/gemma-3n/model_card
- https://ai.google.dev/gemma/terms/
- https://huggingface.co/google/gemma-3n-E4B-it

Fetched: 2026-10-16
