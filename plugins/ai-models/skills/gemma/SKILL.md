---
name: gemma
description: "Select Google Gemma open-weight checkpoints for local, edge, or self-managed multimodal inference. Use for Gemma 3, Gemma 3n, Gemma 4, Gemma checkpoint IDs, Google weight licenses, or choosing among Gemma sizes and modalities. Do NOT use for hosted Gemini API models, AI fine-tuning or training workflows, generic model APIs/SDKs, agent harness/tool integration, inference routing, or evaluation infrastructure; use the `ai` skill for those tasks. Do NOT use for Meta Llama, Mistral, IBM Granite, NVIDIA Nemotron, or Microsoft Phi; use their family skills."
license: MIT
---

# Google Gemma

Use this skill to choose among the catalogued Gemma checkpoints and understand their documented input modalities, model terms, context caveats, and deployment tradeoffs. Gemma is downloadable-weight model family; the Google-hosted Gemini API is a separate product family. A matching family name does not make their identifiers, prices, limits, or terms interchangeable.

## Start with the deployment requirement

Ask which constraint is binding before recommending a checkpoint:

- **Small device and audio/video input:** start with `google/gemma-3n-E4B-it`. It is the selected on-device oriented checkpoint and supports text, images, audio, and video under a 32K input budget.
- **General vision at moderate scale:** compare `google/gemma-3-12b-it` with the 27B sibling. Both have 128K documented context and image input; the 12B variant is the smaller option.
- **More capacity with Gemma 3:** use `google/gemma-3-27b-it` when the workload benefits from a larger dense model and deployment resources permit it.
- **Newest selected general model:** evaluate `google/gemma-4-31B-it` for configurable thinking, image/video understanding, coding, and native function calling. Its 256K context is variant-specific; this 31B checkpoint does not support audio.
- **Commercial-use simplicity:** among these selected checkpoints, Gemma 4 lists Apache 2.0. Gemma 3 and 3n are governed by Google's separate Gemma Terms of Use and prohibited-use policy. Review current terms before deciding.
- **Price:** the catalog contains no official hosted API rate for these downloadable checkpoint identities. Compare actual hosting or self-hosting costs for the deployment you plan to operate.

Do not select from the family label alone. The generation and size determine context, modalities, prompt conventions, and license.

| Selected checkpoint | Useful starting point | Main constraint |
|---|---|---|
| `google/gemma-3-12b-it` | Compact general text and image instruction | Custom Gemma terms; 128K is a ceiling, not a quality guarantee |
| `google/gemma-3-27b-it` | Larger Gemma 3 general model with image input | More deployment resources than 12B; same custom terms |
| `google/gemma-3n-E4B-it` | Compact multimodal/on-device experiments | 32K input; per-modality preprocessing and runtime support |
| `google/gemma-4-31B-it` | Current 31B general, reasoning, code and image/video checkpoint | Dense 31B footprint; no audio on this variant; distinct prompt format and Apache terms |

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://ai.google.dev/gemma/docs/core/model_card_4

## Keep the releases separate

### Gemma 3 12B and 27B IT

The selected Gemma 3 checkpoints are instruction-tuned text-and-image models. They are two different checkpoint IDs, not aliases. Both are documented with 128K input context; do not project that value onto every Gemma 3 size. The official family card reports narrower context for smaller releases outside the selected 12B/27B pair.

Use the 12B artifact when local capacity is constrained and task quality is sufficient. Use 27B when a representative evaluation shows the extra model capacity improves the workload enough to justify its larger deployment footprint. Do not assume the larger model always wins for latency, factual accuracy, or a specific domain.

Image input uses image preprocessing and visual tokens. Image resolution and serving implementation affect the context budget. Keep image batches, prompt text, and generated output within the actual runtime's limit. For a text-only workload, do not pay an operational cost for a vision path you do not need.

The cards and availability paths require acceptance of Google's Gemma terms. Preserve the official model ID and the instruction-tuned `it` designation when downloading. A base checkpoint, community fine-tune, or quantized derivative is a distinct artifact and can change license obligations, behavior, or chat formatting.

### Gemma 3n E4B IT

