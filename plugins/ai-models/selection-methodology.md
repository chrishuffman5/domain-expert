# Selection methodology

## Purpose and scope

This catalog is a curated, popularity-weighted set of 60 model identities as of 2026-10-16 UTC. It is not an exact global ranking, an exhaustive inventory, or a quality leaderboard. It aims to cover models people can choose among for current general language work, reasoning, coding, multimodal tasks, open-weight deployment and specialist decision workloads. The portfolio is selected evidence-first; no fixed broad/emerging/specialist quotas or numeric ranks are imposed. Specialists are included only for distinct requested coverage, and every such exception is called out rather than disguised as adoption evidence.

Popularity means documented evidence of use or distribution within a stated scope. It is distinct from capability, benchmark quality, safety and suitability for a specific workload. Each entry has `evidence_class` (`observed`, `proxy`, or `unknown`), its underlying signal and limitation in `adoption`, and an individual `selection_reason`. It does not calculate one composite score because tokens, downloads, stars, customer anecdotes and API availability do not share a meaningful unit.

## Evidence in the selected set

At this snapshot, 5 of 60 entries are classified as `observed`: each has a public OpenRouter traffic observation, which is measured but scoped only to public traffic routed through that platform and its stated window. 19 entries are `proxy`: examples include Hugging Face download or engagement counters, GitHub stars, Spaces/integrations, and vendor-displayed cumulative figures. These proxies have different units and coverage and were not numerically ranked against each other. The remaining 36 entries are `unknown` because inspected sources did not establish a comparable public usage/distribution signal. Unknown is not zero and does not mean the model is unpopular.

The observed subset materially informed selection: platform-visible models such as GPT-6 Luna, GPT-5.6 Luna, DeepSeek V4.1 Flash, GLM 5.3 Flash, and Perplexity Decider V1.1 27B received concrete inclusion support from that measured scope. Open-weight candidates with inspectable repository/download/community signals were considered as weaker proxies. The many unknown entries were retained only where the catalog also needed a current provider tier, an active distinct capability or modality, or a requested specialist category. Their reasons say that explicitly; current availability and breadth are coverage rationales, not proof of popularity. The selected set is therefore popularity-weighted where compatible evidence exists, but public telemetry coverage is too uneven to claim most-used global ordering.

## Evidence hierarchy

Researchers should search current provider material and open the actual official source before recording model facts. For each model, record the exact provider-facing identity, source URLs, retrieval date, release/status, capabilities, context/output limits, pricing and billing conditions, availability, license, strengths and limitations. Use `unknown` when an official source does not establish a field.

| Evidence class | Acceptable signal | What to preserve | Limitation |
|---|---|---|---|
| Direct provider usage | Model-specific requests, tokens, active users/accounts, or production use published by the provider | Provider, model/version, count/unit, period, date, source | Definitions and reporting coverage can differ; providers rarely disclose full telemetry |
| Platform usage | Transparent API/router telemetry such as public OpenRouter token totals | Exact model variant, traffic source, prompt+completion unit, complete UTC window and latest bucket | Covers only traffic routed through that platform; excludes private, direct-provider and other-platform use |
| Distribution | Official model-repository downloads or package downloads | Exact repository/package, measure/window, date, source | Downloads are requests, not unique users or active deployments; mirrors, caches and automation affect counts |
| Discovery / interest proxy | Stars, likes, forks, dependents, integrations or public case studies | The exact counter/claim, source/date and its limited meaning | Weak proxy with no common denominator; does not prove runtime use |
| Unknown | No comparable public signal was found in inspected sources | Explicit unknown plus the scope searched | Unknown does not mean zero usage or low quality |

Only compare numbers within compatible evidence classes, platform scopes and time windows. OpenRouter rankings measure traffic routed through OpenRouter, not all provider traffic, user counts, spend, preference or model quality. Hugging Face downloads are distribution requests and may include repeated or automated fetches. Stars, likes and integration counts are interest indicators rather than usage. Availability alone is not adoption.

