---
name: tabpfn
license: MIT
description: "Select TabPFN for supervised classification or regression on labeled structured tables when in-context tabular prediction fits dataset, compute, and licensing constraints. Use this skill for task fit, checkpoint limits, evaluation, and adoption evidence. Do NOT use for typed semantic judgments over free-form state (use jev-system-one), for TabICLv2 model selection (use tabicl), or for API/SDK integration, provider routing, harnesses, or eval infrastructure (use the existing ai guidance); do NOT use as a general language model."
---

# TabPFN selection

## Model role

TabPFN is a family of pretrained tabular predictors. A fitted classifier or regressor receives a labeled training table and predicts target values for test rows. It is relevant when the problem is supervised prediction over structured features, not when the application needs a model to interpret arbitrary natural-language state and return a caller-defined semantic answer.

TabPFN is not a large language model and does not generate explanations or free-form responses. It can contribute a class probability or regression output to a decision system, but the product owner still defines the target, data pipeline, threshold, actions, and review path.

The catalog identity is TabPFN-3.5, the current default described in the official repository at the 2026-10-16 snapshot. TabPFN-3.5 uses one multitask checkpoint for classification and regression according to the repository. Do not confuse this identity with older TabPFN versions, Fast variants, experimental checkpoints, the API/client offering, or downstream distilled enterprise products.


> Source: https://github.com/PriorLabs/tabpfn

## When to shortlist it

Shortlist TabPFN when:

- The target is a supervised classification or regression outcome.
- Labeled rows are available and representative of deployment cases.
- The data can be expressed as a feature matrix with a well-defined target.
- Dataset size and feature count fit the selected checkpoint and hardware.
- A pretrained in-context learner is worth benchmarking against standard tabular baselines.
- The applicable weight/API license permits the intended use.

Do not select it just because a task involves a table. Rule lookup, aggregation, forecasting, causal inference, ranking, clustering, policy interpretation, and natural-language decision questions require different methods or explicit task-specific evaluation. The repo describes extension projects for other capabilities; do not treat those as the base TabPFN-3.5 contract.

A credible comparison includes at least a well-tuned tree-based baseline and a simple baseline such as logistic/linear regression where applicable. Include the operational cost of building and maintaining features and training pipelines. A model that wins one benchmark may lose on a different population, objective, or latency constraint.


> Source: https://github.com/PriorLabs/tabpfn

## Identity and version control

Use the exact checkpoint identity for any reproducible evaluation. The official Python package defaults to TabPFN-3.5 on the retrieved snapshot. Pin package, checkpoint, and preprocessing code for a benchmark; record the version in model artifacts and prediction logs.

The repository lists TabPFN-3.5-Fast separately as a smaller, faster model. Compare it on the same split and operational target if latency is important; do not assume the Fast suffix preserves accuracy or matches the default. Experimental variants are explicitly not recommended as the first choice by the repository and can be worse on average.

Older model weights have distinct terms and behavior. Repository claims about the v2 license must not be transferred to the 3.5 weights, and vice versa. Existing reports should state which version they evaluated rather than using “TabPFN” without a checkpoint qualifier.


> Source: https://github.com/PriorLabs/tabpfn

## Dataset and resource fit

The official repository says TabPFN-3.5 and TabPFN-3.5-Fast accept up to 1,000,000 rows and 20,000 features. Treat these as checkpoint guardrails, not a promise of a particular latency, memory footprint, predictive accuracy, or throughput. CPU and GPU limitations differ; the repository recommends GPU use and notes large CPU workloads can be slow.

Inspect the specific checkpoint documentation and hardware before approving a deployment. Measure peak memory, fit and prediction time, batch size, concurrency, cold weight download, warm-cache behavior, and recovery after worker restart. Do not infer feasible production scale from the maximum row count alone.

