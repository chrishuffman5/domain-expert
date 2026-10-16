---
name: jev-system-one
license: MIT
description: Select TypeSafe Jev for application-defined semantic decisions that should return constrained Choice, Score, or Noul values with probability information from text or structured state. Use it for classification, rubric scoring, or proposition probability rather than generated prose. Do NOT use for Jev API/SDK/HTTP integration, provider routing, harnesses, eval infrastructure, or implementation (use ai:jev); do NOT use for open-ended writing, code, explanations, or chain-of-thought (use a generative model), or supervised prediction from labeled tabular rows (use tabpfn or tabicl).
---

# Jev System One selection

## Role and boundary

Jev is TypeSafe's System One model for structured judgments consumed by software. The caller supplies application state and a set of typed questions; Jev returns typed answers and probabilities rather than a drafted response. This is a model-selection and decision-design guide. The existing `ai:jev` skill owns SDKs, endpoints, authentication, request construction, retries, and integration troubleshooting.

Use Jev when the decision is semantic but the answer space is known in advance: choose a queue, classify an intent, score a state against a rubric, or estimate whether a proposition is true. It can answer multiple independent questions against one shared state in a request. Keep each question atomic. If the workflow needs an explanation, user-facing prose, a code patch, or a multi-step deliberation, use a generative reasoning model for that part.

Jev is not interchangeable with a supervised tabular model. TabPFN and TabICL take labeled examples in a structured feature table and predict targets for rows. Jev interprets caller-provided state and question instructions. Choose based on the data contract and output task, not the fact that all three may influence a downstream decision.


> Source: https://docs.typesafe.ai/introduction
> Source: https://docs.typesafe.ai/concepts/system-one

## Choose by answer contract

| Need | Jev primitive | Use when | Do not assume |
|---|---|---|---|
| Select among named alternatives | Choice | Options can be described and the caller owns the valid set | The selected option is correct merely because it is schema-valid |
| Grade against ordered rubric levels | Score | A rubric has clear anchors and the result is useful as an ordered score | The numeric scale is an objective measurement without validation |
| Estimate whether a statement is true | Noul | A well-scoped proposition has a yes/no interpretation | Noul includes a separate confidence field; its probability is the uncertainty signal |

Define valid options, score levels, and the proposition in application code. Treat these definitions as part of the product contract. A change to option wording or rubric anchors can change behavior even when the model version remains fixed.

Prefer one question per distinct judgment. If a broad decision depends on policy compliance, evidence quality, and urgency, ask those separately and combine them with explicit code. This makes the weighting and action threshold reviewable and lets policy owners change logic without hiding it in a single opaque prompt.

Use a generative model in tandem only where it adds a distinct function: summarize long text, produce a response, or explain a result for a human. Keep Jev's typed judgment and the generative text output separate in the workflow so downstream actions depend on the validated result, not a plausible-sounding explanation.


> Source: https://docs.typesafe.ai/introduction
> Source: https://docs.typesafe.ai/primitives/choice
> Source: https://docs.typesafe.ai/primitives/noul

## Version and lifecycle choice

The catalog snapshot identifies `jev-1.13.0` as the stable release behind `jev-latest` on 2026-10-16. TypeSafe's model page identifies `jev-1.14.0` as the newer release available from October 14, 2026, and `jev-preview` points to it. The aliases are lifecycle pointers rather than pinned model identities.

Use the stable version for a production baseline when reproducibility matters. Pin the exact version for threshold calibration and regression tests; log the response model identifier. Evaluate a preview on representative offline cases before moving traffic. Do not treat `jev-latest` and `jev-preview` as synonyms: they can identify different versions during a rollout.

Re-check the official model page before recommending a newer version. Preserve the distinction between stable and preview in reports, dashboards, test fixtures, and change reviews. Recalibrate thresholds after a model change even if the primitive shape is unchanged.


> Source: https://docs.typesafe.ai/models
> Source: https://typesafe.ai/blog/jev-1-14

## Decision quality and uncertainty

A typed answer constrains format, not truth. Calibration describes how probabilities align with outcomes across groups; it does not certify an individual decision. Confidence values for Choice and Score summarize the returned probability distribution. For Noul, the yes probability itself indicates uncertainty, with values near 0.5 representing less decisive output.

