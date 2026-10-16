# Phi-4

**Canonical checkpoint ID:** `microsoft/phi-4`  
**Status:** available  
**Release:** 2024-12-12  
**Weight license:** MIT

## Intended role and capability boundary

Phi-4 is cataloged as open-weight, general, reasoning, small. The recorded task capabilities are text generation, reasoning, math, code. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://huggingface.co/microsoft/phi-4

## Context and deployment constraints

16K tokens in Microsoft model card; no vision/audio for this named variant.

16K context is short by current long-context standards; vendor benchmark claims require independent validation; model card asks developers to add appropriate safeguards for harmful content.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://huggingface.co/microsoft/phi-4, https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/

## Availability, license and cost

Availability recorded for this identity: Hugging Face, Microsoft Azure AI Foundry, vLLM/SGLang and local runtimes. The weight license is **MIT**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted price captured for downloadable model.

> Source: https://huggingface.co/microsoft/phi-4, https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/

## Adoption evidence and interpretation

Official HF card showed 426,836 downloads in the last month at retrieval. Scope: Hugging Face microsoft/phi-4 model card; downloads are not unique users. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/microsoft/phi-4

## Selection notes

**Strengths recorded:** 14B dense model with unusually strong reasoning for size per Microsoft evaluations; permissive MIT license; official runtime options and data summary.

**Limitations recorded:** 16K context is short by current long-context standards; vendor benchmark claims require independent validation; model card asks developers to add appropriate safeguards for harmful content.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/

## Sources

- https://huggingface.co/microsoft/phi-4
- https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/

Fetched: 2026-10-16
