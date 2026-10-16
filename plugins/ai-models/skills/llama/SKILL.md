---
name: llama
description: "Choose Meta Llama open-weight checkpoints for self-hosted text or multimodal assistants, including Llama 4 Scout, Llama 4 Maverick, and Llama 3.3 70B Instruct. Use for Llama checkpoint IDs, Meta Community License terms, MoE tradeoffs, or Llama migration questions. Do NOT use for AI fine-tuning/training workflows, generic model API/SDK mechanics, agent harness/tool integration, inference routing, or evaluation infrastructure; use the `ai` skill. Do NOT use for Google Gemma, Mistral, IBM Granite, NVIDIA Nemotron, or Microsoft Phi; use their family skills."
license: MIT
---

# Meta Llama

Use this skill to compare the selected Llama checkpoints as downloadable weights. The catalog covers the multimodal Llama 4 Scout and Maverick releases and the text-only Llama 3.3 70B Instruct checkpoint. Model family membership does not make the model IDs or licenses interchangeable.

## Choose by workload and footprint

| Checkpoint | Choose it when | Main caveat |
|---|---|---|
| `meta-llama/Llama-4-Scout-17B-16E-Instruct` | Long-context or image understanding is central and you can serve a 109B-total MoE | Meta advertises up to 10M tokens, but runtime support, memory, and long-range quality need validation |
| `meta-llama/Llama-4-Maverick-17B-128E-Instruct` | General multimodal assistant quality matters and a much larger 400B-total MoE is operationally acceptable | 17B active parameters do not represent storage needs; check distributed serving capacity |
| `meta-llama/Llama-3.3-70B-Instruct` | You need a mature, text-only 70B baseline with 128K context and broad runtime support | Older generation, dense weight footprint, custom Llama license |

Use Scout when its long-context and image capabilities solve a real requirement. Its total expert weights matter even though only 17B parameters are active per token. Use Maverick when evaluation supports its general multimodal quality and the higher overall weight footprint is viable. Use Llama 3.3 when a mature ecosystem and text-only tasks are more important than newer image capabilities.

Do not select based only on Meta benchmark tables, active parameter counts, or advertised input ceiling. Compare exact quantized artifacts on representative prompts and serving hardware.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct

## Llama 4 Scout: long-context caveat

The exact selected checkpoint ID is `meta-llama/Llama-4-Scout-17B-16E-Instruct`. The repository is gated; access requires following the model host's access and license-acceptance process. The official card describes a 17B-active / 109B-total mixture-of-experts model with text and image input.

Meta advertises a 10M input-token ceiling. The official model card separately documents 256K pre- and post-training sequence length and long-context generalization experiments. Keep those facts distinct. The advertised ceiling does not guarantee that every serving engine accepts 10M tokens, that the KV cache fits available memory, or that retrieval remains reliable across the whole window.

Start with a lower limit appropriate to the runtime, then test retrieval at multiple positions across documents of realistic length. Measure prompt processing latency, memory, truncation, and quality. For long-context use, include distractors, repeated facts, and evidence near both ends of the input. Do not claim model quality at 10M from the context headline alone.

Scout has 16 experts and 17B active parameters, but the expert weights still contribute to the total artifact and storage burden. The active count describes per-token activation, not a complete memory estimate. Quantized formats and expert placement affect actual deployment.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Llama 4 Maverick: multimodal capacity

The selected ID is `meta-llama/Llama-4-Maverick-17B-128E-Instruct`. The official material describes a 17B-active / 400B-total model with 128 experts, image understanding, multilingual behavior, and a 128K context. Its 17B active parameter count must not be used as if the model were a 17B dense checkpoint.

Maverick suits a higher-capacity general multimodal assistant when the deployment can store and serve its expert weights. Confirm the engine's support for expert placement, image preprocessing, context limits, and the instruction template. Meta's launch material includes vendor deployment examples, but they are not transferable guarantees for every cloud or local environment.

Use a test set with both image and text-only prompts so that image performance and ordinary chat behavior are compared separately. Check OCR-like inputs, spatial or chart questions, multilingual image text, tool calls, and refusal behavior if those are part of your product.

If the selected deployment cannot support the total weight artifact, consider Scout or a different family based on task needs. Do not assume quantizing Maverick preserves the same behavior or quality.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Llama 3.3 70B Instruct: mature text baseline

The exact ID is `meta-llama/Llama-3.3-70B-Instruct`. It is a 70B dense instruction-tuned text model with a documented 128K context, multilingual chat and tool-use capability. It is not an image model and should not be selected for image understanding.

Use it as a baseline where a mature ecosystem, text generation, and support for common serving stacks are useful. The 70B dense footprint is substantial. Quantization may make local service feasible on more constrained systems, but changes numerical behavior and should be evaluated on the intended workload.

