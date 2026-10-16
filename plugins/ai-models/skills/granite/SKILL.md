---
name: granite
description: "Select IBM Granite open-weight models for enterprise text workflows, local or managed deployment, and IBM ecosystem use. Use for Granite 4.0 H Small, Granite checkpoint IDs, Apache-2.0 weight terms, or IBM-documented serving support. Do NOT use for AI fine-tuning/training workflows, generic model API/SDK mechanics, agent harness/tool integration, inference routing, or evaluation infrastructure; use the `ai` skill. Do NOT use for Gemma, Llama, Mistral, Nemotron, or Phi models; use their family skills."
license: MIT
---

# IBM Granite

This skill covers the selected Granite identity `ibm-granite/granite-4.0-h-small` and how to evaluate it for a deployment. The catalog currently selects one Granite model; it does not imply that every IBM Granite modality or release is covered here.

## When Granite 4.0 H Small fits

Consider Granite 4.0 H Small when you need an open-weight instruction model for enterprise text tasks, want to operate weights in your own environment, or need documented IBM serving paths. IBM presents the model as long-context and supports structured chat and tool calling in the official card.

The selected model has 32B parameters according to the catalog's inspected card and is Apache 2.0. IBM documentation lists vLLM, SGLang, and Docker Model Runner deployment options. These are useful supported paths, but they do not establish one universal memory target, throughput, or compatibility matrix. Check the selected engine version and accelerator support for the exact artifact.

Choose this model when provenance, enterprise workflow orientation, the Apache weight license, and a documented self-managed path matter more than a known numeric context ceiling or public adoption counter. Choose another model when multimodal inputs, small-device footprint, or a public per-token hosted price is a hard requirement; those are not established for this selected Granite identity.

| Requirement | Evidence-based Granite guidance |
|---|---|
| Commercial-friendly weight terms | Catalog lists Apache 2.0 for this artifact; still check code and dependencies separately |
| Long prompts | Described as long-context, but exact numeric context is unknown in this catalog |
| Text and enterprise workflow use | Primary intended selection profile in the model card |
| Tool calling | Supported in the model family/card; verify exact engine's template and parser |
| Public hosted price | Unknown; no official rate captured for this checkpoint |
| Popularity | Unknown; deployment documentation is not usage telemetry |

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/models/granite4-0

## Identity and release boundary

Use the canonical checkpoint ID `ibm-granite/granite-4.0-h-small`. The ID identifies a specific Granite 4.0 H Small artifact, not all Granite 4 releases or all IBM foundation models.

The catalog records the release month as 2025-10 and status as available. Pin the repository revision used for testing. If a later Granite release or checkpoint appears, treat it as a separate model identity unless IBM explicitly documents an alias or replacement.

Do not infer a retirement date from a release month or from an older IBM documentation page. Check the current official Hugging Face repository and IBM model page for availability when making a new selection.

If a managed IBM endpoint exposes the same model, confirm that the serving endpoint still matches this checkpoint's weights and template. Hosted platform aliases can have separate release schedules, access rules, pricing, or behavior.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small

## Context and quality limits

The inspected catalog record describes Granite 4.0 H Small as long-context but leaves its numeric maximum unknown because the extracted official card did not surface a specific cap. Preserve that unknown. Do not copy a context figure from a different Granite model, IBM API, or a third-party quantization.

Before using long prompts:

- inspect the exact pinned checkpoint configuration for its position limit;
- check the serving engine's accepted maximum sequence length;
- confirm whether truncation, chunking, or sliding-window behavior is applied;
- measure memory use as prompt length increases;
- evaluate retrieval quality at the beginning, middle, and end of realistic long inputs;
- budget for generated output and tool schemas alongside the input.

A configured maximum is only an input acceptance boundary. It does not guarantee accurate use of every position. Validate the context length that your workflow actually needs and choose a lower practical limit if quality degrades.

Do not describe the model as multimodal based on broad Granite family offerings. The selected record establishes text generation and enterprise workflows; check the exact checkpoint card for any additional modality before building around it.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## License and artifact terms

