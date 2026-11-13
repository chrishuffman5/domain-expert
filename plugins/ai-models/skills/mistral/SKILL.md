---
name: mistral
description: "Select Mistral AI downloadable checkpoints across Large 3, Ministral 3, and Small 4 for open-weight general, vision, reasoning, or coding workloads. Use for exact Mistral Hugging Face IDs, Apache-2.0 model weights, Mistral family selection, or hosted-price versus self-host-cost comparisons. Do NOT use for AI fine-tuning/training, generic model API/SDK mechanics, agent harness/tool integration, inference routing, or evaluation infrastructure; use the `ai` skill. Do NOT use for Meta Llama, Google Gemma, IBM Granite, NVIDIA Nemotron, or Microsoft Phi; use their family skills."
license: MIT
---

# Mistral AI open-weight models

This family skill covers three selected Mistral checkpoint identities with different scale and capability profiles: Large 3, Ministral 3 14B, and Small 4. Their weight licenses are listed as Apache 2.0 in the catalog. The hosted Mistral API rates listed for some models are separate service prices; they do not price self-hosted use.

## Select by capacity and task

| Checkpoint | Role | Main deployment tradeoff |
|---|---|---|
| `mistralai/Mistral-Large-3-675B-Instruct-2512` | High-capacity general multimodal MoE, 41B active / 675B total | Large total expert artifact; Transformers support was not integrated on the card at publication; official card recommends vLLM |
| `mistralai/Ministral-3-14B-Instruct-2512` | Smaller general assistant with vision | Lower scale than Large 3, but 14B still requires meaningful memory, especially with long context and images |
| `mistralai/Mistral-Small-4-119B-2603` | General, reasoning, coding and image input in a hybrid MoE | 6.5B active / 119B total; lower active count does not remove expert-weight storage needs |

Start with Small 4 when one Mistral checkpoint must cover general instruction, reasoning, and code and the deployment can handle its total weights. Use Ministral 3 for a smaller vision-capable profile. Consider Large 3 for higher capacity only when its larger artifact, engine support, and evaluation outcomes justify it.

Do not choose solely from active parameter count. An MoE can activate fewer parameters per token while still requiring storage and distribution of its experts. Total memory also depends on precision, engine, KV cache, batch size, and prompt lengths.

> Source: https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512

## Mistral Large 3

The canonical checkpoint is `mistralai/Mistral-Large-3-675B-Instruct-2512`, an instruction-tuned 675B-total / 41B-active multimodal MoE. The selected card lists text and image understanding, multilingual tasks, and agentic instruction use. The recorded context is 256K, but the actual runtime limit and modality budget should be checked against the chosen engine.

The official Hugging Face card recommends vLLM and noted at publication that Transformers support was not yet integrated. Treat this as a time-bound compatibility statement: check current framework documentation before choosing an engine. Pin the tested version and do not assume support has appeared merely because a newer version exists.

The total weight size means Large 3 is intended for cluster-grade or otherwise high-capacity serving. The 41B active figure describes per-token activation, not full storage. No universal accelerator count or tokens-per-second claim is recorded here; establish them from the exact format, runtime and hardware you will use.

The selected FP8 instruction artifact is Apache 2.0. A base model, different precision, or community quantization is a separate artifact. Keep the exact repository path and revision in experiment records.

Mistral's hosted API page lists $0.50/M input, $0.05/M cached input, and $1.50/M output for this identity in the research snapshot. This is a provider-hosted service rate, subject to change. It does not estimate self-hosted hardware, power, support, or operations costs.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Ministral 3 14B

The exact selected checkpoint is `mistralai/Ministral-3-14B-Instruct-2512`. The catalog records text, vision, and general-assistant capability, with 256K context documented by Mistral. Runtime memory and visual input tokenization reduce the practical budget.

Use it when a smaller general-purpose Mistral checkpoint with image input is more appropriate than Large 3. It is still a 14B model; do not describe it as a zero-resource or mobile fit without testing the actual artifact and runtime.

Confirm that the chosen serving stack loads the model's vision pathway and applies the expected image preprocessing. Test whether one or many images fit within the needed context while preserving enough room for instructions and generated output.

The checkpoint is listed under Apache 2.0. The hosted Mistral API rate in the research snapshot is $0.20/M input, $0.02/M cached input, and $0.20/M output. Treat these as service prices for the corresponding API tier, not deployment estimates for local weights.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Mistral Small 4

The selected artifact is `mistralai/Mistral-Small-4-119B-2603`, an instruction-tuned hybrid MoE with 119B total and 6.5B active parameters. Mistral describes general instruction following, reasoning, coding, image input, and function calling. Its documented context is 256K; confirm the exact sequence length and memory behavior on the selected engine.

This model is a strong first Mistral choice when a workload needs more than basic chat and benefits from code, reasoning, images, or tools in one checkpoint. The total parameter count remains relevant to artifact storage and expert placement. It may exceed the capacity of a typical local workstation without a suitable quantized format or offload strategy; measure rather than assume.

