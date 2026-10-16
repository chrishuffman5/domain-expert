---
name: tabicl
license: MIT
description: "Select TabICLv2 for supervised classification or regression on labeled structured tables when its open tabular model, local deployment, and scale fit. Use this skill to assess data fit, compute, licensing, validation, and adoption evidence. Do NOT use for semantic decisions over free-form state (use jev-system-one), for TabPFN checkpoint selection (use tabpfn), or API/SDK integration, provider routing, harnesses, or eval infrastructure (use the existing ai guidance); do NOT use for language generation or as a general model API guide."
---

# TabICLv2 selection

## Model role

TabICLv2 is an open tabular foundation model for supervised classification and regression. It uses labeled training rows and predicts targets for test rows through the TabICL implementation. It is not a conversational model, an arbitrary policy interpreter, or a replacement for Jev's caller-defined semantic decision primitives.

Use it where a structured table, target column, and deployment-like validation split are available. The model can return predictions that downstream systems use, but the application owns thresholds, business policy, and action authorization. Do not infer that an open model's output is inherently transparent or safe.

The catalog entry is TabICLv2. The official repository covers both TabICLv2 and the earlier TabICL project, so distinguish the paper/checkpoint family from the pip package and release tags. The candidate snapshot lists the current v2 line and notes the repository's latest visible package release as v2.2.0; the inspected release listing did not expose a dependable release year. Preserve that uncertainty rather than guessing a date.


> Source: https://github.com/soda-inria/tabicl

## When to shortlist it

Shortlist TabICLv2 when:

- The task is supervised tabular classification or regression.
- Labeled rows reflect the population and feature timing of expected use.
- Local or self-managed execution is important and the team can operate the runtime.
- The intended table size and hardware fit a tested inference configuration.
- You want to compare an open, in-context foundation model against strong classical baselines.
- The relevant code and checkpoint licensing have been reviewed for the intended use.

Do not select it for generic spreadsheet summarization, SQL/report generation, causal inference, arbitrary forecasting, semantic triage from unstructured text, or a decision that is fundamentally a deterministic rule. The repository offers optional extras and examples; they should not be treated as equivalent to the base classifier/regressor contract without separate evaluation.


> Source: https://github.com/soda-inria/tabicl

## Dataset scale and resources

The official repository reports benchmark experience on datasets with 300 to 100,000 training samples and up to 2,000 features. It says larger datasets, such as 500K rows, can be handled with CPU/disk offloading, with possible accuracy degradation. These are reported benchmark and scale observations, not a guarantee that every dataset in this range will fit, run quickly, or attain similar accuracy.

The repository recommends a GPU for larger datasets and documents fitting and predicting through a single forward pass. Optional key-value caching can speed repeated prediction over the same training rows, at the cost of additional memory. Measure the exact installation, hardware, cache mode, batch size, and cold-start behavior with realistic data.

Check peak memory and latency during both fitting and inference. Record whether the runtime uses GPU, CPU fallback, disk offload, or KV cache. Test whether latency and memory remain acceptable under concurrency and service restart. Caching or saving model state can involve training data or derived representations; treat those artifacts as sensitive and review the chosen persistence options.


> Source: https://github.com/soda-inria/tabicl

## Data and validation design

Define the target label, prediction timestamp, and feature availability before constructing a benchmark. Prevent leakage from post-outcome fields, duplicate entities across splits, target encodings that cross validation boundaries, or repeated observations from the same subject appearing in both train and test when deployment requires generalization to new subjects.

Choose splits that reflect production: chronological holdout for time-ordered use, grouped holdout for repeated entities, geographic or organization holdout when transfer matters, and a final untouched test set for reporting. Random splitting can overstate performance when rows are correlated.

Assess missingness, class imbalance, rare categories, label noise, outliers, cardinality, feature drift, and train/deployment differences. Document whether preprocessing is needed. Do not assume model defaults are correct for a particular data schema merely because a benchmark used similar row counts.