The selected weight artifact is recorded as Apache 2.0. That license applies to the artifact as distributed under its stated terms. It does not automatically license IBM's serving products, third-party libraries, datasets, trademarks, or alternative model versions.

For a commercial or redistributed deployment, keep the model license file with the pinned model revision. Check dependency licenses, any packaged code, and applicable platform agreements. Review attribution or notice requirements in the exact license file rather than relying solely on the catalog summary.

Do not equate “open weights” with “open training data” or unrestricted support. The current entry supports weights and documented deployment paths; the catalog does not make claims about availability of all training data or proprietary serving components.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small

## Serving and application integration

IBM documents serving with vLLM and a containerized route, and the model card lists vLLM, SGLang, and Docker Model Runner. Treat this as evidence that these paths are documented, not that every version has identical support or performance.

For a new setup, consult the linked current IBM guide and the checkpoint's current card. Record the serving engine version, container tag, model revision, tokenizer revision, accelerator, precision, and launch parameters. Pin dependencies and review any remote code before execution.

When the model returns tool calls, the application must still validate the tool name, arguments, permissions, and expected output shape. A model-supported tool format does not execute a tool safely by itself. Keep authorization and side-effect checks in application code.

Test user-facing behavior with representative documents, domain vocabulary, structured inputs, and tool schemas. Include adversarial or malformed requests, long text, empty fields, and outputs that violate a schema. A valid-looking answer may still be factually incorrect; create human review or deterministic checks where needed.

This skill helps choose the model identity and understand its documented tradeoffs. Generic API client setup, retry policy, routing across endpoints, and evaluation harness construction belong in the existing `ai` skill.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Deployment decision checklist

1. Confirm the workload is supported by the exact selected text checkpoint.
2. Establish a required prompt length and verify a numeric cap from the pinned model config.
3. Compare a representative quality set against a smaller or more specialized alternative.
4. Test the exact serving engine and supported model format before committing to a platform.
5. Measure latency and memory using your own hardware and prompt-length distribution.
6. Check that the Apache license and dependency terms meet redistribution and commercial requirements.
7. Build tool-call permission checks and output validation into the application.
8. Record an immutable model and runtime revision for reproducibility.
9. Treat the hosted price as unknown until an official endpoint-specific rate is found.
10. Treat model-level adoption as unknown unless a source gives a dated, scoped measurement.

Do not invent hardware requirements or throughput from the 32B parameter label. Weight precision, runtime implementation, batching, context length, and accelerator all affect deployment behavior.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Adoption interpretation

The inspected official card documents serving options but does not provide a captured usage or download count. IBM's deployment documentation establishes ecosystem support, not the number of active users or production requests.

Keep adoption marked unknown in this snapshot. If a later source publishes a count, record the platform, measurement window, retrieval date, whether it is downloads or active usage, and limitations. Do not compare a download count directly with API token totals or treat a card's likes as quality.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Practical fit by enterprise workflow

Granite 4.0 H Small is a candidate for text-centric enterprise workflows where an organization values open weights, IBM model provenance, and documented deployment choices. Potential task classes to evaluate include internal knowledge assistance, document question answering, extraction into schemas, and tool-mediated workflow steps. These are evaluation targets, not a claim that the model is accurate or certified for every domain.

| Workload | What to check before selection |
|---|---|
| Internal knowledge assistant | Retrieval quality, source citation behavior, refusal on missing evidence, and document length |
| Information extraction | Exact schema adherence, null handling, and behavior on conflicting fields |
| Tool-using workflow | Function syntax, argument validity, least-privilege execution, and safe failure |
| Regulated record review | Applicable policy, sensitive-data controls, reviewer workflow, and tested error rates |
| Long-context analysis | Numeric limit from the current config, engine cap, memory, and answer quality across positions |
| IBM-centered infrastructure | Current IBM deployment guidance, container compatibility, and support boundaries |

Use human review for high-impact decisions. Model output is probabilistic and does not replace policy checks, record validation, or domain expertise.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Exact configuration matters

“Granite 4.0 H Small” is not sufficient as a production identifier. Preserve `ibm-granite/granite-4.0-h-small`, the commit or immutable revision, tokenizer, quantized artifact if any, runtime, and prompt template.

At minimum, record:

- repository ID and revision;
- selected files and weight precision;
- tokenizer and special-token configuration;
- engine and container version;
- accelerator model and deployment topology;
- maximum sequence setting and truncation policy;
- tool parser or structured-output adapter;
- test set version and date;
- license and notices bundled with the deployment;
- date the official card and serving guide were rechecked.

This information is necessary to reproduce results. The model card's Apache 2.0 summary does not record every environment detail.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## What to do about the unknown context limit

The absence of an extracted numeric limit is a real evidence gap. Use this sequence to resolve it before accepting long-document workloads:

1. Open the current official model repository at the pinned revision.
2. Inspect model configuration fields that define supported sequence length.
3. Check whether the serving engine uses that value or overrides it.
4. Review IBM's current deployment guide for limitations that apply to its container.
5. Run a safe smoke test at a series of increasing prompt lengths.
6. Confirm whether the model rejects, truncates, or silently clips oversized input.
7. Test retrieval quality with relevant evidence placed early, in the middle, and near the end.
8. Select a conservative production maximum below the point where quality or memory becomes unacceptable.

Do not publish a guessed “long context” number as a model limit. If a numeric figure is later verified, add its official source and specify whether it is a model config maximum, a runtime cap, or an application policy.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/models/granite4-0

## Migration and change control

Treat changes to the weight revision, prompt template, runtime, quantization, or maximum sequence as a model change that requires retesting. A release with the same family name may alter output format or tool behavior.

For a migration, preserve the old revision and run both artifacts against the same representative examples. Compare task completion, schema validity, unsupported claims, refusals, tool-call quality, and operational resource use. Set acceptance criteria before looking at the comparison results.

If the model is behind a managed IBM endpoint, document the platform model identifier and current platform lifecycle separately from the local checkpoint. The hosted endpoint may change independently of a downloaded revision.

Do not rely on a stale IBM documentation URL for current parameters without checking its publication state. The catalog notes that IBM documentation labels some pages as legacy; current Hugging Face and GitHub artifacts should be checked when page content warns that it is no longer maintained.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Selection and fallback policy

Before making Granite the only model in a workflow, define how the application handles these cases:

- prompt exceeds the verified context setting;
- model returns malformed structured output;
- requested tool is not available or not authorized;
- model produces a low-confidence or unsupported answer;
- selected runtime cannot load the expected artifact;
- inference service is unavailable or runs out of memory;
- a license or security review blocks the chosen distribution;
- the user requests a modality not documented for this checkpoint.

A fallback can be a smaller input, a retrieval workflow, a deterministic parser, a different selected model, or a human review queue. Choose it based on the product risk and document the behavior for the user.

For comparisons, make sure alternatives are tested on the same input content, data access, output schema, and review criteria. Do not give one model privileged context that another lacks.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## Questions to answer in a recommendation

- What is the exact checkpoint and revision?
- What is the verified context limit on the intended runtime?
- Which serving path is being used and which versions are documented?
- What user workflow is the model expected to support?
- What quality criteria and fallback are defined?
- Does Apache 2.0 cover the intended weight use, and what licenses cover the rest of the stack?
- What is known about price and adoption, and what remains unknown?

When some answers are unavailable, make that uncertainty explicit. For Granite 4.0 H Small this snapshot records no official hosted rate, no numeric context cap, and no comparable public usage count. Avoid treating these gaps as zeros or as proof of superiority over another model.

Escalate missing license interpretation, privacy obligations, or security review to the organization's responsible owners before deployment.

> Source: https://huggingface.co/ibm-granite/granite-4.0-h-small ; https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized ; https://www.ibm.com/granite/docs/models/granite4-0

## References to load

- `references/versions/granite-4-0-h-small.md` for canonical ID, catalog lifecycle, license, recorded context caveat, sources, and unknown price/adoption values.
- IBM's model page and deployment guide for details that change independently of the catalog snapshot.

## Sources

- https://huggingface.co/ibm-granite/granite-4.0-h-small
- https://www.ibm.com/granite/docs/run/granite-with-vllm-containerized
- https://www.ibm.com/granite/docs/models/granite4-0

Fetched: 2026-10-16