The official model page and Hugging Face collection show a current release identity. The catalog snapshot reports 74.9K downloads and 452 likes on the main checkpoint listing. Downloads are Hugging Face distribution counts with platform-specific measurement behavior, not unique users or production calls.

The hosted API price in the research snapshot is $0.15/M input, $0.015/M cached input, and $0.60/M output. Keep the exact hosted tier, date, and cache distinction when using this figure. Price may change and does not establish any local inference cost.

> Source: https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Licenses, formats, and model identity

The three selected weight artifacts are cataloged as Apache 2.0. Check each repository's exact license file and any additional file-level terms before redistribution, commercial use, or derivation. Do not extend the Apache statement to hosted services, datasets, code, or a community artifact without checking its terms.

Quantization is a precision or packaging choice for model weights, not a new base model family. Record the canonical checkpoint ID plus quantizer, precision, and source repository. Quantized variants may have different quality, supported kernels, and license notices. They must not be counted as additional Mistral model identities in this catalog.

Keep model IDs distinct across Large 3, Ministral 3, and Small 4. A similar name, an API endpoint, or a current Mistral page does not establish that two entries share weights or behavior.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Validation before rollout

For each deployment, pin the checkpoint and engine and run a representative evaluation before selecting a production default.

- Check loading support, tokenizer, chat template, context limit, and output terminators.
- Test image preprocessing and model response separately from text-only interaction.
- Test tool call syntax, valid argument serialization, and safe application-side validation.
- Benchmark prompts in the actual context-length distribution, including long inputs and multimodal content.
- Measure memory and latency with the intended batch size and concurrency.
- Compare at least one alternative size or architecture using the same task and runtime.
- Verify behavior after quantization rather than assuming precision changes are invisible.
- Inspect framework release notes if the model card lists incomplete or changing support.

Don't use a provider benchmark as a substitute for application evaluation. Compare factuality, tool success, image understanding, code quality, latency, and cost using your own workload. Keep unsafe tool actions gated by application authorization.

This skill describes model selection and tradeoffs. Generic API credentials, SDK usage, inference routing, training, and evaluation infrastructure belong to the existing `ai` skill.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Adoption evidence and limitations

The catalog records public evidence with its scope rather than a global ranking. Mistral Small 4's dated Hugging Face downloads and likes are distribution/interest proxies. Large 3's official repository shows community presence but no direct production usage count. Ministral 3's inspected official card did not expose a precise download count.

Do not infer that a model is widely deployed from its presence in an official catalog or compatibility list. Likewise, don't compare these platform counts directly with API token usage, enterprise customer counts, or another model's counters without aligned windows and definitions.

Check the latest official status before new deployment. Lifecycle pages can change, and public previews, hosted endpoints, deprecated models, and downloadable weights have separate availability states. A hosted API remains a separate product even if it serves related weights.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Matching model to workload

Use a workload-first comparison rather than a winner-takes-all family ranking.

- **General assistant with tool use:** include Small 4 if the 119B total artifact is feasible. Test tool-call format and reliability on your agent loop.
- **Code and reasoning in one checkpoint:** include Small 4 because the official card lists both; verify code quality on your own language and repository tasks.
- **Image input with a smaller selected model:** include Ministral 3 14B, subject to the chosen engine supporting its vision path.
- **Higher-capacity multimodal use:** include Large 3 only if its 675B total weight storage and documented runtime path fit the deployment.
- **Low-cost hosted inference:** compare the dated API rates, cache rules, and output price, while keeping these distinct from self-hosted model costs.
- **Commercial redistribution:** the selected weights are Apache 2.0, subject to each artifact's exact files and third-party dependencies.
- **Consumer workstation deployment:** test Ministral first, but confirm actual memory and context requirements rather than assuming the label guarantees fit.

No family recommendation should claim a fixed memory minimum from the listed parameter counts alone. An accelerator's usable memory, weight format, KV cache, batch size, and runtime are all material.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Price and deployment are separate decisions

The catalog captures official API pricing for the selected Mistral identities at a snapshot date. These prices describe provider-hosted calls, not downloadable-weight execution. They can change independently of model availability and do not include a self-hosted operator's costs.

If the requester compares an API with local weights, break the comparison into:

- API input and output rates for the region and service tier;
- cached-input discount and any cache eligibility rules;
- tokenization and modality accounting;
- expected input/output distribution and concurrency;
- local accelerator purchase or rental cost;
- weight storage, networking, memory, and utilization;
- operations, monitoring, upgrades, and support;
- data residency and retention requirements.

Do not promise that local serving is cheaper based only on rate-card comparison. Conversely, do not compare only the token price while ignoring control or data-locality needs.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Lifecycle distinctions

At the 2026-10-16 snapshot, Large 3 and Ministral 3 14B are available selected open-weight artifacts; Small 4 is the current selected hybrid checkpoint. Check the official Mistral model page before a new deployment because status, framework support, and previews can change.