The repository's basic guidance says to batch test predictions rather than calling each row separately, avoid scaling or one-hot encoding, and use a GPU for better speed. Verify such preprocessing advice against the exact package version, task, and benchmark design. Preserve an untouched evaluation set so pipeline choices are not tuned against test outcomes.

Check data types, missingness, categorical representations, rare labels, duplicates, leakage, target timing, and train/test drift. Keep entities or time periods grouped in splits when random row splits would leak correlated information. For temporal deployment, test on later periods. For repeated entities, test on held-out entities or an appropriate production-like split.


> Source: https://github.com/PriorLabs/tabpfn

## Evaluation and decision use

Define an objective metric that matches the product loss. Accuracy alone can hide rare-class failures; choose precision/recall, ROC/PR measures, log loss, calibration, expected cost, or regression error according to the task. Report uncertainty intervals across multiple splits where feasible, along with subgroup performance and coverage.

If downstream code thresholds predicted probabilities, evaluate calibration on the deployment distribution and recalibrate only using training/validation data. A model score is not an action policy. Set thresholds with the costs of false positives, false negatives, abstentions, manual reviews, and delayed decisions made explicit.

For high-impact choices, use independent deterministic checks or human review. Validate feature freshness and provenance, prevent post-outcome fields from leaking into the model, and monitor drift after launch. Ensure operators can identify the checkpoint and data version behind an output.

When training data are small, compare TabPFN with simple regularized estimators and tree models using nested or otherwise leakage-safe validation. When data are large, benchmark both runtime/memory and accuracy at operational scale, not only a convenient small subset. If the task distribution differs from public benchmark datasets, treat benchmark positioning as a hypothesis to test.


> Source: https://github.com/PriorLabs/tabpfn

## License, availability, and cost

The repository says code is Apache-2.0, while TabPFN-3.5 weights use a separate non-commercial license. Commercial production requires checking the exact weight license and applicable commercial terms; Prior Labs describes an enterprise edition and commercial enterprise license. API use and hosted offerings have terms distinct from the downloadable weight license.

The catalog records pricing as unknown/contract-specific because no fixed public per-token rate was established in the inspected sources. Confirm the current hosted API, private cloud, or enterprise price and service terms directly with Prior Labs before budgeting. For local inference, account for GPU/CPU hardware, storage, dependency maintenance, and model download/authentication requirements.

Do not assume open-source code grants commercial weight rights. Do not assume a hosted API's terms are the same as a local model license. Keep a license review attached to the exact checkpoint and deployment route.


> Source: https://github.com/PriorLabs/tabpfn
> Source: https://priorlabs.ai/pricing

## Adoption and portfolio context

Prior Labs' official homepage displayed 8K GitHub stars and 4M downloads when inspected on 2026-10-16. The page does not define a measurement period, unique-user count, current active use, or per-checkpoint split. These vendor-displayed figures are cumulative or otherwise time-undefined discovery/distribution proxies, not active inference telemetry or quality evidence.

The signal supports including TabPFN as an established open tabular ecosystem candidate, but it cannot be compared numerically with hosted token volumes or another project's repository stars. The model is included in a popularity-weighted catalog with an explicit scope caveat, not as a claim that it ranks above models with direct usage evidence.


> Source: https://priorlabs.ai/

## Alternatives and boundaries

- **TabICL:** consider a separately implemented open tabular learner with public repository and model card; compare dataset scale, runtime, package behavior, licensing, and validation results on the same data.
- **Jev System One:** choose for semantic judgments from caller-provided text or structured state with typed Choice, Score, or Noul outputs; not as a replacement supervised table learner.
- **Tree ensembles or linear models:** retain as strong task-specific baselines and potentially preferable deployment choices.
- **Generative LLMs:** use only when the task needs language understanding/generation that a table target does not express; do not treat prose classification as equivalent to trained supervised prediction without evaluation.

This skill covers selection and technical tradeoffs. Existing `ai` integration skills own APIs, clients, authentication, provider routing, deployment mechanics, and troubleshooting.