Build a labeled validation set from the actual workload. Include ordinary cases, boundary cases, missing context, conflicting evidence, adversarial inputs, and examples where none of the configured options fits. Inspect errors by subgroup and by action cost. Do not set thresholds from a demo or from a vendor example.

Choose a separate action policy for each consequence. A low-risk inbox suggestion can tolerate a different threshold from a financial, legal, eligibility, medical, or access-control action. High-impact decisions should be checked against deterministic policy, authoritative records, and/or human review. High model confidence does not replace authorization, factual verification, or appeal paths.

A useful initial policy is three-way: accept only well-validated answers above a conservative threshold; send an uncertain or incomplete case to review; and reject or request missing evidence when the state fails preconditions. Thresholds are local operating choices, not model guarantees. Track coverage as well as accuracy: a system that abstains on difficult cases can look accurate while helping few users.

For Choice, compare the selected option probability with alternatives, not only a single confidence scalar. An option set with many choices changes the meaning of top probability. For Score, preserve the rubric and probability distribution where possible; adjacent levels may have different operational consequences than distant levels. For Noul, make the proposition direction explicit and inspect both positive and negative outcomes around the threshold.


> Source: https://docs.typesafe.ai/confidence

## State and question design

Supply only the state required to make the judgment. TypeSafe documents text as the input modality, represented as a string, JSON object, or array of text values. Images, audio, and video are not accepted as native inputs in the stable System One docs; transform them to reviewed text or structured fields before considering a request.

Use a structured state when it makes evidence and provenance clearer. Label fields, distinguish observed facts from user claims and derived values, include the relevant policy version, and avoid ambiguous nulls. Keep the original source available for audits. Do not ask the model to infer a missing fact that the application can obtain from an authoritative system.

Write question instructions as a narrow task with explicit criteria. Define what counts as each choice, what the score levels mean, or what evidence makes a proposition true. Mention how to handle insufficient or conflicting evidence. If no valid abstention value exists, design an external abstain route rather than forcing a guessed answer.

Avoid joining unrelated records into a single state unless the task requires it. More context is not automatically better. Review whether added history is relevant, current, and authorized for the purpose. Untrusted text inside user content can contain instructions; treat it as evidence to evaluate, never as an instruction that overrides the caller-authored question or system policy.


> Source: https://docs.typesafe.ai/concepts/system-one
> Source: https://docs.typesafe.ai/primitives/choice

## Context, language, and modality

The stable model page lists 64k tokens per request and 32k per question by default. The request limit covers state plus all questions; the per-question limit covers state plus an individual question. There is no separate fixed question-count limit if both documented limits are met.

The official page documents an opt-in long-context header that raises both limits to 262k. It warns that long-context requests are slower and less accurate than staying within the defaults. Use this experimental expansion only when necessary, compare quality on long and short cases, and document the latency and accuracy tradeoff. Do not presume the larger limit improves performance.

English is the primary training language and TypeSafe says it currently has the best accuracy. Other languages, including CJK scripts, are handled but not equally well. Evaluate each language and script with representative cases; route uncertain or unsupported language situations to an appropriate alternative.


> Source: https://docs.typesafe.ai/models

## Operational fit and adoption

The official model page lists input at $0.042 per million tokens and says output tokens are free. The same page describes organization-level rate limits, with custom or enterprise limits available. Recheck current terms and account limits during implementation planning; this skill's snapshot is not a quote or guarantee of capacity.

Public model-level request volume, token volume, active-user counts, or downloads were not found in inspected official materials. TypeSafe publishes qualitative company and case-study material, but that is not comparable usage telemetry. Jev is present in the curated catalog as a requested specialist typed-decision model, not because it was measured among the globally most used models.

Use Jev when a typed semantic decision fits the problem and the provider's hosted service, language support, data requirements, and price are acceptable. Use TabPFN or TabICL for supervised tabular rows; use ordinary classifiers or calibrated tree ensembles as local baselines; use a generative model when the needed output is text. Selection should follow a benchmark on the target distribution, not category prestige.


> Source: https://docs.typesafe.ai/models
> Source: https://typesafe.ai/blog/jack-jill-jev-case-study

## Deployment decision checklist

