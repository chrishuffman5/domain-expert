# Gemma 4 31B IT

**Canonical checkpoint ID:** `google/gemma-4-31B-it`  
**Status:** available; latest Gemma generation  
**Release:** 2026-07  
**Weight license:** Apache 2.0

## Intended role and capability boundary

Gemma 4 31B IT is cataloged as open-weight, general, reasoning, multimodal, coding. The recorded task capabilities are reasoning with configurable thinking, text and image, video understanding, coding, native function calling, 35+ languages; trained on 140+. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://ai.google.dev/gemma/docs/core/model_card_4

## Context and deployment constraints

256K tokens. Image/video inputs and visual token budgeting affect context consumption; audio is not supported in this 31B variant.

31B dense model needs substantial memory; 256K serving requires larger KV cache; Gemma 4 card reports vendor-run benchmarks; task-specific validation still required; different prompt format and native system role from Gemma 3; do not assume drop-in compatibility.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://ai.google.dev/gemma/docs/core/model_card_4, https://huggingface.co/collections/google/gemma-4

## Availability, license and cost

Availability recorded for this identity: Hugging Face, Google AI model distribution and partners, local and cloud runtimes. The weight license is **Apache 2.0**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted API price captured for the downloadable checkpoint.

> Source: https://ai.google.dev/gemma/docs/core/model_card_4, https://huggingface.co/collections/google/gemma-4, https://huggingface.co/google/gemma-4-31B-it

## Adoption evidence and interpretation

Official Google HF collection showed 9.18M downloads and 4.13K likes on the 31B instruct card at retrieval; HF download window is platform-defined, not unique users Scope: Google official Gemma 4 HF collection/model listing. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/collections/google/gemma-4

## Selection notes

**Strengths recorded:** Current dense flagship in Gemma 4 with reasoning, image/video and function calling; 256K context and broad deployment ecosystem; strong newest-family option to compare against Gemma 3.

**Limitations recorded:** 31B dense model needs substantial memory; 256K serving requires larger KV cache; Gemma 4 card reports vendor-run benchmarks; task-specific validation still required; different prompt format and native system role from Gemma 3; do not assume drop-in compatibility.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it

## Sources

- https://ai.google.dev/gemma/docs/core/model_card_4
- https://huggingface.co/collections/google/gemma-4
- https://huggingface.co/google/gemma-4-31B-it

Fetched: 2026-10-16
