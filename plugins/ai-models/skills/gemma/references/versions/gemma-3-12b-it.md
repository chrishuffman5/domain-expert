# Gemma 3 12B IT

**Canonical checkpoint ID:** `google/gemma-3-12b-it`  
**Status:** available; usage terms apply  
**Release:** 2025-03-12  
**Weight license:** Gemma Terms of Use and prohibited-use policy (custom terms; not OSI-approved)

## Intended role and capability boundary

Gemma 3 12B IT is cataloged as open-weight, general, multimodal, local. The recorded task capabilities are text, image understanding, 140+ languages, instruction following. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3

## Context and deployment constraints

128K tokens documented for Gemma 3; actual feasible prompt length depends on hardware and serving configuration.

Custom usage restrictions; quantization/runtime support can affect multimodal behavior; verify exact tag and chat template before migration.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3, https://ai.google.dev/gemma/terms/

## Availability, license and cost

Availability recorded for this identity: Hugging Face (terms acceptance), Kaggle, Vertex AI and local inference runtimes. The weight license is **Gemma Terms of Use and prohibited-use policy (custom terms; not OSI-approved)**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API price captured.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3, https://ai.google.dev/gemma/terms/, https://huggingface.co/google/gemma-3-12b-it

## Adoption evidence and interpretation

Official Gemma 3 family has broad model-card and deployment ecosystem; exact count for this variant unknown Scope: Google AI developer documentation and official Hugging Face card. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3

## Selection notes

**Strengths recorded:** Mid-sized multimodal general model; lower hardware threshold than 27B while retaining long context; multiple post-training variants available.

**Limitations recorded:** Custom usage restrictions; quantization/runtime support can affect multimodal behavior; verify exact tag and chat template before migration.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it

## Sources

- https://ai.google.dev/gemma/docs/core/model_card_3
- https://ai.google.dev/gemma/terms/
- https://huggingface.co/google/gemma-3-12b-it

Fetched: 2026-10-16
