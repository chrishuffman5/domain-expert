---
name: cohere-command
license: MIT
description: "Select among Cohere Command A+ multimodal agents, Command A Reasoning, and Command A Vision for enterprise language and document tasks. WHEN: Command family exact IDs, vision versus reasoning, tool-use and RAG fit, context or licensing. Do NOT use for other model families, Cohere API/SDK calls, routing, agent harnesses, training, or eval infrastructure; use `ai-models-specialist` for comparisons and the existing `ai` plugin for operations."
---

# Cohere Command model selection

This family skill distinguishes the selected Command model identities and their deployment boundaries. It covers model fit, documented limits, licenses and lifecycle evidence. The Command API request schema, SDKs, cloud routing and agent implementation remain in the existing `ai` plugin.

## Routing

| Request | Read |
|---|---|
| Image input plus agentic reasoning and tools | [`Command A+`](references/versions/command-a-plus-05-2026.md) |
| Reasoning-first text model with long context | [`Command A Reasoning`](references/versions/command-a-reasoning-08-2025.md) |
| Document, image, chart, table or OCR analysis without tools | [`Command A Vision`](references/versions/command-a-vision-07-2025.md) |
| Command API/SDK mechanics, tool schemas or RAG integration | Existing `ai` plugin API/agent/inference skills |
| Other model families, exact cross-provider comparisons | `ai-models-specialist` and the competing family skill |

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Selected identities

| Name | Exact model ID | Modality | Main selection reason | Version reference |
|---|---|---|---|---|
| Command A+ | `command-a-plus-05-2026` | Text and image input; text output | Multimodal tool-using agent, 48 languages | [reference](references/versions/command-a-plus-05-2026.md) |
| Command A Reasoning | `command-a-reasoning-08-2025` | Text input/output | Reasoning-first, long-context agent and RAG work | [reference](references/versions/command-a-reasoning-08-2025.md) |
| Command A Vision | `command-a-vision-07-2025` | Text and image input; text output | Document/image perception with OCR and charts | [reference](references/versions/command-a-vision-07-2025.md) |

These are distinct active family members. Model names and version suffixes are not interchangeable. Do not assume a newer date guarantees suitability or a specific performance gain for your task.

The broader Command family also includes other models, including general Command A, translation and R-family versions. They are not selected model identities in this catalog subset. Do not silently substitute `command-a-03-2025` for one of these three or count old aliases/variants as additional selected models.

> Source: https://docs.cohere.com/docs/models (inspected 2026-10-16)

## Quick selection rules

- Choose **A+** when one model needs image and text input together with reasoning and tool use, and its 128K context and production pricing are acceptable.
- Choose **A Reasoning** when the task needs explicit reasoning-first behavior, text input and 256K context; production hardware is heavier and current pricing was not published in the inspected page.
- Choose **A Vision** when visual/document understanding is central and the model does not need to call tools; it has 128K context and a 20-image-per-request limit.
- If the workflow requires both detailed image perception and tools, compare A+ with a separate vision-plus-agent architecture. Vision alone cannot use tools.
- If the request only needs routine RAG or chat, do not automatically select a reasoning or multimodal tier. Compare other current family members and platform choices in the complete catalog.

| Workload requirement | Candidate | Verify |
|---|---|---|
| Tool-using enterprise agent that sees screenshots/doc images | A+ | Image throughput, tool quality, 48-language coverage and contract rate |
| Nuanced multi-step text reasoning over long source context | A Reasoning | 4×H100 production footprint, response length and current entitlement |
| Read charts, scanned documents or tables and answer in text | A Vision | Maximum image count, supported languages, no tool use |
| Produce an image | None of these selected Command models | Select a separate image-generation family |
| Free API calls for production indefinitely | None assumed | Free language is conditional on rate limits; confirm contract/pricing |

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Modality and tool boundaries

The family has two multimodal identities with different behavioral boundaries. A+ accepts text and images and supports tool use and reasoning. A Vision accepts images and text but explicitly does not support tool use and does not generate images. A Reasoning is described as text-input reasoning, not the image-input tier. Do not transfer one model's capability list to the others because the family shares a Chat API surface.

For image-heavy work, test input scale and actual visual conditions. Include documents with dense tables, small text, multiple charts, low-resolution scans and mixed-language evidence. For image input plus action, ensure the chosen model supports tools and validate every proposed tool call in application code. For Vision-only extraction, parse outputs against a schema and reject incomplete or unsupported-format answers.