The model is still available and carries its own Llama 3.3 Community License. It is a different generation from Llama 4 and has distinct prompt and capability boundaries. When migrating to Llama 4, test the chat template, system instruction behavior, tool schema and output parsing. Do not assume a checkpoint replacement is behaviorally transparent.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## License and gated access

Llama 4 Scout and Maverick use Meta's Llama 4 Community License; Llama 3.3 70B uses the Llama 3.3 Community License. These are custom terms, not OSI-approved open-source licenses. Do not write “Apache”, “MIT”, “unrestricted open source”, or “commercial use is automatically allowed” for these weights.

- Accept and retain the exact license terms for the selected version.
- The Llama 4 Hugging Face repositories are gated; check account access before planning an offline deployment.
- Review attribution, redistribution, acceptable-use and scale-related conditions in the relevant license.
- Check whether a quantized or fine-tuned artifact carries additional terms from its publisher.
- Separate weight terms from engine, tokenizer, dataset, and hosted-service terms.
- Seek legal review for commercial redistribution or derivative models where terms affect the intended use.

Do not infer a license from “open-weight” or from the license of another Llama generation. The exact artifact and its release terms govern.

> Source: https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct

## Deployment sizing and validation

No universal minimum VRAM, tokens-per-second rate, or cost-per-request is recorded here. Those depend on checkpoint total weights, precision, runtime, concurrency, sequence length, batching, KV-cache strategy, and modality support.

1. Pin the official checkpoint revision and record tokenizer and config revisions.
2. Check the current serving engine's support for Llama 4 architecture and required model-code path.
3. Estimate artifact storage using actual file sizes and precision; do not estimate from active MoE parameters alone.
4. Include KV cache and image-encoder memory in the deployment budget.
5. Benchmark short, medium, and target-long contexts separately.
6. Measure image and text-only prompts independently where relevant.
7. Compare full precision and quantized artifacts only after documenting the exact quantizer and runtime.
8. Test tool-call formatting and application validation.
9. Evaluate language and domain performance; Meta's broad multilingual claim does not guarantee equal quality in each language.
10. Validate refusal and prompt-injection behavior as part of the application, not solely from a model card.

For long-context workloads, measure answer correctness as well as whether the backend accepts the input. For image tasks, include real application resolutions and image counts. Keep prompt/output budgets below the effective runtime limit.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Adoption and ecosystem signals

The selected Scout card showed 5.0M Hugging Face downloads and 700 likes in the dated source snapshot, a platform-specific family-card proxy rather than unique production users. The Llama 3.3 card/collection showed 266K downloads and 3.14K likes in the research snapshot. The Maverick card's inspected evidence identified integrations but did not capture a current download count; that value remains unknown.

Use these figures only as dated distribution or interest indicators. Hugging Face downloads may reflect repeated or automated downloads and do not measure active installations, user count, inference tokens, quality, or commercial use. Compare signals only when their scope and time window align.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Task-specific selection questions

For **document-heavy text tasks**, start by checking whether the target application truly needs Scout's advertised long input range. If the effective engine limit or quality target is much lower, compare a shorter-context model that is easier to operate.

For **image understanding**, separate image quality from text generation quality. Test real image resolutions, multiple images, and text rendered inside images. Confirm that the serving path includes the correct image processor and preserves its expected input format.

For **agentic tool use**, test tool selection, argument formatting, repeated calls, recovery after tool errors, and refusal to call unauthorized tools. The model produces proposed actions; the application authorizes and executes them.

For **multilingual work**, test the target language and domain directly. A general multilingual claim does not establish equal support across languages, dialects, writing systems, or specialized terminology.

For **cost control**, compare actual serving cost, not only active parameter count. Include weight storage, precision, accelerators, request length, output length, concurrency, and operations. A hosted API rate is not recorded for these selected downloadable identities.

For **commercial distribution**, evaluate the applicable Llama Community License before choosing any family checkpoint. A high download count or permissive-looking model card does not grant rights beyond the license.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Avoid false equivalence

The following pairs are not interchangeable without a migration test:

- Llama 4 Scout and Llama 4 Maverick differ substantially in total expert count and context profile.
- Llama 4 and Llama 3.3 differ in generation, image capability, architecture, and license version.
- A Hugging Face gated checkpoint and a hosted endpoint may differ in availability and lifecycle.
- An original precision checkpoint and a quantized derivative may differ in output quality and runtime requirements.
- An instruct-tuned checkpoint and its base model have different prompt and behavior expectations.
- A family-wide context headline and a runtime's supported context are not equivalent.

When a requester names “Llama 4” without Scout/Maverick, ask what task and resource constraint matters, then compare both. When they name only “Llama”, first distinguish local weights from an API-hosted service.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Operational validation plan

