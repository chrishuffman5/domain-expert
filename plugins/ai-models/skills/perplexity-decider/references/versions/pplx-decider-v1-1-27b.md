# Perplexity Decider 27B (`pplx-decider-v1.1-27b`)

Status: active in the Perplexity Decisions API as of the inspected October 2026 documentation. Canonical ID: `pplx-decider-v1.1-27b`. The October changelog says v1.1 replaces `pplx-decider-v1-27b`; the older ID remains available at the same published input price in the pricing table. Use the versioned ID for reproducible selection and recheck status before deployment.

## What it returns

Decider reads a supplied state that can contain text, JSON or images and evaluates named questions. Supported question forms include `noul` (yes/no probability), `choice` (probability for each user-defined option plus a most-likely answer), and `score` (probability over ordered rubric levels plus expected score). It returns structured probability data rather than assistant prose.

It is intended for classification, routing, rubric grading and other decisions where software needs a typed answer instead of prompting a chat model and parsing text. The model does not write a user reply, generate code or explain its reasoning. Application code remains responsible for interpreting the probabilities and deciding whether an action is permitted.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart (inspected 2026-10-16)

## Price and limits

The current Perplexity price table lists $0.02 per million input tokens, free output tokens and no per-request fee for `pplx-decider-v1.1-27b`. The old v1 ID is listed at the same rate. The inspected decision-model documentation does not publish a context window number. Keep context as unknown and check current API request limits; do not infer it from the 27B model name or from another Perplexity model.

Pricing is unusually low per input token, but total task cost includes the application work needed to prepare state, any separate search/retrieval calls and downstream model/action steps. Token rate alone does not establish cost per correct routed decision.

> Source: https://docs.perplexity.ai/docs/getting-started/pricing ; https://docs.perplexity.ai/docs/decisions/quickstart (inspected 2026-10-16)

## Availability and licensing

The inspected docs expose the model through Perplexity's Decisions API. The model identity is a proprietary hosted API; no downloadable weights or public license were found in the inspected sources. Use current account and API access documentation for eligibility and request limits.

The changelog says v1.1 replaced v1 in the Decisions API and still supported requests naming the earlier model ID at the same price. That is a version lifecycle note, not a guarantee that old IDs will remain available indefinitely. Pin the selected ID in reproducible workflows and monitor current notices.

> Source: https://docs.perplexity.ai/docs/resources/changelog ; https://docs.perplexity.ai/docs/decisions/quickstart (inspected 2026-10-16)

## Adoption evidence

The catalog records a limited platform signal: OpenRouter's public ranking showed 184B tokens processed for Decider V1.1 27B among new/trending models, with the newest bucket dated 2026-10-13. This covers only public traffic routed through OpenRouter, not Perplexity's first-party API, other gateways, private traffic, unique users, spend, task preference or quality. It is an early platform-use signal, not broad market adoption.

Perplexity's own cookbook documents decision-model examples such as ticket triage, quote ranking and gating agent actions. These establish intended applications, not aggregate customer usage. Do not derive a global popularity rank from the OpenRouter token figure or cookbook presence.

> Source: https://openrouter.ai/rankings?benchmark=intelligence ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-ticket-triage/README (inspected 2026-10-16)

## Selection guidance

Choose Decider when the problem naturally decomposes into one or more declared questions over the same evidence and the application needs probability-bearing typed outputs. A single request can ask multiple questions about the same state. This can avoid generating a paragraph and extracting an answer, but question and rubric design still determines usefulness.

Use a general chat model when the product requires a natural-language explanation, drafting, code generation or open-ended synthesis. Use Jev System One when TypeSafe's semantic decision primitives and ecosystem fit the workload. Decider and Jev are alternatives in the decision-model category, not aliases or equivalent products. Read both family references before comparing them.

Use tabular prediction families such as TabPFN or TabICL when the input is labeled structured rows and the job is to predict outcomes for new rows. Decider takes natural-language or JSON state plus declared questions; it is not a supervised tabular predictor.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/getting-started/pricing (inspected 2026-10-16)

## Thresholds, calibration and safety

A returned probability is a model estimate. It is not a calibrated business probability unless you validate calibration for the target data, question wording and population. Build a labeled test set, inspect reliability and error rates, tune thresholds by consequence and define a review/escalation path for uncertain or high-impact cases. A low token price does not justify acting on a poorly tested decision.

The Decisions API examples show threshold-based workflows. The threshold is part of application policy, not an automatic permission grant from the model. Keep authorization, payment rules, account checks, data validation and rollback control in ordinary code. For actions with external effects, use independent checks and human approval where appropriate. Avoid sending extra irrelevant state: it adds tokens and can distract the classifier.

Do not ask the model to replace deterministic computations such as arithmetic, dates, exact schema validation or access-control checks. Compute deterministic facts in code; ask the model only for the semantic judgment that remains uncertain. Decide what to do when probabilities conflict, are diffuse or fall below a minimum confidence condition.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-ticket-triage/README (inspected 2026-10-16)

## Migration and exact-ID checks

Perplexity's October 2026 changelog says `pplx-decider-v1.1-27b` replaced `pplx-decider-v1-27b`; the older ID continued working in the inspected changelog and price table. The model examples refer to the stable versioned name. If an integration uses a floating alias, verify its current target and preserve the versioned ID in records where reproducibility matters.

The catalog sources do not establish a context limit, a retirement date or first-party usage total. Keep those fields unknown unless the provider publishes them. Recheck the exact endpoint, API contract, model lifecycle and pricing before a deployment change.

> Source: https://docs.perplexity.ai/docs/resources/changelog ; https://docs.perplexity.ai/docs/getting-started/pricing (inspected 2026-10-16)

## Sources

- https://docs.perplexity.ai/docs/decisions/quickstart
- https://docs.perplexity.ai/docs/getting-started/pricing
- https://docs.perplexity.ai/docs/resources/changelog
- https://openrouter.ai/rankings?benchmark=intelligence

Fetched: 2026-10-16