Compare against a simple baseline, a well-tuned classical tree ensemble, and any incumbent model. Use the same data splits, target definition, and metric. Include the time and expertise required to tune baselines. Vendor benchmark statements are evidence for shortlisting, not a substitute for local evaluation.

Select metrics that reflect loss. For classification, consider per-class precision/recall, PR-AUC for rare outcomes, log loss, calibration, and decision cost. For regression, report task-appropriate error measures and segment behavior. Show uncertainty across repeated splits or resamples where possible, and audit critical subgroups.


> Source: https://github.com/soda-inria/tabicl

## Predictions in decision workflows

Prediction quality and action quality are different. If predicted probabilities drive a threshold, evaluate calibration and threshold performance on data representative of the intended deployment. Set thresholds based on false-positive and false-negative costs, review capacity, and reversibility of the action.

For consequential decisions, add human review or authoritative rule checks. Make it possible to abstain, request more evidence, or fall back when the input is outside validated ranges. Monitor population drift, feature quality, calibration, missing inputs, and error rates after deployment.

Maintain an audit trail that identifies model checkpoint, package version, feature schema, training data snapshot, validation results, and policy version. Keep sensitive training data out of logs. If fitted-state saving or caching is used, assess retention, access controls, and deletion behavior.


> Source: https://github.com/soda-inria/tabicl

## Licensing, hosting, and price

The official GitHub repository describes the project as open source with a permissive license, and the official Hugging Face model card lists BSD-3-Clause. The inspected repository says there is no hosted inference provider listed for the model card. No public hosted price was found in inspected official pages because no official hosted inference offer was identified there.

Verify license terms for both code and the exact checkpoint distribution before commercial or regulated use. A permissive project description is not a substitute for reading the license file and any separate data, dependency, or checkpoint terms. Recheck the official sources at adoption time.

Local operation shifts cost to infrastructure and maintenance: GPU capacity if needed, storage for weights and caches, deployment packaging, monitoring, security updates, and staff time. Estimate total cost using a representative production workload rather than a single benchmark timing.


> Source: https://github.com/soda-inria/tabicl/blob/main/LICENSE
> Source: https://huggingface.co/jingang/TabICL

## Adoption evidence

The official GitHub repository showed 1.4k stars when inspected on 2026-10-16. This is a cumulative interest/discovery proxy, not a measure of active installations or production inference. The Hugging Face model card says downloads are not tracked and that the model is not deployed by an Inference Provider. The evidence therefore does not support a download-based or hosted-traffic rank.

TabICLv2 is selected for an open, distinct tabular prediction category with a visible research and implementation ecosystem. Its adoption evidence is weaker and less comparable than direct hosted token/request telemetry. Do not describe it as one of the most-used models on the basis of repository stars.


> Source: https://github.com/soda-inria/tabicl
> Source: https://huggingface.co/jingang/TabICL

## Alternatives and boundaries

- **TabPFN:** compare a separate pretrained tabular family whose current default has different checkpoint limits and non-commercial weight terms. Benchmark both with the same leakage-safe split and metric.
- **Jev System One:** use for semantic judgments over caller-supplied text/JSON state with typed Choice, Score, or Noul outputs. It does not require a supervised feature matrix.
- **Tree ensembles or linear models:** strong, often practical baselines; choose based on measured predictive quality, calibration, latency, operations, and license.
- **General LLM:** use for language generation or flexible semantic interpretation when those outputs are needed, not as an unvalidated substitute for a trained tabular predictor.

This skill covers model selection and tradeoffs. Existing `ai` guidance owns integration code, API mechanics, provider selection, and runtime troubleshooting.


> Source: https://github.com/soda-inria/tabicl

## Selection checklist