The selection question is whether the model should understand an image, reason over text, or both understand images and use tools. These are different requirements; selecting “multimodal Command” without making that distinction can select the wrong member.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Context, output and languages

| Model | Context | Maximum output | Language detail in inspected docs |
|---|---:|---:|---|
| A+ | 128K | 64K | 48 languages |
| A Reasoning | 256K | 32K | 23 languages |
| A Vision | 128K | 8K | Officially listed support: English, Portuguese, Italian, French, German, Spanish |

Context is not the same as usable retrieved evidence. Test long RAG contexts for attention to relevant passages, citation correctness and factual grounding. Plan for output caps and stop conditions; a 64K output limit is not a recommendation to generate 64K tokens. Language lists indicate provider-supported coverage, not equal accuracy across languages or tasks.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision ; https://docs.cohere.com/docs/models (inspected 2026-10-16)

## Pricing, access and licensing

A+ and Vision pages say the API is free until rate limits are reached; production deployment routes through Model Vault or requires sales/commercial access. These statements do not provide a universal public production rate. A Reasoning's inspected page also does not provide a current rate. Record exact prices as unknown unless current account pricing is available.

A+ has a W4A4 Hugging Face checkpoint with an Apache 2.0 license; that license belongs to the disclosed artifact. It does not set the terms for hosted Cohere API access. The inspected pages did not establish a downloadable license for A Reasoning or A Vision; treat them as hosted proprietary offerings unless an official checkpoint/license is verified.

Do not estimate self-hosting cost from parameter count alone. The source describes A+ fitting on one B200 or two H100s at W4A4, while Reasoning production is optimized for four H100s. Confirm the precise artifact, quantization, runtime and contract before converting these hardware notes into capacity plans.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4 ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Adoption and lifecycle

Cohere did not publish comparable model-level usage or download totals for these three entries in the inspected docs. Adoption is unknown; product positioning, hardware efficiency claims and active status are not adoption measurements. Do not infer that A+ is most popular because it is newer or called the most performant.

The family overview lists Command model status, model IDs, modalities and limits. It marks some older Command R/R+ IDs as deprecated. This selected subset does not include those older identities. Recheck current status, exact model ID, context/output limits, account eligibility, production pricing and license before a migration. Do not treat the model-ID date as a retirement or support guarantee.

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Evaluation checklist

For a pilot, compare the selected candidate on the actual workflow:

1. Use held-out examples with representative language, document quality, retrieval noise and tool outcomes.
2. Measure task correctness and grounding, not answer fluency alone.
3. For vision, label the target text, tables, chart values and layout interpretation separately.
4. For agents, measure tool-call precision, unnecessary calls, invalid arguments and final task completion.
5. Record context length, generated tokens, latency, failures and the model version used.
6. Price with account-specific production rates and hardware/hosting terms.
7. Define an escalation route for unsupported languages, malformed documents or low-confidence outputs.

Do not use this model-selection skill to build the API request, calculate exact token counts or implement tool execution. Those are integration concerns handled by existing `ai` skills. Use `evals` for framework and grader design.

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Decision path for a first shortlist

Use these questions in order:

1. Must the model interpret images? If no, A Reasoning may be a fit for text-only reasoning; evaluate other text options if the workload is simple.
2. Must the model call tools? If yes, A+ is the selected multimodal Command identity with image and tool support. A Vision is excluded because it lacks tool use.
3. Is the input primarily document images/charts/tables where extraction matters? If yes and tools are not needed, start with A Vision.
4. Is a 256K context important? A Reasoning has the selected family’s longest listed context; verify the specific request and output limits.
5. Is deployment via a downloadable checkpoint required? Only the selected A+ W4A4 artifact has a documented Apache 2.0 license in this subset; inspect artifact terms and compute requirements.
6. Does the contract/rate card fit? Public docs do not establish a universal production token rate for these entries.

A “yes” to multiple conflicting requirements may imply a two-stage design or a different family. Do not select Vision for a tool-using workflow and then assume the shared Chat endpoint can make it use tools.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Field-level tradeoffs

| Dimension | A+ | A Reasoning | A Vision |
|---|---|---|---|
| Primary strength | Multimodal agentic tasks | Text reasoning and agentic tasks | Image/document interpretation |
| Image input | Yes | Not listed in inspected family table | Yes |
| Tool support | Yes | Yes | No |
| Context | 128K | 256K | 128K |
| Max output | 64K | 32K | 8K |
| Language count | 48 | 23 | Six listed official languages |
| Hardware note | 1 B200 or 2 H100 at W4A4 | 4 H100 production; 4 A100 non-production | Unknown in inspected page |
| Public rate | Not listed; commercial Model Vault terms | Unknown | Production access via sales; rate not listed |

