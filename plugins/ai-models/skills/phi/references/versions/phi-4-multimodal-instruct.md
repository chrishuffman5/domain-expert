# Phi-4 Multimodal Instruct

**Canonical checkpoint ID:** `microsoft/Phi-4-multimodal-instruct`  
**Status:** available  
**Release:** 2025-02-26  
**Weight license:** MIT

## Intended role and capability boundary

Phi-4 Multimodal Instruct is cataloged as open-weight, multimodal, small. The recorded task capabilities are text, image, audio, speech, multimodal reasoning. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct

## Context and deployment constraints

Variant-specific limits differ by audio/image pathway; inspect current card before setting application token budgets. Numeric ceiling recorded as unknown in this catalog.

Uses task-specific modality conventions; check model card and preprocessing; quality varies across audio and vision tasks; more integration complexity than text-only Phi-4.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct, https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Availability, license and cost

Availability recorded for this identity: Hugging Face, Azure AI Foundry, local compatible runtimes. The weight license is **MIT**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted price captured.

> Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct, https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Adoption evidence and interpretation

Official HF repository card showed 98 community Spaces at retrieval; integrations proxy only Scope: Hugging Face Spaces using official card. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct

## Selection notes

**Strengths recorded:** Combines language, vision and speech in a relatively compact family; MIT license; supports multimodal use cases without a hosted-only dependency.

**Limitations recorded:** Uses task-specific modality conventions; check model card and preprocessing; quality varies across audio and vision tasks; more integration complexity than text-only Phi-4.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Sources

- https://huggingface.co/microsoft/Phi-4-multimodal-instruct
- https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

Fetched: 2026-10-16
