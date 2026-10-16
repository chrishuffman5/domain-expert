# Grok 4.7 (`grok-4.7`)

Status: active in the inspected xAI model catalog as of 2026-10-16. Release date: unknown. The model-list page carried a 2026-09-21 page-update date; that is catalog freshness metadata, not a verified release date. Canonical API ID: `grok-4.7`.

## Capability and limits

- Text and image input; text output.
- 500,000-token context window.
- Function calling and structured outputs are listed. Reasoning is supported with low, medium, high and xhigh effort; high is the documented default.
- Model positioning: xAI describes it as its flagship for coding, agentic tasks and knowledge work. Treat this as provider positioning, not a benchmark or independent ranking.
- Pricing shown for US East: $2.00 per million input tokens, $0.50 per million cached input tokens and $6.00 per million output tokens.
- xAI applies a higher-context rate once a request exceeds 200K tokens. The threshold changes the rate for the request; do not multiply the base rate over the whole request without checking the rate table for the selected cluster.
- Batch API is not supported on the inspected model page.
- The model page lists 150 requests/second and 50M tokens/minute for the selected region. These are regional account limits and can change; confirm the live console before relying on them.

> Source: https://docs.x.ai/developers/models/grok-4.7 (inspected 2026-10-16)

## Availability, identity, and licensing

The catalog lists xAI API access and a US East model detail page. The API model page also describes availability across clusters, so use its current region selector and pricing rows for a real deployment. This reference does not claim an AWS Bedrock, Google Cloud or Microsoft hosted endpoint. Availability through an API-compatible gateway, if offered by a gateway, does not change model identity and may expose different features or rates.

License: proprietary hosted API; no public weights or self-hosting license were identified in the inspected model docs. Adoption: no model-level usage or download count was published on the inspected official catalog. Do not use aggregate X/Grok consumer reach as API adoption evidence.

> Source: https://docs.x.ai/developers/models (inspected 2026-10-16)

## Selection guidance

Choose Grok 4.7 when the workload needs a general-capability xAI model with image input, tool use and configurable reasoning. It is the broader option against the code-specialist Grok Code Fast 1. Select effort intentionally: higher effort can be useful for difficult work but is not a guarantee of correctness or an accuracy score. For source-grounded current facts, pair it with a retrieval/search design and verify citations rather than assuming model knowledge is live.

Before budgeting, estimate request length and check whether any request crosses 200K. Include cached input, output, selected cluster and tool charges separately. Confirm rate-limit eligibility for the account. No batch discount is documented for this model because the model page states batch is unsupported.

Avoid selecting it solely because it is described as a flagship, and do not assume its prompt formats, reasoning controls, cache semantics, tools or exact prices carry over to another provider's API-compatible client. Compare on the user's representative tasks.

> Source: https://docs.x.ai/developers/models/grok-4.7 ; https://docs.x.ai/developers/models (inspected 2026-10-16)

## Migration and lifecycle checks

Use the pinned canonical ID when reproducibility matters. The catalog may evolve and xAI can update models or pricing independently; check the live models list, region selector, release notes and pricing before production changes. Do not promote a page-update date to a release date. No retirement date was published in the inspected source.

> Source: https://docs.x.ai/developers/models (inspected 2026-10-16)

## Sources

- https://docs.x.ai/developers/models
- https://docs.x.ai/developers/models/grok-4.7

Fetched: 2026-10-16
