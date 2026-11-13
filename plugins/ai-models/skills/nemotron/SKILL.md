---
name: nemotron
description: "Evaluate NVIDIA Nemotron open-weight models for agentic, reasoning, or NVIDIA-stack deployment, including the selected Nemotron 3 Nano NVFP4 checkpoint. Use for exact Nemotron IDs, NVFP4 caveats, NVIDIA Nemotron Open Model License, or model-card-supported serving guidance. Do NOT use for AI fine-tuning/training, generic model API/SDK mechanics, agent harness/tool integration, inference routing, or evaluation infrastructure; use the `ai` skill. Do NOT use for Gemma, Llama, Mistral, Granite, or Phi models; use their family skills."
license: MIT
---

# NVIDIA Nemotron

This skill covers the catalogued `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4` artifact. The catalog selects a single quantized precision variant. Its exact suffix matters: NVFP4 is not an alias for BF16, FP8, another checkpoint, or a hosted NVIDIA service.

## When to evaluate Nemotron 3 Nano

Consider this checkpoint for text generation, reasoning, tool use, or agentic workflows when you want downloadable weights and can use a compatible NVIDIA-serving path. The model has 30B total parameters and 3B active parameters according to the cataloged model card. Use the active count only as an architectural clue; it does not tell you total artifact storage or a universal memory requirement.

The selected NVFP4 artifact may be useful where its supported low-precision deployment path aligns with the target runtime. Validate kernel and accelerator compatibility from current official instructions before planning capacity. Do not infer hardware support simply from the NVFP4 name or a community conversion.

Choose a different precision artifact only after checking its exact ID, model card, weight terms, and expected quality. The official FP8 card is a comparison reference; it is not the catalog's selected Nano ID. Quantized formats can change numerical behavior and require separate evaluation.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4

## Identity and version boundaries

The canonical selected ID is `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4`. Preserve exact capitalization and the NVFP4 suffix when describing or loading the artifact.

The catalog records status as available and release month as 2025-12. It does not record a numeric usable context limit because the inspected excerpts were insufficient to verify one. Keep the limit unknown unless the pinned card and config for this exact artifact provide it.

The model card discusses long-context tests. That is not itself a numeric maximum or a guarantee that every serving stack accepts the same length. Read the exact config and engine documentation before setting prompt budgets. Test quality at the intended length.

Do not transfer a context figure from another Nemotron release or precision variant without a source that explicitly connects it to this model. Likewise, do not claim that an NVIDIA hosted endpoint's availability or price applies to downloadable weights.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## What NVFP4 means for deployment

NVFP4 is a specific quantized weight format. Quantization can reduce weight representation size, but actual deployment depends on supported hardware, kernels, model-loading code, and runtime versions. This catalog does not establish a minimum GPU, memory floor, or tokens-per-second guarantee.

Before adopting the artifact:

- confirm NVFP4 support in the intended runtime and accelerator generation;
- pin the exact Hugging Face repository revision and inspect its config and file metadata;
- identify required CUDA, driver, and serving-engine compatibility from current vendor documentation;
- review any custom loading code before running it;
- compare the NVFP4 variant against an official higher-precision artifact on representative prompts;
- measure memory, latency, output quality, and stability under the required context lengths;
- test batch size and concurrency using your target serving topology.

The official Nano card includes a Transformers example that requests `trust_remote_code`. Review that code, pin its revision, and assess the security implications before enabling remote code in a production environment. Avoid running model repository code with broader permissions than required.

If a candidate cannot satisfy exact precision support, select a verified supported model or precision. Do not quietly substitute an FP8 artifact under the NVFP4 ID.

> Source: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## License and safe use

The catalog records the selected weights under the NVIDIA Nemotron Open Model License. Review the license file at the exact repository revision before commercial deployment, redistribution, or model modification. Do not replace the model-specific terms with a generic “NVIDIA open model” assumption.

Keep weight rights distinct from the serving runtime, CUDA libraries, containers, tokenizer, and any externally supplied training or evaluation data. Verify those licenses and security policies independently.

