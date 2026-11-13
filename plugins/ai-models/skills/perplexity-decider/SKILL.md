---
name: perplexity-decider
license: MIT
description: "Select Perplexity Decider for structured probability-bearing semantic decisions over text, JSON or images. WHEN: classification, routing, yes/no, choice, rubric scoring, Decider versus Jev fit. Do NOT use for other model families, Perplexity API calls/SDKs, search or inference routing, agent harnesses, training, or eval infrastructure; use `ai-models-specialist` for alternatives and the existing `ai` plugin for operations."
---

# Perplexity Decider selection

This skill covers the selected Perplexity decision model's identity, behavior and workload fit. It distinguishes a typed decision model from a text-generating chat model. API mechanics, search API usage and integration operations belong to the existing `ai` plugin where covered.

## Routing

| Request | Read |
|---|---|
| Exact ID, structured decision types, limits, price and lifecycle | [`pplx-decider-v1.1-27b`](references/versions/pplx-decider-v1-1-27b.md) |
| Decide between Perplexity Decider, Jev and other model families | `ai-models-specialist`, then read each candidate reference |
| Perplexity API/SDK operations or Search/Agent API configuration | Existing `ai` plugin's relevant API/integration material |
| Agent policy, human approval or tool execution | Existing `ai` plugin's agent/security skills |
| Tabular supervised prediction | `tabpfn` or `tabicl` family skill, not this family |

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/getting-started/pricing (inspected 2026-10-16)

## Selected model

| Model | Canonical ID | Output form | Best-fit task |
|---|---|---|---|
| Perplexity Decider 27B | `pplx-decider-v1.1-27b` | Typed probability result | Semantic classification, routing, choice or rubric scoring |

The catalog contains one Perplexity Decider identity. The older `pplx-decider-v1-27b` is a prior version still listed as working in the October 2026 changelog/pricing docs, not a separate current selection. Keep the current versioned ID distinct from any floating alias a cookbook or client may expose.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/resources/changelog (inspected 2026-10-16)

## What makes this a decision model

A decision model takes supplied state and named questions, then returns probabilities in a typed shape. Perplexity documents yes/no (`noul`), multiple-choice (`choice`) and ordered rubric (`score`) questions. It can answer multiple questions about one state in one request. The output is structured evidence for application code; it is not a user-facing message.

This changes how you should assess fit:

- Use Decider when your software needs a label, a choice among supplied options, or a score over a defined rubric.
- Use a general chat model when you need explanation, writing, code, conversation or broad synthesis.
- Use a search/grounded answer path when the task is to retrieve and synthesize current web information.
- Use a tabular predictive model when the input is a dataset of labeled rows and the output is a prediction for new rows.

The interface may be exposed by an API product, but this skill is about model suitability, not request construction.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart (inspected 2026-10-16)

## Fit against nearby families

**Jev System One** is the closest semantic decision alternative in this catalog. Jev uses declared Choice, Score and Noul primitives and returns typed answers. Decider is Perplexity's decision model and API. Compare input shape, response semantics, context and account access from each provider source before choosing. Do not infer equivalence from similar yes/no/choice/score terminology.

**TabPFN and TabICL** target predictive tabular learning from examples/rows, not natural-language state-to-question decisions. If the user has a labeled dataset and wants classification/regression on new records, inspect those families. Do not recommend a semantic decision model as a substitute for a tabular model without evaluating the actual input and task.

**General chat models** can sometimes be prompted to output labels or JSON, but their native purpose is generated language. Compare parsing burden, probability calibration, latency and model cost against Decider with a representative test set. Decider does not provide prose explanations, so choose a chat model or a separate explanation stage when human-readable rationale is required.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/getting-started/pricing (inspected 2026-10-16)

## Price, limits and unknowns

The inspected Perplexity price table lists $0.02 per million input tokens, free output and no per-request fee for the versioned Decider ID. The same table lists the older v1 ID. Exact context length is not given on the inspected decision model page; keep it unknown and consult current request limits.

The official documentation does not establish a downloadable license. This is a hosted proprietary API model. The model-level usage total for Perplexity's own API was not disclosed. A scoped OpenRouter usage signal is recorded in the version reference and should remain clearly labeled as router-only traffic.

Do not import Sonar token rates, search invocation fees, Agent API tool charges or a third-party model's limits into Decider's pricing. Check the product route because Perplexity's APIs meter services differently.

