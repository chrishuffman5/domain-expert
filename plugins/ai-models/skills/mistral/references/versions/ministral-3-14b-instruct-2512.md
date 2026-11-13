# Ministral 3 14B Instruct 2512

**Canonical checkpoint ID:** `mistralai/Ministral-3-14B-Instruct-2512`  
**Status:** available  
**Release:** 2025-12  
**Weight license:** Apache 2.0

## Intended role and capability boundary

Ministral 3 14B Instruct 2512 is cataloged as open-weight, general, multimodal, edge-to-cloud. The recorded task capabilities are text, vision, general assistant. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://docs.mistral.ai/models

## Context and deployment constraints

256K context window documented by Mistral; runtime memory and modality input budgets reduce practical usable context.

14B still needs meaningful accelerator memory for full precision and long contexts; do not assume all runtimes implement vision identically; newer release has less long-term adoption history than Llama 3.3.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://docs.mistral.ai/models, https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512

## Availability, license and cost

Availability recorded for this identity: Hugging Face, Mistral model catalog, local/partner runtimes. The weight license is **Apache 2.0**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: Mistral API: $0.20/M input, $0.02/M cached input, $0.20/M output (USD; standard hosted tier, subject to change); self-host cost varies.

> Source: https://docs.mistral.ai/models, https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512, https://docs.mistral.ai/models/ministral-3-14b-25-12

## Adoption evidence and interpretation

Official HF card shows an active community and distribution; exact download count was not exposed in inspected result Scope: Mistral official HF repository. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512

## Selection notes

**Strengths recorded:** Smaller multimodal option than Mistral Large; size useful for single-node and tuned local deployment; official model release and family docs identify 3B/8B/14B sizes.

**Limitations recorded:** 14B still needs meaningful accelerator memory for full precision and long contexts; do not assume all runtimes implement vision identically; newer release has less long-term adoption history than Llama 3.3.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12

## Sources

- https://docs.mistral.ai/models
- https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512
- https://docs.mistral.ai/models/ministral-3-14b-25-12

Fetched: 2026-10-16