For tool use, the model can suggest a tool name and arguments; the application remains responsible for authorization, schema checking, argument bounds, and side-effect confirmation. Do not let a model response execute privileged actions by itself.

Model-card safety language and benchmark scores do not guarantee safe behavior in a new application. Evaluate prompt injection, data exfiltration attempts, harmful requests, and malformed tool calls using the actual system context. Use deterministic checks and human review for high-impact actions.

> Source: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4

## Capability fit and limits

NVIDIA describes Nemotron 3 Nano as a reasoning and agentic model. The selected catalog record lists reasoning, tool use, agentic tasks, and text generation. These are selection cues; they do not provide a guaranteed score on your domain workload.

Good evaluation tasks include multi-step text instructions, tool selection with constrained schemas, structured extraction, and realistic agent state. Compare outputs at the same decoding and context settings. Score not only task success but invalid tool calls, unsupported claims, refusal behavior, and latency.

The catalog has no official hosted API price for this weight artifact. Self-hosted total cost depends on hardware, power, quantization, memory utilization, staffing, and runtime. Do not invent a token price from a hosted service listing or calculate one from parameter count alone.

Numeric context and adoption remain explicit evidence gaps. The recorded 190 likes and 12 discussions on the official NVFP4 Hugging Face card at retrieval are small platform interest/community signals, not active usage volume. No usage or download count was established in this snapshot.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Choosing a fair comparison

Compare Nemotron Nano with models intended for the same task and deployment type. A parameter count or benchmark score alone cannot establish a useful choice.

- For reasoning tasks, use questions with objectively checkable answers and keep hidden or held-out examples.
- For agents, measure tool selection, argument correctness, completion rate, retries, and invalid calls.
- For extraction, score field-level correctness, missing values, and output schema validity.
- For long prompts, validate runtime acceptance and retrieval quality at actual prompt positions.
- For local service, measure the selected precision on the exact accelerator and engine.
- For hosted service comparison, verify that the endpoint serves the same model identity and record its own price and limits.

If one candidate is quantized and another is full precision, document that difference. Either compare equivalent precision or treat the precision as a real deployment choice and report its quality/resource effect separately.

Do not infer an advantage from the “Nano” label. The selected model's 30B total size and 3B active size describe different aspects of an MoE. Decide from actual file sizes, memory use, supported serving kernels, and application results.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Hardware and software evidence

This catalog does not contain a verified minimum GPU specification for the selected NVFP4 artifact. Avoid statements such as “runs on one X GPU” unless a current official source identifies the exact weight format, runtime, context, and conditions.

Use the official model card and current serving guidance to answer:

- which accelerator and compute capability are supported;
- which libraries and versions load the artifact;
- whether special kernels or model code are required;
- whether `trust_remote_code` is used;
- whether the card demonstrates a local command, container, or managed endpoint;
- how the model config sets context length and precision;
- what tokenizer and prompt template are expected.

The answer can differ between NVFP4 and FP8. Verify both separately if you evaluate both. The FP8 artifact is a comparison checkpoint, not a drop-in substitute under the NVFP4 name.

Before production, pin package versions and model revisions. Record any custom repository code, container, driver, and runtime flags. Review security updates before refreshing the artifact.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Quantized artifact handling

Use the complete canonical name wherever the selected variant appears in documentation or automation. Preserve the source repository and revision.

For a quantized checkpoint, confirm:

- the publisher and provenance of the quantized artifact;
- whether the quantization is official or third-party;
- license terms and notices shipped with the artifact;
- required hardware and kernels;
- compatibility with the intended inference engine;
- whether calibration data or code is included;
- measured quality changes on target tasks;
- reproducibility across supported runtime versions.

Do not call precision suffixes aliases. Do not merge quantized and full-precision weight files as separate base model identities in the catalog. The suffix is still important for loading and deployment safety.

If a deployment path fails, do not automatically switch to another precision. Resolve the support mismatch or select an explicitly evaluated alternative and update the deployment record.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Safety for agentic use