`google/gemma-3n-E4B-it` is a compact multimodal checkpoint selected for on-device and edge scenarios. It supports text, images, audio, and video according to its model card. The per-layer embedding architecture means the E4B label is not a direct statement of total stored parameter count or resident memory.

The documented input context is 32K. The card describes image tokenization at supported 256, 512, and 768 resolutions and audio at 6.25 tokens per second. These modality conversions consume the same finite prompt budget. A prompt containing audio, frames, and instructions can therefore hit the cap sooner than a short text-only message.

Use a modality-specific smoke test before production: verify audio sampling and chunking, video frame extraction, image resolution behavior, timestamps if relevant, and output format. Do not infer that all runtime backends expose identical audio/video pathways just because the checkpoint card lists them.

### Gemma 4 31B IT

`google/gemma-4-31B-it` is the selected dense 31B Gemma 4 instruction checkpoint. The family includes other sizes and architectures, but those identities are not aliases for this selected model. Its card lists configurable thinking, text and image input, video understanding, coding, function calling, and broad language coverage.

The 31B checkpoint has a documented 256K context. Visual inputs consume context through their token representation, so maximum video frames or image sizes reduce room for text and output. The 31B variant is not an audio-input model; choose another explicitly audio-capable Gemma artifact if that is a requirement.

Gemma 4 introduces native `system` role support and a different prompt convention from Gemma 3. Test system-message behavior, tool schemas, stop markers, and structured output when upgrading. Do not simply replace a Gemma 3 checkpoint while retaining an unverified template.

The selected 31B model is listed under Apache 2.0 in its official card. Keep this license boundary specific to Gemma 4; it does not convert Gemma 3 or Gemma 3n terms to Apache 2.0.

> Source: https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/google/gemma-4-31B-it

## Weight terms and artifact hygiene

Open weights describe an access and distribution model. They do not mean every use is unrestricted or that the training corpus, runtime code, trademarks, and hosted Gemini services have the same terms.

- Gemma 3 and Gemma 3n: apply Google's Gemma Terms of Use and prohibited-use policy.
- Gemma 4 31B: cataloged as Apache 2.0 for the selected weight artifact.
- Hugging Face downloads can be gated on account acceptance. Confirm access before planning an offline deployment.
- Retain the exact repository ID, revision or commit, tokenizer, and model configuration in deployment records.
- Check whether a community quantization or fine-tune adds or changes obligations. The upstream license does not automatically settle downstream artifact terms.
- For redistribution, commercial products, model derivatives, or regulated use, review the applicable legal terms rather than relying on a short license label.

Google's model pages and the checkpoint card are the source for the listed variant's terms. If a card or terms page changes, recheck it before release.

> Source: https://ai.google.dev/gemma/terms/ ; https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/docs/core/model_card_4

## Practical deployment checks

Before choosing hardware or serving software, verify support for the exact checkpoint and precision. No universal hardware minimum or throughput figure is recorded here because the cataloged official pages do not give a deployment-neutral guarantee.

1. Pin the exact model repository and revision. Check the model config for parameter dimensions, tokenizer, sequence limit, and modality components.
2. Confirm that the selected inference engine supports the checkpoint generation, chat template, vision pathway, and any audio/video preprocessing you need.
3. Estimate memory from actual weight precision plus runtime buffers and KV cache. Longer context and larger visual prompts increase memory demand.
4. Treat quantization as a deployment variant, not a new model family. Record bit width, quantizer, calibration method, runtime kernels, and any measured quality change.
5. Test the same prompt and output schema across at least one alternative size or family when the decision is consequential.
6. Measure representative input lengths, modality mix, output lengths, concurrency, and tail latency on your own stack.
7. Check refusal, unsafe-request handling, language quality, and prompt-injection behavior in the application context.
8. Maintain a fallback path for prompts that exceed the chosen context or modalities, rather than silently truncating important content.

Image and video input require preprocessing. Audio support depends on model variant and backend. A family card's capability statement is not an assurance that a library or hardware target has implemented every path.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/google/gemma-3-27b-it ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://huggingface.co/google/gemma-3n-E4B-it

## Upgrade and compatibility guidance

Treat each generation change as a model migration. Compare outputs using a task set representative of your own prompts. Check conversation templates, special tokens, system role behavior, function-call structure, refusal behavior, and output termination before changing model IDs.

