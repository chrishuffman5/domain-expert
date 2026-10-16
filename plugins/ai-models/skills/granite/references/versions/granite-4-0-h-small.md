# Granite 4.0 H Small

**Canonical checkpoint ID:** `ibm-granite/granite-4.0-h-small`  
**Status:** available  
**Release:** 2025-10  
**Weight license:** Apache 2.0

## Intended role and capability boundary

Granite 4.0 H Small is cataloged as open-weight, general, enterprise, long-context. The recorded task capabilities are text generation, enterprise workflows, tool calling, long-context. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small

## Context and deployment constraints

IBM documentation describes it as long-context; the inspected card did not surface a numeric cap in the extracted text, so value recorded unknown pending exact config verification.

32B memory demand; quantization needed on modest hardware; IBM warns legacy docs are no longer updated; prefer HF/GitHub for latest; check exact context length in current model config before claiming a ceiling.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small, https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized

## Availability, license and cost

Availability recorded for this identity: Hugging Face, IBM Granite docs, vLLM, SGLang, Docker Model Runner. The weight license is **Apache 2.0**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No official hosted price captured.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small, https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized, https://www.ibm.com/granite/docs/models/granite4-0

## Adoption evidence and interpretation

Official HF card documents vLLM, SGLang and Docker Model Runner; popularity counters not captured Scope: IBM official model card/deployment documentation. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small

## Selection notes

**Strengths recorded:** 32B instruct model with enterprise-friendly commercial license; IBM supplies signed model artifacts and documented serving paths; structured chat and tool calling support.

**Limitations recorded:** 32B memory demand; quantization needed on modest hardware; IBM warns legacy docs are no longer updated; prefer HF/GitHub for latest; check exact context length in current model config before claiming a ceiling.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Sources

- https://huggingface.co/ibm-granite/granite-4.0-h-small
- https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized
- https://www.ibm.com/granite/docs/models/granite4-0

Fetched: 2026-10-16