## Curation process

1. **Define the model identity.** Start from a provider's current model catalog, official model card or release notice. Use the exact inspected identity appropriate to the source: this may be a provider model ID, checkpoint repository ID, or release name. The `identity_kind` and `callable_id` fields distinguish identity from endpoint syntax. Mark aliases and deployment/profile IDs as references when they route to the same underlying model.
2. **Deduplicate.** Count the underlying model once across aliases, API endpoints, regions, hosted wrappers, quantizations and mirrors. Keep separately versioned tiers/releases only when the model identity materially differs; do not turn every version, speed mode or deployment route into another model.
3. **Collect current evidence.** Record official-source availability and technical claims. Search for dated adoption signals, then preserve their units and scope. Verify the model's lifecycle status and release date rather than inferring them from a page's modified date or a model name.
4. **Assemble a broad-use pool.** Prefer actively offered, observed-use models where there is credible evidence. Retain an older release when it has a transparent ongoing-use signal or a distinct established deployment role. Recency and capability breadth may break ties but do not substitute for use evidence.
5. **Reserve specialist coverage.** Include decision models such as Jev when needed for the user's requested domain, even when public usage is unknown. Keep typed semantic decision models distinct from chat models, and keep predictive tabular foundation models distinct from general prompt-to-decision systems. Record this as deliberate category coverage, not a claim that they rank highly in broad LLM usage.
6. **Check portfolio balance.** Review coverage after the evidence-based shortlist to avoid redundant identities and retain genuinely distinct current tasks or modalities. Do not backfill with marginal entries to hit a quota. Explain any included entry whose use signal is unknown in its `selection_reason`.
7. **Review and maintain.** On each refresh, re-check canonical IDs, active/deprecated status, rates, limits, license terms and source links. If public evidence is missing or the source does not define a field, retain `unknown`. Record exclusions and overlaps in the research workspace.

The proxy set includes repository/download/community counters and vendor-displayed aggregate figures; qualitative availability alone is classified unknown. Every entry is also annotated with `identity_kind` and `callable_id` so a checkpoint or release name is not presented as a universal endpoint.

## Decision and specialist model treatment

The catalog includes three distinct specialist shapes:

- **Semantic decision models** such as Jev and Perplexity Decider take supplied state plus declared questions and return typed answers/probabilities. They are useful for software-controlled classification, routing or rubric decisions; they do not replace an application's action policy or safety controls.
- **Predictive tabular foundation models** such as TabPFN and TabICL take labeled tabular examples and predict labels or values for new rows. Their strengths, data assumptions and operating limits differ from general language models.
- **Other specialist models** (for example audio or embedding models) should be selected by modality/task rather than included in a generic text-tier ladder.

Popularity evidence for these categories is not directly comparable with general LLM token-volume rankings. A deliberate specialist allocation is a coverage choice and must remain clearly labeled.

## What this catalog does not claim

The set does not establish a universal “best” model, relative benchmark superiority, or global usage order. It does not cover every active model or guarantee future API availability. Adoption is unevenly observable across providers, regions and deployment modes, and model-level usage is unknown for many entries. Cited rates and lifecycle details are snapshots; provider terms and availability can change. For production decisions, re-open the linked provider source and run workload-specific evaluations.

## Method sources

- OpenRouter [model rankings and scope](https://openrouter.ai/rankings?benchmark=intelligence)
- OpenRouter [daily token totals dataset/API](https://openrouter.ai/docs/api/api-reference/datasets/daily-token-totals-for-top-50-models)
- Hugging Face [model download statistics](https://huggingface.co/docs/hub/models-download-stats)
- Hugging Face [publisher analytics](https://huggingface.co/docs/hub/publisher-analytics)
- Provider-specific facts and usage claims are sourced in the per-family references and `catalog.json`.

Fetched: 2026-10-16 UTC.