Before launch, assemble representative examples for each use case and keep a held-out set for final comparison. Include successful cases, ambiguous inputs, conflicting instructions, malformed images, long prompts, and attempts to elicit unauthorized actions.

For Scout, test effective context at target length and evidence retrieval across the input. For Maverick, test total-weight deployment and image behavior. For Llama 3.3, check whether its text-only path and 128K context meet the task without image support.

Record correctness, completeness, schema validity, refusal behavior, tool success, and resource behavior. Do not turn a single benchmark or a handful of examples into a universal quality claim.

Keep the test prompt template and decoding configuration fixed when comparing models. If the official recommended template differs across models, record the difference and treat it as part of the model's deployment interface rather than changing prompts ad hoc.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Common recommendation mistakes

| Mistake | Correction |
|---|---|
| Call Llama “open source” without qualification | State that these weights use custom Community Licenses |
| Size Scout from 17B active parameters | Account for 109B total expert weights and runtime state |
| Size Maverick from 17B active parameters | Account for 400B total weights and expert placement |
| Promise reliable 10M retrieval | Verify engine acceptance and task quality at that range |
| Apply Llama 3.3 terms to Llama 4 | Use the license for the exact release |
| Assume all Llama 4 endpoints expose the same functionality | Verify the exact serving provider and model identity |
| Treat image input as a text-only capability | Include image preprocessing and visual token budget |
| Compare HF downloads to live API tokens | Preserve measurement scope and don't manufacture a rank |

If a requirement is unknown, give a conditional recommendation. For example: “Scout is worth testing if the runtime supports the desired long input and the license fits; otherwise compare Llama 3.3 or another family against a shorter input budget.”

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Prompt and tool compatibility

The catalog identifies the selected artifacts as instruction-tuned checkpoints. Keep the official chat template paired with the corresponding model revision. Do not build one universal Llama prompt serializer and assume it produces identical behavior for 3.3 and Llama 4.

When using tools, include the exact tool schema in the test. Validate that calls are parsed correctly, the model can distinguish tool output from new user instructions, and the conversation can resume after a failed call. Keep side effects behind an application permission check.

Test a range of tool results, including empty results, malformed results, and results containing hostile text. A tool response can itself contain prompt injection; the application must preserve its trust boundary.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Long-input evaluation for Scout

Use a separate test set to determine whether Scout's long-context capability solves the actual retrieval problem. Include documents of multiple lengths, different evidence positions, distractor text, repeated names, and questions where the answer is absent.

Record the runtime-configured context limit and prompt length for each example. Score whether the answer is supported by the supplied document, not just whether it sounds plausible. Measure behavior at the start, middle, and end of the prompt.

If quality declines as inputs grow, choose a shorter prompt, retrieval, or chunked workflow. Do not keep raising the accepted context ceiling in order to hide quality degradation.

The 10M advertised value should always be reported with the official distinction that the card describes 256K pre/post-training and generalization experiments. State that runtime support and quality are subject to testing.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Deployment comparisons by dimension

Compare checkpoints using separate criteria instead of one overall scalar:

- task correctness on domain examples;
- text-only answer quality;
- image understanding when required;
- context retrieval and position sensitivity;
- tool-use validity and safe failure;
- effective prompt budget;
- weight storage and runtime memory;
- availability and gated access;
- license obligations;
- dated adoption evidence and its measurement scope.

This makes tradeoffs visible. A high-capacity model can be the wrong choice if it fails a required runtime, license, or latency constraint.

When uncertain, do not describe the model as “best.” Recommend a short comparative prototype with explicit pass criteria. Record why the final model was chosen, and retain the rejected candidates and reasons to make a future upgrade easier.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Reference map

- `references/versions/llama-4-scout-17b-16e-instruct.md`: exact Scout ID, release, gating, advertised versus documented context, and platform adoption proxy.
- `references/versions/llama-4-maverick-17b-128e-instruct.md`: exact Maverick ID, total/active parameters, modality, context, and access/license caveats.
- `references/versions/llama-3-3-70b-instruct.md`: exact older-generation text checkpoint and dated repository evidence.

Consult the version note before relying on limits or lifecycle details. For generic model APIs, inference routing, training, and evaluation systems, use the `ai` skill.

## Operational readiness

Keep gated access and license acceptance in provisioning documentation. Record who can download and redistribute the model.

For Scout, log prompt length and evidence position during long-context tests. For Maverick, record total weight placement and image pathway behavior. For Llama 3.3, identify that it is text-only in registries and user documentation.

Recheck the official model card and license before upgrading an artifact or sharing it with another organization.

> Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct ; https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct ; https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main ; https://huggingface.co/meta-llama/collections

## Sources

- https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct
- https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct-Original
- https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct
- https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct/blob/main/README.md
- https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
- https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/tree/main
- https://huggingface.co/meta-llama/collections

Fetched: 2026-10-16