1. State the target, prediction unit, and timing of features.
2. Confirm the data are labeled and the task fits classification or regression.
3. Select a deployment-like split and guard against correlated-row leakage.
4. Test representative data near expected row/feature limits.
5. Measure GPU/CPU memory, latency, batch behavior, offload, and cache tradeoffs.
6. Compare with incumbent, simple, and strong classical baselines.
7. Assess calibration, subgroup results, drift, and action thresholds.
8. Review code, checkpoint, dependency, and data licenses separately.
9. Define fallback and human review for out-of-domain or high-impact cases.
10. Pin model/package/schema versions and rerun evaluation after any material change.


> Source: https://github.com/soda-inria/tabicl

## Benchmark protocol details

Define the prediction timestamp and the information available then. Build features as they would exist in production, including delayed fields and missing data. Keep transformations that learn from data inside training folds to avoid leakage.

Choose holdouts that resemble deployment. Group records by person, organization, site, or device when rows are correlated. Reserve later periods for forward prediction. If the model must generalize to new regions or cohorts, include those as holdouts.

Use an untouched test set for final reporting. Tune parameters, cache settings, feature processing, or hardware configuration only against validation data. Report the benchmark protocol, not only the best metric.

Compare a simple baseline, a strong classical model, and the incumbent on the same splits. Include predictive quality, calibration when relevant, fit/predict time, peak memory, artifact size, and operator effort. A speed claim is useful only when the candidate meets quality and governance requirements.

Inspect errors by class, target range, and important cohorts. For rare classes, report per-class performance and precision-recall behavior. For regression, inspect residuals by segment. Replicate results over multiple splits or periods where feasible.


> Source: https://github.com/soda-inria/tabicl

## Runtime and data stewardship

Profile the chosen GPU/CPU/offload setup. Repository-reported benchmark sizes do not establish behavior on every feature distribution or hardware configuration. Test expected row counts, upper-bound cases, concurrency, worker restarts, and cold checkpoint download.

The repository documents optional KV caching for repeated predictions on the same training data, with additional memory use. Benchmark cache build and reuse separately, and decide how cache artifacts are protected and deleted; derived state may encode information about training rows.

Review fitted-model serialization options. The official example allows decisions about saving weights, training data, and KV cache. Persist only the state needed for reproducibility and protect it according to source-data sensitivity.

Lock dependencies and record checkpoint provenance. Test clean installation and reload from saved state. Verify behavior on the deployment platform before relying on a cached or serialized estimator.


> Source: https://github.com/soda-inria/tabicl

## Project maturity and license checks

Read the exact code license and checkpoint terms. Check third-party dependencies separately; a repository description of “permissive” is not a substitute for legal review. The catalog keeps the release year unknown because the inspected release page did not establish it.

Review release activity, issue status, maintainer guidance, and upgrade path during adoption. Repository stars measure interest, not support guarantees or production maturity.

No official hosted inference provider was listed on the inspected model card. If a third party serves TabICL, assess that provider independently for version pinning, data handling, price, service limits, and contract terms. Do not attribute third-party terms to the model authors.


> Source: https://github.com/soda-inria/tabicl/releases
> Source: https://github.com/soda-inria/tabicl/blob/main/LICENSE

## Operational acceptance criteria

Set an acceptance envelope for dataset range, schema, quality floor, latency, memory, fallback, ownership, and alert conditions before launch. Include an out-of-range test so unsupported inputs fail visibly.

Build a regression set covering typical rows, boundary values, missing fields, rare categories, and known failure modes. Run it after package, checkpoint, or feature pipeline changes. Do not store sensitive examples in broad-access fixtures; use controlled synthetic or de-identified cases where practical.

Monitor input drift, missingness, output distribution, review overrides, and subgroup performance when labels become available. Changes can reflect data quality or population shift rather than model updates. Record checkpoint, code, schema, and evaluation data version for each result.


> Source: https://github.com/soda-inria/tabicl

## Sources

- The exact TabICLv2 identity, task, scale, license, and adoption limits are recorded in the model reference.

Fetched: 2026-10-16
