---
name: gpt-oss
license: MIT
description: Choose between OpenAI gpt-oss downloadable open-weight models for local or self-managed inference, balancing memory, reasoning, tool use, and deployment control. Use when weights and self-hosting are part of the requirement. Do NOT use for hosted GPT API model selection; use gpt. Do NOT use for API or SDK mechanics, harnesses, eval infrastructure, or inference routing; use ai.
---

# OpenAI gpt-oss model selection

This skill covers OpenAI’s downloadable gpt-oss-120b and gpt-oss-20b model identities. It helps decide whether either model fits a local or self-managed environment. It does not explain runtime libraries, serving stacks, API mechanics, or inference routing.

## First decide whether open weights fit

Choose this family when access to model weights, self-managed inference, or local iteration is a meaningful requirement.

Do not choose it only because “open” sounds lower cost or simpler.

Self-hosting shifts work to the deploying team: hardware, memory, serving, upgrades, access controls, monitoring, and safety evaluation.

Compute and engineering costs can exceed a hosted token bill at low or irregular volume.

Estimate expected throughput and concurrency against actual hardware before selecting a size.

Confirm the selected license and usage policy for the intended use.

Apache 2.0 is the cataloged license, subject to OpenAI’s usage policy.

A permissive license does not remove security, privacy, safety, or governance obligations.

## Routing table

| Need | Start with | Why | Main tradeoff |
|---|---|---|---|
| Local or self-managed inference with more capacity | [gpt-oss-120b](references/versions/gpt-oss-120b.md) | The release describes near-parity with OpenAI o4-mini on core reasoning benchmarks and efficient operation on one 80 GB GPU | Requires substantial accelerator memory and serving capacity |
| Smaller deployment or edge-oriented use | [gpt-oss-20b](references/versions/gpt-oss-20b.md) | The release says it can run with 16 GB memory and reports competitive common-benchmark results | Lower capability ceiling and still requires deployment expertise |

These are separate model identities, not quantizations or endpoints of one hosted API model. Use the model card and release source for the selected identity rather than transferring details from one size to the other.

## Understand the model shape

Both models are text-oriented reasoning models with tool-use capability in OpenAI’s release materials.

The training data is described as mostly English and text-only, with focus on STEM, coding, and general knowledge.

The family uses mixture-of-experts architecture. Only a fraction of total parameters are active per token, but this does not mean total memory requirements equal active parameter count.

The release lists 128K context for each size.

Context length does not promise perfect retrieval, instruction following, or stable cost/latency across the full window.

Test long prompts for retrieval, distractor resistance, and answer quality at the intended sequence length.

Check the model card for recommended prompt format and implementation-specific details before running the model.

Do not assume that a hosted GPT API model’s controls, refusals, or behavior transfer to gpt-oss.

## Compare the two sizes

### gpt-oss-120b

The release lists 117B total parameters and 5.1B active parameters per token.

It has 128 experts with four active experts per token and 36 layers.

OpenAI says it can run efficiently on one 80 GB GPU.

The release reports near-parity with o4-mini on core reasoning benchmarks and strong tool use.

This makes it the larger option to test when task quality matters and infrastructure supports it.

It still needs measured memory, throughput, concurrency, and prompt-fit validation in the actual serving environment.

### gpt-oss-20b

The release lists 21B total parameters and 3.6B active parameters per token.

It has 32 experts with four active experts per token and 24 layers.

OpenAI says it can run on edge devices with 16 GB of memory.

The release describes results similar to o3-mini on common benchmarks and notes strong mathematics results.

This is the first candidate to test when memory and deployment footprint dominate.

Do not assume the 20b model equals 120b quality because the active-parameter figures are close.

The total model size, architecture and evaluated results differ.

## Selection procedure

Write down hardware constraints: accelerator type, available memory, expected concurrency, and storage.

Estimate request size and context distribution rather than planning for a maximum prompt on every request.