An agentic model's suggestions are untrusted inputs until validated by the application. A model card that lists tool use does not grant it access to a shell, cloud account, database, or user data.

- Allowlist available tools and actions.
- Validate arguments with strict schemas and bounded values.
- Apply user and tenant authorization outside the model.
- Require confirmation for irreversible or high-impact actions.
- Keep secrets out of prompts unless necessary and authorized.
- Log model revision and tool outcomes without storing sensitive content unnecessarily.
- Apply deterministic checks to outputs that update systems or make consequential decisions.
- Route uncertainty or policy-sensitive actions to human review.

Test prompt injection from user text, retrieved documents, and tool outputs. The model should not decide its own permission scope. Do not deploy privileged tool execution solely because a benchmark reports agentic performance.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4

## Decision record for adoption

The current catalog records 190 card likes and 12 discussions on the selected official Hugging Face NVFP4 card as of 2026-10-16. These are visible community-interest signals. They do not establish download volume, active installations, production use, or model quality.

No comparable public per-model inference volume was captured. Keep adoption marked as this card-level signal, not “widely adopted.” If updated counts become available, record the date and preserve the same scope. Avoid comparing likes or discussions with Hugging Face downloads or API tokens as a single number.

The official card lists documented serving implementations and supplies commands. Compatibility is a practical availability signal, but is not a popularity measure.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Questions for an operator

Before approving a Nemotron Nano deployment, answer these questions in the architecture record:

1. Is the NVFP4 precision specifically required or merely a default assumption?
2. Which exact hardware and runtime combination has been tested?
3. What current official source confirms support for that combination?
4. What is the verified context maximum on the pinned model and runtime?
5. How much memory is used at the expected prompt and concurrency levels?
6. What change in quality appears versus a higher-precision checkpoint?
7. Which license and code review conditions apply?
8. What application permission checks constrain tool use?
9. How are unsupported outputs or runtime failures handled?
10. What evidence supports adoption claims, and what is still unknown?

If the first four questions cannot be answered, describe the deployment as a test candidate, not a ready-to-run recommendation. This avoids overclaiming support from a model name or a broad NVIDIA ecosystem reference.

Review any official card revision or container update for changes to loading code, precision handling, and supported model configuration before refreshing a production deployment.

When presenting a recommendation, distinguish what the official card states from what your team has measured. Include the checked date so operators know when to revalidate a changing runtime path.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Deployment decision sequence

1. Confirm that the target is the exact NVFP4 artifact and not a similarly named checkpoint.
2. Verify the model license and access conditions.
3. Confirm that the serving software and accelerator support the chosen precision.
4. Review code and configuration changes required to load the official artifact.
5. Determine context from the exact pinned config and validate the chosen engine's limit.
6. Estimate memory from actual weight files, KV cache, runtime buffers, and concurrency.
7. Run task-specific evaluation against a supported higher-precision or alternate model.
8. Test tool use with application-side validation and permission checks.
9. Record runtime, hardware, precision, and prompt settings for reproducibility.
10. Recheck the official card before changing precision or deploying a new revision.

For generic endpoint selection, routing, client retries, training, or evaluation harness construction, use the existing `ai` skill. This family skill is about the model artifact and its selection tradeoffs.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Version note

Load `references/versions/nvidia-nemotron-3-nano-30b-a3b-nvfp4.md` before using the selected model's exact license, status, release month, context unknown, deployment source, or adoption signal. The note lists all cataloged source URLs.

## Operational readiness

Keep the selected NVFP4 model ID attached to the configuration and confirm each environment loads that same precision. Record checked hardware, runtime, model revision, and context cap.

For agent use, validate untrusted output before execution and give the model only the minimum tool access required. Revisit support when updating drivers or inference software.

Log unsupported requests and fallback behavior so operators can see where the model is not a suitable fit.

Treat each precision change as a separate validation step.

> Source: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

## Sources

- https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8

Fetched: 2026-10-16
