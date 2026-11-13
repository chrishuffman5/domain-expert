---
name: phi
description: "Select Microsoft Phi open-weight checkpoints for compact text reasoning or multimodal local inference. Use for Phi-4, Phi-4 Multimodal Instruct, exact Microsoft checkpoint IDs, or MIT weight licensing. Do NOT use for AI fine-tuning/training, generic model API/SDK mechanics, agent harness/tool integration, inference routing, or evaluation infrastructure; use the `ai` skill. Do NOT use for Google Gemma, Meta Llama, Mistral, IBM Granite, or NVIDIA Nemotron; use their family skills."
license: MIT
---

# Microsoft Phi

This skill covers two selected downloadable Phi checkpoints: the text-only `microsoft/phi-4` and the multimodal `microsoft/Phi-4-multimodal-instruct`. Both are cataloged as MIT-licensed weight artifacts, but they have different modalities, limits, and input conventions.

## Select a Phi checkpoint

| Checkpoint | Best starting fit | Main boundary |
|---|---|---|
| `microsoft/phi-4` | Compact text reasoning, math, and code tasks | Text-only, 16K context |
| `microsoft/Phi-4-multimodal-instruct` | Compact experiments that need image and audio/speech pathways | Modality-specific formatting and context limits; numeric maximum unknown in this catalog |

Use Phi-4 when all inputs are text and the application can work within its documented 16K context. It is a 14B dense model with Microsoft-reported reasoning strengths, but benchmark statements are vendor evaluations and need independent task testing.

Use Phi-4 Multimodal Instruct when input includes supported images or audio and you need a compact downloadable model. It adds integration complexity and has task-specific modality conventions. Do not apply Phi-4's 16K text context to the multimodal checkpoint without checking its current card and pathway.

When the workload needs long context, sustained high-throughput production, a guaranteed hosted endpoint, or a modality not documented on the exact card, compare a different family. These selected checkpoints do not have catalogued official hosted token rates.

> Source: https://huggingface.co/microsoft/phi-4 ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct

## Phi-4 text model

The exact canonical ID is `microsoft/phi-4`. The model card describes a 14B dense text model with reasoning, mathematics, and coding capability. It has 16K tokens of context and no vision or audio input in this named variant.

This is a useful candidate when a relatively compact text model is preferred and tasks resemble its target reasoning, math, or code use. A short 16K context is a material constraint: reserve budget for instructions, conversation history, retrieved material, and output. Split or retrieve long documents deliberately rather than silently truncating them.

Microsoft's research report describes model performance and training decisions; treat benchmark results as vendor-reported evidence. Evaluate correctness on your domain, especially when tasks involve specialized terminology, long multi-step prompts, or external tool outputs.

The weight license is MIT. Preserve the exact repo revision and accompanying license, and check licenses for tokenizer, runtime, and dependencies separately. The model card asks developers to apply suitable safeguards for harmful content; integrate those controls into the application.

The model card showed 426,836 downloads in the last month at retrieval. This is a Hugging Face platform distribution count, not unique users, active deployments, or production requests. Use it as a dated adoption proxy only.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/

## Phi-4 Multimodal Instruct

The exact ID is `microsoft/Phi-4-multimodal-instruct`. It is a distinct instruction-tuned model combining language, vision, and speech/audio pathways. The official card and Microsoft report describe image and audio-related task conventions; inspect their current requirements for preprocessing, task markers, and input handling.

The catalog records its numeric context maximum as unknown because the inspected excerpts did not establish one. Do not borrow the 16K text Phi-4 value. Set application limits only after checking the current exact card/config and the selected runtime.

Multimodal requests can include hidden cost and memory from image encoders, audio features, frame sampling, and preprocessing. Their token accounting may differ from text-only prompts. Test each task path separately before combining modalities.

Use representative examples for image question answering, speech input, transcription or speech-related tasks as listed by the card. Verify which directions of audio are supported; “multimodal” does not imply every audio input and output task.

The model uses a task-specific format. Do not submit raw image or audio payloads as if the model accepted ordinary text alone. Use the documented multimodal data preparation and prompt tokens. Confirm that the runtime's model adapter recognizes the same format.

The selected weights are cataloged as MIT. Review the exact file license and any model-specific use guidance before redistribution or product deployment. The card showed 98 Hugging Face community Spaces at retrieval; this is an integration proxy, not usage volume.

> Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Deployment and validation

No universal memory minimum or throughput rate is recorded for either checkpoint. The actual requirements depend on precision, inference engine, hardware, context length, batch size, and modality preprocessing.