Select a representative task set that includes common, difficult, malformed, and adversarial examples.

Measure task completion quality and correctness, not only token generation speed.

Measure total serving performance under the expected concurrency.

Inspect tool-use behavior on realistic tool schemas and failure responses.

Test whether the model asks for missing data or fabricates a plausible answer.

Compare both sizes at the same task and acceptance criteria.

If the smaller model meets the bar with adequate headroom, the larger model’s capability may not justify the deployment burden.

If the smaller model misses important task cases, evaluate the larger model before choosing a hosted alternative.

Keep a fallback plan for tasks that exceed the local model’s tested capability.

## Cost and operations

There is no OpenAI hosted API token price for these downloadable weights in the catalog.

Self-hosted cost depends on hardware purchase or rental, utilization, energy, serving software, staffing, and maintenance.

Do not quote parameter count as a direct estimate of dollars per request.

Do not equate a model’s active parameters with the amount of memory needed to load and serve it.

Quantized or third-party derived variants are not separate catalog identities here.

Validate any derivative’s provenance, license, quality, security, and compatibility independently.

Use the original OpenAI model card as the basis for canonical identity and policy.

Keep downloaded weights and supporting artifacts versioned and integrity-checked.

Apply access controls to model endpoints and data stores.

Keep sensitive prompts and outputs within the approved environment.

Plan how to update the model, serving stack, and safety controls without losing reproducibility.

## Deployment readiness checks

Confirm that the available memory accounts for model weights and runtime overhead.

Reserve headroom for context, concurrent requests, and intermediate buffers.

Measure first-token and full-response time under representative load.

Check behavior when the environment restarts or the model process fails.

Validate that the model artifact can be fetched from a trusted source and verified.

Confirm that local data stays on the intended machine and logs do not leak prompts.

Write down who owns model updates, incident response, and rollback.

Decide how users learn that the local model may be less capable than a hosted service.

Keep an operational fallback for requests that exceed local capacity.

Review license and usage-policy changes when refreshing model artifacts.

## Safety and output limits

Open weights provide deployment control, not guaranteed safe behavior.

Test refusal behavior and policy compliance for the actual task and user population.

Tool calls can produce external effects if the surrounding software executes them.

Review or constrain those effects in the application.

Use explicit permissions and validate tool arguments before execution.

Treat model-generated code and commands as untrusted until checked.

Add domain validation for high-impact outputs.

Keep logging and retention consistent with applicable privacy and security rules.

The model card and release materials provide a baseline, not a substitute for local risk analysis.

## Adoption evidence

The catalog marks model-specific adoption as unknown for both gpt-oss entries.

The release and official model card establish availability and technical characteristics, but those are not usage counts.

Repository downloads, even where available, count distribution requests rather than active installations or production usage.

Do not use third-party mirrors as official deployment telemetry.

Unknown does not imply zero use or low capability.

The family is included because open-weight deployment is a distinct capability choice, not because a global adoption rank was established.

## Model identity and license

The canonical identifiers are `gpt-oss-120b` and `gpt-oss-20b`.

A quantization, mirror, runtime, or hosted endpoint serving the same weights does not create another model entry.

Use the source reference to distinguish original weights from community derivatives.

The catalog records Apache-2.0 subject to the OpenAI usage policy.

Read the license and policy text applicable to your downloaded artifact and use case.

Do not infer permission for a use case solely from the word “open-weight.”

## When to choose another family

Choose `gpt` when a hosted OpenAI API model is the requirement and self-managed weights are not.

Use the `ai` skill for SDKs, serving harnesses, API mechanics, evaluation infrastructure, and routing.

Choose a specialized decision model when typed decisions or predictive tabular learning is the actual task.

## Sources

- OpenAI gpt-oss release: https://openai.com/index/introducing-gpt-oss/
- OpenAI gpt-oss model card: https://openai.com/index/gpt-oss-model-card/

Fetched: 2026-10-16 UTC.