> Source: https://docs.perplexity.ai/docs/getting-started/pricing ; https://docs.perplexity.ai/docs/decisions/quickstart ; https://openrouter.ai/rankings?benchmark=intelligence (inspected 2026-10-16)

## Confidence and application policy

Treat the probabilities as estimates to validate, not as guaranteed calibrated confidence. Build a labeled dataset from the target population, measure correctness and calibration, and tune action-specific thresholds. Use an explicit undecided/other option when the choice set may be incomplete, or design a separate no-match check. Handle contradictory or low-confidence results through review or clarification.

Keep deterministic and policy checks outside the model. Code should enforce schemas, thresholds, authorization and side-effect rules. The model's probability that an action is appropriate is not an authorization grant. For payments, account changes, or other consequential actions, independently verify facts and retain a human approval path as appropriate.

Minimize state to relevant information. Unrelated documents can raise cost and influence the answer. Use separate questions for separate dimensions rather than a compound question whose outputs cannot be independently acted upon.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-ticket-triage/README (inspected 2026-10-16)

## Adoption and lifecycle

The selected catalog entry has a 2026-10-13 OpenRouter public token-volume observation, retrieved on 2026-10-16. This is only traffic routed through OpenRouter; it excludes private and direct provider calls and is not unique users or quality evidence. The Perplexity docs describe example applications but do not publish an aggregate first-party model usage total.

Perplexity's changelog states that v1.1 replaced v1; no retirement date was found for the older ID. Check the exact model list and price table before pinning or migrating. Avoid floating aliases when you need reproducible behavior.

> Source: https://openrouter.ai/rankings?benchmark=intelligence ; https://docs.perplexity.ai/docs/resources/changelog (inspected 2026-10-16)

## Selection checklist

1. Does the task need a typed decision result, or a generated explanation?
2. Is the state text/JSON/image content that can be represented within current request limits?
3. Are the answer options and rubric complete and unambiguous?
4. Has the threshold been calibrated on representative labeled examples?
5. What should happen when confidence is low or the result is inconsistent?
6. Are deterministic validation and action authorization enforced outside the model?
7. Which API product and pricing route will be used, and are current limits confirmed?

For Jev-versus-Decider or cross-provider comparison, use the `ai-models-specialist`. For SDK, API, Search API and operational questions, route to the existing `ai` plugin's integration guidance.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/getting-started/pricing (inspected 2026-10-16)

## Decision-shape worksheet

Before choosing Decider, write down the required output in terms of software behavior:

| Need | Question design | Output consumer |
|---|---|---|
| Does a condition hold? | One narrow yes/no question | Boolean threshold plus review policy |
| Which intent/category applies? | Choice among complete named options plus `other`/none when needed | Router with fallback for low confidence |
| How severe is a case? | Ordered rubric with concrete, distinct levels | Escalation threshold and audit trail |
| Explain a conclusion in natural language | Not a Decider task by itself | Chat/research model or separately generated rationale |
| Predict a value from rows and labels | Tabular prediction, not semantic decision | TabPFN/TabICL family workflow |

Question text and criteria are part of the model's behavior. Keep each question focused on one condition or dimension. Avoid mixing urgency, sentiment and refund intent into one overloaded label if separate downstream actions depend on them.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart (inspected 2026-10-16)

## Designing a controlled decision workflow

1. Keep the source record as the state; avoid paraphrasing away material evidence.
2. Limit the state to relevant facts to avoid distraction and unnecessary input cost.
3. Define all valid output choices before calling the model.
4. Include an explicit no-match or human-review route when the taxonomy can be incomplete.
5. Ask independent questions separately so each result can have its own threshold.
6. Validate that the returned answer schema matches the intended question type.
7. Use a calibrated threshold; record when the system abstains or escalates.
8. Store the model ID, state version, question wording, options and returned probabilities for audit.
9. Let deterministic code enforce business rules and final actions.
10. Test with examples from both common cases and rare, high-consequence cases.

The official quickstart describes multiple questions per state. That feature saves repeated context, but it does not guarantee consistency among answers. If downstream invariants matter, check them in application code.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-ticket-triage/README (inspected 2026-10-16)

## Threshold and abstention policy

