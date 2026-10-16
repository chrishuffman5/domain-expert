# Gemma 3 27B IT

**Canonical checkpoint ID:** `google/gemma-3-27b-it`  
**Status:** available; usage terms apply  
**Release:** 2025-03-12  
**Weight license:** Gemma Terms of Use and prohibited-use policy (custom terms; not OSI-approved)

## Intended role and capability boundary

Gemma 3 27B IT is cataloged as open-weight, general, multimodal. The recorded task capabilities are text, image understanding, 140+ languages, reasoning, summarization. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3

## Context and deployment constraints

128K tokens documented for Gemma 3; context/input modality support can vary by serving stack.

Terms impose use/distribution restrictions and notice requirements; 27B high-quality deployment requires substantial RAM/VRAM; not audio/video input; image input only in Gemma 3; Google's benchmark claims are vendor-run.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3, https://ai.google.dev/gemma/terms/

## Availability, license and cost

Availability recorded for this identity: Hugging Face (must accept Google usage terms), Kaggle, Google AI Edge/Vertex and community runtimes. The weight license is **Gemma Terms of Use and prohibited-use policy (custom terms; not OSI-approved)**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API price captured for this downloadable model ID.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3, https://ai.google.dev/gemma/terms/, https://huggingface.co/google/gemma-3-27b-it

## Adoption evidence and interpretation

Official Gemma 3 card and Google distribution ecosystem inspected; variant-specific usage/download count unknown. Third-party quantization activity is a qualitative proxy, not official usage Scope: Google official Gemma 3 card and Hugging Face ecosystem. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3

## Selection notes

**Strengths recorded:** Open weights across sizes with image input; long context for a 27B model; well-supported on consumer/prosumer hardware when quantized.

**Limitations recorded:** Terms impose use/distribution restrictions and notice requirements; 27B high-quality deployment requires substantial RAM/VRAM; not audio/video input; image input only in Gemma 3; Google's benchmark claims are vendor-run.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-27b-it

## Sources

- https://ai.google.dev/gemma/docs/core/model_card_3
- https://ai.google.dev/gemma/terms/
- https://huggingface.co/google/gemma-3-27b-it

Fetched: 2026-10-16