When comparing Gemma 3 with Gemma 4, include examples that use system instructions and tool calls. When comparing Gemma 3n to a text/image checkpoint, include the relevant audio or video paths and measure whether modality processing fits inside 32K. When switching between 12B and 27B, test memory and response quality on the same runtime settings.

Do not treat Hugging Face download totals as unique users or production requests. At retrieval, Google’s Gemma 4 collection displayed 9.18M downloads and 4.13K likes for the 31B IT checkpoint. This is a platform-specific distribution proxy with a platform-defined window; it can include repeated downloads and should not be compared directly with API token traffic. The Gemma 3n card displayed 100 Spaces using the model, also an ecosystem integration proxy rather than usage volume. The selected Gemma 3 12B and 27B records retain unknown variant-level usage counts.

These adoption signals help establish ecosystem availability. They do not establish quality, active deployment, or a ranking among all open-weight models.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/google/gemma-3-27b-it ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://huggingface.co/google/gemma-3n-E4B-it

## Workload-oriented comparison

Use this comparison to narrow candidates before testing them. It is not a universal quality ranking.

- **Image Q&A with moderate prompt size:** compare Gemma 3 12B and Gemma 3 27B using the same images, resolution, and question set.
- **Large image/video understanding:** compare Gemma 4 31B only if its 31B deployment and visual token budgets are practical.
- **On-device audio/video prototypes:** evaluate Gemma 3n E4B; include actual audio duration and video frame extraction in the input budget.
- **Text-only extraction:** compare Gemma 3 12B with Gemma 4 31B using exact schema and error criteria; avoid paying for modality processing you do not use.
- **Tool-using assistants:** Gemma 4's documented native function calling is a reason to test it, not evidence that calls will always be valid or safe.
- **License-sensitive redistribution:** assess Gemma 4's Apache 2.0 terms separately from Gemma 3/3n's custom terms.
- **Long document processing:** use retrieval or chunking if a model's actual context support cannot meet quality and memory needs.

For each comparison, keep the tokenizer, prompt template, decoding settings, examples, and output parser aligned. Record which model revision and runtime produced each result. If the runtime only supports one generation, do not compare a model from a different generation as if the stack were equivalent.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/google/gemma-3-27b-it ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://huggingface.co/google/gemma-3n-E4B-it

## Common selection errors

| Error | Why it causes trouble | Safer choice |
|---|---|---|
| Treat every Gemma checkpoint as 128K | Gemma 3 sizes and Gemma 3n have different limits | Check the exact card and config |
| Treat Gemma 3n E4B as a conventional 4B dense model | Per-layer embeddings alter the relationship between label and storage | Measure actual artifact size and runtime memory |
| Assume Gemma 4 31B accepts audio | Audio capability is size-specific; it is not listed for this variant | Use only modalities the exact card documents |
| Treat 10M or 256K as a guaranteed accurate window | Context acceptance does not prove retrieval quality | Evaluate realistic long prompts and position sensitivity |
| Carry custom terms from Gemma 3 into Gemma 4 | License changed for the selected 4 release | Review each artifact's current terms |
| Use third-party quantization as provider support evidence | Community packaging can have different behavior and terms | Record its source and validate it independently |
| Compare HF downloads with API tokens | They count different events and populations | Keep adoption evidence type and window explicit |
| Assume a family label guarantees runtime parity | Engines implement modality and template paths differently | Validate the chosen engine and exact revision |

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/google/gemma-3-27b-it ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://huggingface.co/google/gemma-3n-E4B-it

## Requirements worksheet

Before recommending a Gemma identity, collect these facts from the requester or environment:

- whether images, video, or audio are required;
- whether inference must run locally, in a managed cloud, or on a device;
- maximum prompt and expected output size;
- expected number of simultaneous requests;
- whether user data can leave the deployment boundary;
- whether the license must allow redistribution or commercial use;
- expected language, domain, and structured output format;
- available serving engines and any pinned versions;
- acceptable response time and failure fallback;
- whether a provider-hosted Gemini endpoint is actually the intended product.

If the request says “Google's model” without clarifying deployment, distinguish Gemma weights from hosted Gemini API offerings before recommending an identity. A hosted Gemini request should not trigger this family skill.