The table reports vendor documentation, not a head-to-head benchmark. Longer context and output are capacity ceilings, not proof of better answers. Hardware rows may refer to different deployment recipes and should not be compared as equal-cost throughput.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision ; https://docs.cohere.com/docs/models (inspected 2026-10-16)

## Failure modes to test

- A+ can produce text about a screenshot yet still misread small labels; test actual resolution and compression.
- A+ tool availability does not guarantee correct or necessary tool selection; inspect call precision and argument validity.
- A Reasoning's long context can still miss or distort relevant evidence; use citation/grounding checks and long-context probes.
- A Reasoning's reasoning-first profile may cost more in time or tokens than a simpler model; compare task completion cost.
- Vision may return plausible prose while omitting a table row or chart scale; compare structured extracted values against ground truth.
- Vision cannot call tools or generate images, even if another Command model can.
- Multiple supported languages do not imply identical task performance across all languages; test the actual languages required.
- A free trial/rate-limited key does not prove a production capacity, SLA or price.
- A quantized self-hosted checkpoint may behave differently from the hosted service; version and evaluate the artifact itself.

Tie each failure case to an application control: reject malformed extractions, retry only for documented transient service failures, require human review for consequential outputs, and log model ID plus source version for reproducibility.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Cost and procurement questions

Before a production recommendation, establish whether the user means Cohere-hosted inference, Model Vault, Azure AI Foundry, OCI or the public A+ checkpoint. The model identity can be constant while billing and operational obligations differ by deployment surface.

Request the current written rate and access terms for the intended environment. Clarify:

- Which model ID and release are included.
- Whether the rate varies by input/output, region, token volume or reserved capacity.
- What the free-until-rate-limit statement means for a production key.
- Whether vision inputs incur additional image processing charges.
- Whether Model Vault deployment requires minimum capacity or contract commitment.
- What hardware, quantization and support versions apply to self-hosted A+.
- Whether a self-hosted deployment has terms beyond the Apache 2.0 checkpoint license.

If these are unknown, label them unknown; do not extrapolate Command A's publicly listed rate to A+, Reasoning or Vision.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision ; https://docs.cohere.com/docs/how-does-cohere-pricing-work (inspected 2026-10-16)

## Deployment boundary questions

Ask which Cohere deployment surface the user intends before making a feasibility statement:

- Cohere's hosted Chat API.
- Cohere Model Vault for production workloads.
- A downloadable model artifact and self-managed serving.
- A third-party cloud endpoint with its own model ID and terms.

Then verify that exact model ID, feature set, public/commercial access and license on the chosen surface. A model may be active in the family catalog while a deployment route is unavailable, gated or governed by separate terms. A hosted API capability list does not automatically apply to a checkpoint, and an artifact license does not grant API credits.

The current chosen catalog has only an A+ open artifact documented with Apache 2.0. Do not tell users that all Command models share this license. For Reasoning and Vision, the inspected sources do not establish a public weight license. Tell the user when that legal/deployment detail remains unknown.

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/docs/command-a-plus ; https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4 ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Compare candidates on the same evidence

Use the same document set, questions, expected answer structure and error rubric when comparing Vision with a general reasoning candidate. Score extraction fidelity separately from answer usefulness so a fluent but unsupported summary does not mask missed table cells or OCR errors.

For agentic tasks, include tool selection, argument correctness, completion rate and recovery from tool failures. Compare the model's reasoning output only if the selected product actually exposes it; do not assume a reasoning trace is available because the model name includes “Reasoning.”

For RAG, assess retrieval relevance and answer grounding in addition to generation. A model's stated RAG use case does not certify the quality of the user's retrieval corpus or prove that citations are complete.

> Source: https://docs.cohere.com/docs/command-a-plus ; https://docs.cohere.com/docs/command-a-reasoning ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Sources

- https://docs.cohere.com/docs/command-a-plus
- https://docs.cohere.com/docs/models
- https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4
- https://docs.cohere.com/docs/command-a-reasoning
- https://docs.cohere.com/changelog/2025-08-21-command-a-reasoning
- https://docs.cohere.com/docs/command-a-vision

Fetched: 2026-10-16
