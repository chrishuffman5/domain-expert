# Mistral Large 3 675B Instruct 2512

**Canonical checkpoint ID:** `mistralai/Mistral-Large-3-675B-Instruct-2512`  
**Status:** available; current open-weight release  
**Release:** 2025-12  
**Weight license:** Apache 2.0

## Intended role and capability boundary

Mistral Large 3 675B Instruct 2512 is cataloged as open-weight, general, multimodal, frontier. The recorded task capabilities are text, image understanding, multilingual, agentic/instruction tasks. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://docs.mistral.ai/models

## Context and deployment constraints

256K context listed in Mistral model overview/known-limitations material; confirm exact runtime and modality limits before using maximum lengths.

Very large total weights require multi-GPU/distributed memory; 41B active count does not eliminate storage cost; official HF card notes Transformers support was not yet integrated at publication; card is FP8 instruct; base/quantized variants are distinct artifacts.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://docs.mistral.ai/models, https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512

## Availability, license and cost

Availability recorded for this identity: Hugging Face, Mistral model catalog, vLLM and partner deployments. The weight license is **Apache 2.0**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: Mistral API: $0.50/M input, $0.05/M cached input, $1.50/M output (USD; standard hosted tier, subject to change); self-host cost varies.

> Source: https://docs.mistral.ai/models, https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512, https://docs.mistral.ai/resources/known-limitations, https://docs.mistral.ai/models/mistral-large-3-25-12

## Adoption evidence and interpretation

Official HF repository displayed 20.1K provider followers and 14 discussion items; direct downloads/production use unknown Scope: Mistral AI official HF repository. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512

## Selection notes

**Strengths recorded:** General-purpose multimodal MoE with 41B active / 675B total parameters; large multilingual model; official card recommends vLLM and provides runnable guidance.

**Limitations recorded:** Very large total weights require multi-GPU/distributed memory; 41B active count does not eliminate storage cost; official HF card notes Transformers support was not yet integrated at publication; card is FP8 instruct; base/quantized variants are distinct artifacts.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12

## Sources

- https://docs.mistral.ai/models
- https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512
- https://docs.mistral.ai/resources/known-limitations
- https://docs.mistral.ai/models/mistral-large-3-25-12

Fetched: 2026-10-16