> Source: https://github.com/PriorLabs/tabpfn

## Selection checklist

1. State the prediction target, unit of analysis, and time at which features are available.
2. Confirm the data are labeled and the intended task is supported classification or regression.
3. Record the exact TabPFN checkpoint, package version, license, and intended deployment route.
4. Check row/feature guardrails and profile hardware requirements with realistic batches.
5. Create leakage-safe train, validation, and final test splits aligned to deployment.
6. Compare with simple and strong tabular baselines using task-appropriate metrics.
7. Assess calibration, subgroup errors, drift risks, and the effect of thresholds.
8. Calculate total operating cost, including license, hardware, API contract, and maintenance.
9. Define human review or deterministic fallback for uncertain or high-impact outputs.
10. Pin the validated checkpoint and rerun evaluation after changes to model, package, features, or population.


> Source: https://github.com/PriorLabs/tabpfn

## Benchmark protocol details

Write an experiment plan before inspecting final test results. Record the target population, data exclusions, split rules, metrics, model comparisons, acceptance threshold, and the cost of errors. This reduces the temptation to choose a favorable measure after the fact.

Keep the final test set untouched until model and threshold choices are fixed. Repeatedly selecting among variants on one holdout can overfit the benchmark process even when the underlying model is pretrained.

Use the same rows and feature-availability assumptions for each baseline. If production receives delayed, missing, or stale features, recreate those conditions in evaluation rather than testing on an unusually clean historical table.

Report metrics by important cohorts and operational strata, with sample support counts. Have domain reviewers inspect false positives and false negatives, but do not tune against final test labels.

For probability-based actions, inspect reliability by score band and relevant subgroup. Global calibration can conceal subgroup miscalibration. If recalibration is needed, fit it on training/validation data and evaluate it independently. Keep ranking quality distinct from probability quality.


> Source: https://github.com/PriorLabs/tabpfn

## Production-readiness review

Record feature names, type constraints, missing-value behavior, category handling, and target definition. Add schema checks so upstream changes fail clearly instead of silently changing predictions.

Profile first-use behavior separately from steady state. The package can download weights on first use, so deployment needs a plan for authentication, network access, caching, artifact provenance, and cold-start latency.

Test resource contention. One GPU benchmark does not establish concurrent production capacity. Measure batch sizes, workers, peak memory, and out-of-memory behavior; set backpressure or queue limits. Keep CPU fallback only if its latency and quality meet requirements.

Define the fallback for unavailable checkpoints, unsupported inputs, schema errors, and degraded quality. Depending on consequence, use an incumbent model, review queue, or safe abstention.


> Source: https://github.com/PriorLabs/tabpfn

## License and governance questions

Review the exact checkpoint and current terms against the intended activity and distribution pattern. Ask whether use is commercial, internal, research, or evaluation; whether the weight terms permit it; and whether a hosted service has distinct data processing, residency, retention, or SLA conditions.

Check dependency licenses and whether a commercial enterprise license or support agreement is required. Identify who can approve a checkpoint or serving-route change. If terms are unclear, leave commercial launch unresolved for legal/procurement review.

A code license does not grant commercial weight rights. A package being installable does not authorize every deployment route.


> Source: https://github.com/PriorLabs/tabpfn

## Record what was selected

Keep a deployed-model record with intended and excluded uses, checkpoint identity, evaluation data and splits, limitations, threshold policy, fallback, owner, and version. Include why TabPFN was selected and what adoption signal supported shortlisting.

Refresh this record when the checkpoint, package, feature pipeline, population, license, or hosted offer changes. Put exact model identity in logs and dashboards rather than documenting it only in setup instructions.


> Source: https://priorlabs.ai/

## Sources

- The TabPFN-3.5 identity, license, limits, and official adoption proxy are recorded in the model reference.

Fetched: 2026-10-16