Do not choose thresholds from a convenient round number or the model's token price. Estimate the cost of false positives, false negatives and human review. Tune thresholds on a representative labeled set and compare expected loss. Check calibration separately across relevant categories or populations if error costs differ.

A practical policy has at least three paths:

- **Automate:** probability and calibrated risk satisfy the action-specific threshold.
- **Review:** evidence is mixed or the possible harm is meaningful.
- **Abstain/escalate:** probabilities are diffuse, the input is out of scope, or the taxonomy has no suitable option.

Set higher thresholds for irreversible or high-impact actions. The model can inform a recommendation, but ordinary code must enforce the permitted action, account limits, identity checks, approval rules and rollback path.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-action-gate/README (inspected 2026-10-16)

## Failure cases to include in validation

- No listed option fits the input.
- The state contains contradictory facts.
- A negation or exception reverses a default label.
- The evidence is incomplete or ambiguous.
- The same record can plausibly satisfy two intents.
- A visual state includes tiny or overlapping text.
- The request includes an adversarial instruction embedded in user content.
- The model returns low/diffuse probabilities.
- Several question answers violate an application invariant.
- A rare class is highly consequential despite low frequency.

Use these cases to decide whether to ask more questions, create a review route, change the taxonomy or use a different model family. Do not blindly retry the same question until a preferred answer appears.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-ticket-triage/README (inspected 2026-10-16)

## Decide between model classes

- **Decider vs Jev:** both are semantic decision-model families, but model identity, API behavior, pricing, context and confidence handling differ. Compare official references and access constraints before choosing.
- **Decider vs chat generation:** choose Decider for typed probabilities; choose a general chat model when prose, explanation, coding or flexible conversation is required.
- **Decider vs retrieval/search:** if the state lacks current external evidence, retrieve first. A decision model is not itself a substitute for web search.
- **Decider vs tabular prediction:** choose TabPFN or TabICL for structured labeled rows and predictive learning, not for natural-language rules over arbitrary state.
- **One-stage vs two-stage:** a decision model can route an input to a more expensive generative/research model only when the router has been tested for the cost of misses.

The OpenRouter signal in the catalog supports only a limited platform-traffic observation. It cannot decide which of these model classes is best for a user's actual workload.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://openrouter.ai/rankings?benchmark=intelligence (inspected 2026-10-16)

## What to report in a selection answer

When recommending Decider, make the reasoning inspectable:

- Identify the concrete decision shape and matching primitive.
- Quote the versioned model ID, not an unverified alias.
- Explain that the response is structured probabilities, not prose.
- State input price and that output is free in the inspected price table.
- Mark context limit unknown where the source does not publish one.
- Distinguish the model's own API access from other Perplexity APIs and router traffic.
- Describe the OpenRouter adoption signal only as scoped platform traffic.
- Recommend calibration, thresholding and an explicit abstention path.
- Keep policy and authorization in application code.
- Name a nearby alternative if the user actually wants chat, search synthesis or tabular prediction.

Do not promise that the model's probabilities are calibrated for the user's data until that has been tested. State what evidence and metric would change the selection.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/getting-started/pricing ; https://openrouter.ai/rankings?benchmark=intelligence (inspected 2026-10-16)

## Calibration evidence to collect

Keep a held-out set that reflects the real class balance and decision costs. Report performance by question type and important slices, not only one aggregate score. Useful measures include precision/recall at the chosen threshold, false-positive and false-negative rates, calibration error and the percentage sent to review.

If the taxonomy changes, version the question text, options and rubric with the dataset. Re-run the evaluation when adding a new choice, changing a definition or changing how missing evidence is handled. A probability from one prompt design should not be treated as transferable to a different rubric.

Record abstention and human override outcomes. These show whether the model is usefully uncertain, whether reviewers add signal, and whether automation thresholds should change. Do not tune on the final evaluation set.

> Source: https://docs.perplexity.ai/docs/decisions/quickstart ; https://docs.perplexity.ai/docs/cookbook/examples/decisions-api-ticket-triage/README (inspected 2026-10-16)

## Sources

- https://docs.perplexity.ai/docs/decisions/quickstart
- https://docs.perplexity.ai/docs/getting-started/pricing
- https://docs.perplexity.ai/docs/resources/changelog
- https://openrouter.ai/rankings?benchmark=intelligence

Fetched: 2026-10-16