For a suitable local model, include an implementation caveat in the recommendation: exact checkpoint, revision, license, context, modality, and selected runtime. If any of these remain unknown, label the gap and suggest a small validation step.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/google/gemma-3-27b-it ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://huggingface.co/google/gemma-3n-E4B-it

## Recommendation patterns

- If the request emphasizes low footprint and image input, begin with Gemma 3 12B rather than assuming the largest model is best.
- If audio or video input is mandatory on a compact device, test Gemma 3n E4B and account for its 32K context and modality tokenization.
- If the request emphasizes video, function calling, or newer reasoning behavior and a 31B deployment is acceptable, evaluate Gemma 4 31B.
- If the workload is strictly text and requires very long prompts, verify usable context and retrieval quality before choosing from the advertised maximum.
- If Apache 2.0 weight terms are a hard requirement, the selected Gemma 4 31B record fits that catalog criterion; Gemma 3/3n require separate terms review.
- If the request requires an official per-token rate, explain that no hosted rate is recorded for these downloadable checkpoints and ask whether managed Gemini API selection is the actual need.

These patterns narrow the shortlist. They do not guarantee performance, policy compliance, or legal suitability. Base a final recommendation on the exact artifact and tested environment.

When a model is rejected, identify the binding reason, such as missing audio input, context mismatch, custom terms, unsupported runtime, or deployment burden. Avoid vague statements like “too small” or “too expensive” unless the target constraints are known.

Before treating a candidate as production-ready, record the person responsible for rechecking terms and runtime support. Revisit these facts when changing model versions or deployment regions.

Keep a written record of chosen ID, revision, terms, context setting, template, runtime, precision, and evaluation result. This lets an operator reproduce a deployment and detect accidental checkpoint substitution.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://ai.google.dev/gemma/docs/core/model_card_4

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://ai.google.dev/gemma/terms/

> Source: https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-3n-E4B-it

## References to load

- `references/versions/gemma-3-12b-it.md` for the exact Gemma 3 12B artifact, license, context, and availability.
- `references/versions/gemma-3-27b-it.md` for the exact Gemma 3 27B artifact and its recorded evidence.
- `references/versions/gemma-3n-e4b-it.md` for Gemma 3n modalities, context tokenization, and adoption proxy.
- `references/versions/gemma-4-31b-it.md` for Gemma 4 identity, license, context, and adoption evidence.

Use Google’s current model cards and terms as the authority for changed details. For API mechanics, training, routing, and general evaluation infrastructure, use the existing `ai` skill.

## Operational readiness

Keep user-facing descriptions clear about which modalities work on the selected checkpoint and whether audio is available. Recheck processors, accepted formats, and terms when moving between major generations.

Name the exact variant whenever giving context, modality, or license guidance to a deployment owner.

Use the model-specific reference before quoting any limit.

> Source: https://ai.google.dev/gemma/docs/core/model_card_3 ; https://ai.google.dev/gemma/terms/ ; https://huggingface.co/google/gemma-3-12b-it ; https://ai.google.dev/gemma/docs/core/model_card_4 ; https://huggingface.co/collections/google/gemma-4 ; https://huggingface.co/google/gemma-4-31B-it ; https://huggingface.co/google/gemma-3-27b-it ; https://ai.google.dev/gemma/docs/gemma-3n/model_card ; https://huggingface.co/google/gemma-3n-E4B-it

## Sources

- https://ai.google.dev/gemma/docs/core/model_card_3
- https://ai.google.dev/gemma/terms/
- https://huggingface.co/google/gemma-3-12b-it
- https://ai.google.dev/gemma/docs/core/model_card_4
- https://huggingface.co/collections/google/gemma-4
- https://huggingface.co/google/gemma-4-31B-it
- https://ai.google.dev/gemma/docs/core/model_card_3
- https://ai.google.dev/gemma/terms/
- https://huggingface.co/google/gemma-3-27b-it
- https://ai.google.dev/gemma/docs/gemma-3n/model_card
- https://ai.google.dev/gemma/terms/
- https://huggingface.co/google/gemma-3n-E4B-it

Fetched: 2026-10-16
