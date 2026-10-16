# Nemotron 3 Nano 30B A3B NVFP4

**Canonical checkpoint ID:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4`  
**Status:** available  
**Release:** 2025-12  
**Weight license:** NVIDIA Nemotron Open Model License

## Intended role and capability boundary

Nemotron 3 Nano 30B A3B NVFP4 is cataloged as open-weight, reasoning, agentic, small-MoE. The recorded task capabilities are reasoning, tool use, agentic tasks, text generation. This ID denotes the checkpoint listed in the catalog; don't silently substitute an API alias, a community merge, a base checkpoint, or a quantized derivative.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard

## Context and deployment constraints

Official card uses long-context tests; numeric usable maximum is unknown in inspected excerpts and should be checked against model config and serving stack.

NVFP4 requires compatible kernels/hardware and should not be conflated with BF16/FP8 quality or performance; official HF example uses trust_remote_code; review code and pin a revision before production; active parameter count does not equal total weight storage.

Treat the parameter label, quantization, or vendor context headline as insufficient evidence for a specific deployment's memory, throughput, or quality. Confirm the exact revision, tokenizer, chat template, serving-engine support, accelerator requirements, and modality preprocessing against the chosen runtime before rollout. No hardware or throughput guarantee is recorded here unless it appears in the official source above.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard, https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4

## Availability, license and cost

Availability recorded for this identity: Hugging Face, NVIDIA NIM/model catalog, Transformers, vLLM, SGLang, Docker Model Runner. The weight license is **NVIDIA Nemotron Open Model License**. Weight terms do not automatically cover serving code, datasets, tokenizer assets, training data, or separate API services. Review the license text and any gated-download terms before redistribution, commercial use, or derivative training.

Pricing: No hosted rate captured; self-hosted cost depends on compatible accelerator and quantized serving stack.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard, https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4, https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Adoption evidence and interpretation

Official Hugging Face card showed 190 likes and 12 community discussions at retrieval; modest but directly measurable platform signal. Scope: NVIDIA official HF quantized model card. Snapshot date: 2026-10-16. Treat this as the specifically named platform or provider signal; it is not a measure of unique users, production request volume, or model quality unless the source explicitly defines it that way.

> Source: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4

## Selection notes

**Strengths recorded:** 30B total / 3B active parameters balances capacity and active compute; NVFP4 quantized variant is a much smaller artifact than full precision; official HF card provides supported serving commands and license metadata.

**Limitations recorded:** NVFP4 requires compatible kernels/hardware and should not be conflated with BF16/FP8 quality or performance; official HF example uses trust_remote_code; review code and pin a revision before production; active parameter count does not equal total weight storage.

Start with a workload-specific evaluation. Pin the exact checkpoint revision and use representative prompt lengths, modalities, output formats and concurrency. Compare the selected weight artifact with alternatives under the same runtime and quality criteria. A hosted API price, where one is listed, is a provider service price and does not estimate self-hosted total cost.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Sources

- https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

Fetched: 2026-10-16