1. Pin the exact checkpoint ID and repository revision.
2. Read the model card for input formatting, tokenizer, supported tasks, and context details.
3. Confirm the chosen runtime supports the exact model and multimodal pathways.
4. Include preprocessing dependencies in the deployment plan.
5. Test realistic prompt and output lengths, not only short examples.
6. Measure text and each modality separately; then test mixed modality if the application needs it.
7. Compare quantized and original formats as distinct deployment artifacts and measure quality changes.
8. Validate refusals, unsafe requests, malformed payloads, and prompt-injection behavior.
9. For multimodal tasks, test missing/corrupt inputs and ensure the application handles failures safely.
10. Keep application code responsible for tool permissions, output parsing, and action confirmation.

For Phi-4 text tasks, compare on accuracy, response quality, and 16K context fit. For Phi-4 multimodal tasks, also compare modality quality and implementation complexity. Use a different candidate if important requirements fall outside the exact model's documented inputs.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## License, status and adoption

Both selected Phi artifacts are MIT-licensed according to their official model cards. This applies to those listed weight artifacts, not automatically to third-party runtimes, dependencies, or services. Preserve notices and verify the files in the exact pinned repository revision.

The catalog lists both as available. Phi-4's release date is 2024-12-12; Phi-4 Multimodal Instruct is 2025-02-26. These are dated identities and should not be collapsed into one generic “Phi-4” deployment record.

The Phi-4 download count is a dated Hugging Face metric. The multimodal card's 98 Spaces are a dated ecosystem integration signal. They have different measurement meanings and should not be treated as a direct popularity comparison. Neither is a direct measure of active users or model quality.

The family does not have an official hosted price captured in this catalog. Where a managed endpoint is used, verify provider-specific ID, context, price, and lifecycle on that provider's current documentation. Do not assume an endpoint is equivalent to local weights.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Workload comparison prompts

Use a small set of focused questions to decide whether a Phi model belongs in the shortlist:

- Is the complete input text, or does it include audio or images?
- Does the full prompt, retrieved content, conversation history, and output fit Phi-4's 16K limit?
- Is the target task math, code, or general reasoning, and can success be checked objectively?
- For multimodal input, which exact image/audio tasks does the application require?
- Does the serving engine implement the required input format?
- Is MIT weight licensing appropriate for the intended deployment, and what terms apply to the dependencies?
- Will the application use the weights locally or a managed endpoint with separately documented terms?

If all inputs are text and fit within a tested 16K budget, compare Phi-4. If image or audio is essential, compare Phi-4 Multimodal Instruct. If the numeric context limit of the multimodal variant is material, verify it before recommending it.

Do not claim that “Phi-4 supports vision/audio” without naming the multimodal checkpoint. The base text Phi-4 card explicitly represents a text model.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Test design for compact models

Small models can be efficient in some deployments, but “compact” does not define acceptable quality. Build a test set around the exact user task.

For math, include problems with known answers, unit changes, and ambiguous wording. For code, include short edits, bug fixes, tests, and repository-specific instructions. For general reasoning, include examples that require distinguishing evidence from assumptions.

For multimodal tasks, create separate groups for image and audio. Use representative file sizes and durations. Include visual text, poor image quality, background noise, multiple speakers, or other application conditions only if those occur in practice.

Score failures at the level that matters: answer correctness, task completion, schema validity, modality understanding, refusal, and safe fallback. Keep the model's output format and preprocessing stable so the comparison remains interpretable.

When a model is used to generate code or tool calls, make application checks independent of model assertions. Validate syntax, execute tests in a safe environment, and constrain tool permissions.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Context and modality accounting

Phi-4 text has a 16K token context. Include all system instructions, retrieved content, history, tool descriptions, and expected output in that budget. If the application sends a prompt near the limit, reserve capacity for response generation and runtime-specific special tokens.

The multimodal variant's numeric ceiling is unknown in this catalog. Different pathways can consume context differently, and model adapters can impose lower limits than the artifact. Check the current card and runtime.

Images and audio are not always counted like plain text. Preprocessing can create multiple crops, patches, frames, or audio features. Ask the exact runtime how it packages them and use the official model input format.

For videos, check whether the selected checkpoint actually supports video input through a documented pathway. Do not infer video support from image support alone.

For speech, distinguish audio input, speech transcription, and generated audio. The cataloged multimodal model should be used only for the tasks its official card documents. If audio output is required, confirm explicit support rather than assuming it from audio input.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Version and artifact integrity

Record whether a deployment uses `microsoft/phi-4` or `microsoft/Phi-4-multimodal-instruct`. These are separate canonical IDs and must not be collapsed in logs or model registries.

Pin an immutable repository revision, preserve the accompanying license and model card, and record tokenizer and processor versions. If a third party publishes a quantized or merged derivative, record that derivative's publisher and license separately.

When upgrading, run the same test set against old and new artifacts. Changes to the model, tokenizer, processor, prompt template, runtime, or precision can each alter the resulting behavior.