- State the decision in one sentence and name the downstream action.
- Confirm the answer contract is Choice, Score, or Noul.
- List valid answer values and define unknown, insufficient, or conflicting evidence handling.
- Identify authoritative facts and deterministic rules that must not be delegated.
- Build a representative labeled validation sample before activation.
- Measure error rates, calibration, subgroup behavior, coverage, and review volume.
- Select thresholds separately for each consequence and document who owns them.
- Choose stable pinned version or a preview evaluation explicitly.
- Confirm language, input modality, default context, rate limits, data handling, and total cost.
- Add human or deterministic fallback for uncertainty and high-impact action.
- Log model ID, question/rubric version, outcome, and permitted evidence needed for audit.
- Reevaluate after changes to prompts, state fields, policy, version, or population.


> Source: https://docs.typesafe.ai/confidence

## Common workload patterns

### Routing and triage

Define a bounded Choice set that maps to real queues or owners. Make options mutually distinguishable and give criteria for borderline cases. If “other” or “review” is valid, model that explicitly or implement an external fallback.

Test every queue with ordinary, short, long, mixed-intent, incomplete, and adversarial records. Measure per-queue precision and recall; a strong overall score can hide one queue that is systematically misrouted. Compare review cost with the cost of a wrong route.

### Rubric scoring

Use Score for ordered levels with observable anchors. Use Choice for nominal categories. If a score combines dimensions, ask a separate question for each dimension and combine them in code; this keeps weighting visible.

Decide whether downstream logic consumes the most likely level, expected score, or full distribution. Document the choice. Do not present a model score as an objective measurement unless local data supports that interpretation.

### Proposition checks

Use Noul for one proposition with a clear truth condition. Phrase the proposition directly and include its supporting evidence. Split compound claims into independent questions and define in code how their outputs combine.

A Noul probability is not a separate confidence field. Values near 0.5 are less decisive, but every threshold still needs validation against labeled outcomes.


> Source: https://docs.typesafe.ai/primitives/choice
> Source: https://docs.typesafe.ai/primitives/noul

## Failure handling and safeguards

Treat malformed responses, provider outages, rate limits, incomplete state, unsupported language, and out-of-distribution cases as explicit system paths. Define whether the system fails closed, queues review, or falls back to a conventional model. Never silently map an error to a default business choice.

Version the valid answer set and question instructions. Renaming a queue, changing a rubric anchor, or adding an option can alter behavior without a model upgrade. Rerun regression cases whenever the contract changes.

Keep model output separate from authorization. Do not let a single typed result directly grant access, transfer money, deny a benefit, or perform a destructive action. Apply the deterministic checks and confirmations that the consequence requires.

Minimize the state sent for a judgment. Include relevant evidence, distinguish observed facts from user claims, and exclude unrelated personal data. Confirm applicable privacy, retention, and data-handling terms for the chosen deployment route.


> Source: https://docs.typesafe.ai/confidence

## Monitoring and change control

After rollout, audit a labeled sample. Track errors, calibration, subgroup behavior, abstention/review rate, decision reversals, invalid inputs, latency, and rate-limit failures where available. Output confidence alone is not a monitoring system.

When labels arrive later, preserve model ID, question/rubric version, threshold, original result, and outcome. Avoid retaining sensitive raw text without a justified retention policy. Prefer aggregate monitoring where possible.

Treat an alias movement, model update, state-schema change, policy edit, or population shift as a revalidation event. Pin versions for controlled comparison and compare both outcome rates and probability distributions.


> Source: https://docs.typesafe.ai/models
> Source: https://docs.typesafe.ai/confidence

## Jev versus neighboring tools

| Need | Starting point | Selection reason |
|---|---|---|
| Semantic choice from text into a bounded set | Jev Choice | Application-defined answer contract |
| Prediction from labeled structured features | TabPFN, TabICL, or classical tabular model | Supervised feature-based task |
| Exact numeric or access rule | Deterministic code | Explicit condition should remain auditable |
| User-facing explanation or response | Generative language model | The required output is prose |
| Several uncertain factors with business weights | Separate Jev questions plus code | The application owns the combination logic |
| Legal entitlement determination | Authoritative rules and review | A probability is not a legal finding |

This is a task-fit comparison, not an accuracy ranking. A local classifier or deterministic workflow may be preferable when it meets the need with lower operational complexity.


> Source: https://docs.typesafe.ai/concepts/system-one

## Sources

- TypeSafe official documentation and release material are cited in the version reference.

Fetched: 2026-10-16