A retired or deprecated hosted API is not necessarily the same thing as a downloadable checkpoint's lifecycle. Likewise, a public preview is not equivalent to a generally available weight artifact. Verify exact distribution and endpoint independently.

Do not revive older models just because an endpoint remains callable. Confirm ongoing support and available evidence before suggesting them for a new system. If a model is pinned for compatibility, explain that it is a legacy maintenance choice.

> Source: https://docs.mistral.ai/models ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03

## Model evaluation dimensions

Compare models with task examples that exercise the capability used in production. A general chat benchmark may not predict code completion, document extraction, image reasoning, or tool-call reliability.

For text, score factual support, instruction adherence, language and output format. For code, use representative repository tasks and check edits, tests, and regression risk. For images, verify the model can read the relevant visual content and that the adapter passes it correctly. For tools, score both the decision to call and the arguments returned.

Measure resource use at the intended context distribution. A 256K context headline does not tell you how much memory, latency, or quality loss occurs at a particular prompt length. Test shorter and longer cases instead of quoting the maximum as a recommended setting.

For Small 4, include both reasoning and non-reasoning tasks if your application uses both. For Large 3, include the exact image workload and verify engine maturity. For Ministral, test whether the smaller checkpoint retains sufficient quality for the target task.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Common pitfalls

| Pitfall | Why it matters | Action |
|---|---|---|
| Treat active MoE parameters as total memory | Experts still occupy weight storage | Check artifact size and runtime memory |
| Treat all three checkpoints as one family alias | Architecture and scale differ | Pin the exact canonical ID |
| Assume Transformers support from other Mistral models | Model support may be incomplete or change over time | Check the exact current model card and engine docs |
| Assume vision works in every serving stack | Vision adapters and preprocessing differ | Verify and test the selected pathway |
| Apply hosted token prices to local weights | The cost basis is different | Compare the full deployment model |
| Assume Apache 2.0 covers dependencies | Runtime and packaged files may have other licenses | Review the full artifact and dependency terms |
| Treat HF downloads as active usage | Counts are platform-specific and repeatable | Label the platform metric and date |

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Recommendation format

A concise model recommendation should name the exact checkpoint, why it fits, what constraint may disqualify it, the applicable license, and the evaluation still needed. Keep hosted price separate from local inference cost. If a requirement depends on a missing numeric limit or runtime capability, state what must be checked before rollout.

An example structure:

1. **Candidate:** exact repository ID and revision.
2. **Fit:** relevant task or modality from the official card.
3. **Tradeoff:** total weights, context behavior, engine support, or license.
4. **Price:** hosted rate if relevant; otherwise unknown.
5. **Validation:** concrete prompt set or runtime check.

Do not call any selected family member “the best Mistral” without naming the task and deployment context. The family contains distinct scale points and the catalog includes no universal quality ranking.

For image workflows, include the image processor and selected resolution in the experiment record. For language tasks, identify the languages tested. For tool use, retain the exact schema and parser configuration. These details help explain failures that are otherwise mistakenly attributed to model quality alone.

If a selected engine does not support the checkpoint, either verify another official deployment path or choose a different model. Do not claim support because the engine can load a related Mistral version.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Version references

- `references/versions/mistral-large-3-675b-instruct-2512.md` contains the exact Large 3 artifact, 256K caveat, API rate, and runtime-support notes.
- `references/versions/ministral-3-14b-instruct-2512.md` contains the exact Ministral 3 identity, vision and context notes, and hosted price.
- `references/versions/mistral-small-4-119b-2603.md` contains Small 4 architecture, capabilities, adoption evidence, and hosted prices.

Read the corresponding version note before claiming an exact price, release, or deployment constraint.

## Operational readiness

Maintain separate deployment records for Large 3, Ministral 3, and Small 4. Keep each model's exact API rate separate from the self-hosted weight artifact.

Before an engine upgrade, verify support for the selected checkpoint and run a small smoke test with expected prompts, image inputs, and tool calls.

Recheck official prices before a procurement comparison. These rates are date-sensitive service data.

Document whether a quoted rate is hosted or self-managed.

Do not treat the active expert count as a memory estimate.

> Source: https://docs.mistral.ai/models ; https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512 ; https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/models/mistral-large-3-25-12 ; https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 ; https://docs.mistral.ai/models/ministral-3-14b-25-12 ; https://docs.mistral.ai/models/mistral-small-4-0-26-03 ; https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 ; https://huggingface.co/collections/mistralai/mistral-small-4 ; https://docs.mistral.ai/inference/pricing

## Sources

- https://docs.mistral.ai/models
- https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512
- https://docs.mistral.ai/resources/known-limitations
- https://docs.mistral.ai/models/mistral-large-3-25-12
- https://docs.mistral.ai/models
- https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512
- https://docs.mistral.ai/models/ministral-3-14b-25-12
- https://docs.mistral.ai/models/mistral-small-4-0-26-03
- https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
- https://huggingface.co/collections/mistralai/mistral-small-4
- https://docs.mistral.ai/inference/pricing

Fetched: 2026-10-16