Do not treat hosted model listings as proof of local artifact equivalence. A cloud endpoint may apply extra system prompts, decoding settings, safeguards, or a different checkpoint.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Deployment risks and controls

For local deployment, test the exact precision and model-loading path on the target hardware. No universal VRAM or throughput figure is recorded here. Do not derive one from the 14B parameter count or from marketing descriptions.

For multimodal deployments, review processor dependencies and input-file handling. Validate file type, maximum size, duration, and preprocessing boundaries. Reject malformed inputs safely and avoid logging raw media when unnecessary.

For user-facing answers, include a fallback when the model returns incomplete or unsupported content. Avoid presenting an answer as verified merely because the model expresses certainty.

For sensitive tasks, confirm policy and privacy controls before sending user data to a managed endpoint. A local-weight path changes the hosting boundary but does not automatically remove all data exposure risks from logs, telemetry, or dependent services.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Common errors

| Error | Why it is wrong | Correction |
|---|---|---|
| Use Phi-4 for image input | Text Phi-4 is not the selected vision model | Choose and test Phi-4 Multimodal Instruct |
| Apply 16K context to the multimodal checkpoint | Catalog does not establish that ceiling for it | Verify exact card and runtime limit |
| Treat API availability as the same as local weights | Hosted endpoint may use distinct behavior and terms | Record the precise deployment identity |
| Infer output audio from audio input | Directionality is not implied | Verify explicit card support for the task |
| Claim quality from Microsoft benchmarks alone | Results may not reflect target data | Run task-specific evaluation |
| Call a download count active users | HF measures distribution events, not unique people | Label the metric and window |
| Assume every local runtime supports all modalities | Adapters and processors differ | Test the exact engine/version |

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Recommendation pattern

For a text-only math or code workload, recommend Phi-4 only when the task and context fit and the benchmark supports it. Mention the MIT weight license and the need to validate Microsoft's vendor evaluation on local examples.

For image/audio workloads, recommend a test of Phi-4 Multimodal Instruct only for explicitly documented pathways. Mention that the catalog's numeric context is unknown and that processor/runtime compatibility must be confirmed.

If a hard requirement cannot be resolved from official sources, state the uncertainty and propose an official source check or a small prototype before production adoption. Do not fill unknown values with a sibling model's data.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Selection handoff

The final recommendation should state whether the candidate is text-only or multimodal, the exact checkpoint ID, its verified or unknown context boundary, the selected weight license, and any price or adoption evidence limitations.

If the requester asks for a hosted product, identify the provider endpoint and its current API documentation separately. Keep this skill focused on downloadable Phi weights and do not assume the managed endpoint uses identical prompts or decoding behavior.

When Phi-4 fails a 16K requirement, choose a model with a verified larger context or change the application to retrieve and segment relevant content. Do not send oversized inputs and hope the runtime truncates them safely.

When Phi-4 Multimodal's processor or context behavior is unclear, first confirm official support for the task and then prototype with representative media. Record the processor version and preprocessing settings as part of the model identity used in evaluation.

For a security-sensitive deployment, review the model card, model-loading code, dependencies, input retention, and output handling. MIT weight terms do not settle security or privacy questions.

> Source: https://huggingface.co/microsoft/phi-4 ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Version references

- `references/versions/phi-4.md` documents the text model's exact ID, 16K context, MIT terms, hosted price unknown, and dated downloads proxy.
- `references/versions/phi-4-multimodal-instruct.md` documents the exact multimodal identity, unknown numeric maximum, task-format caveat, MIT terms, and Spaces proxy.

Use the existing `ai` skill for general model APIs, training, routing, or evaluation infrastructure.

## Operational readiness

Keep the text and multimodal checkpoints separate in model registries and monitoring. Display the exact ID to operators when diagnosing context or processor failures.

Record the revision and processor used for each multimodal test. Verify task directionality, input formatting, and accepted media boundaries before launch.

For text Phi-4, expose the 16K context boundary in application configuration and keep a safe truncation or retrieval policy.

For multimodal Phi-4, verify the numeric limit from the exact card and runtime before setting that configuration.

Check processor and tokenizer versions as part of an upgrade.

Keep the base text model and multimodal model in separate deployment records.

If users can supply media, validate file type and size before inference.

Report the checkpoint ID in incident and test records.

> Source: https://huggingface.co/microsoft/phi-4 ; https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/ ; https://huggingface.co/microsoft/Phi-4-multimodal-instruct ; https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

## Sources

- https://huggingface.co/microsoft/phi-4
- https://azure.microsoft.com/en-us/blog/phi-4-research-series-introductory-blog/
- https://huggingface.co/microsoft/Phi-4-multimodal-instruct
- https://azure.microsoft.com/en-us/blog/phi-4-multimodal-technical-report/

Fetched: 2026-10-16
