# Grok Code Fast 1 / Grok Build 0.1 (`grok-build-0.1`)

Status: active in the inspected xAI catalog as of 2026-10-16. Release date: unknown. The exact canonical model name shown in the API model page is `grok-build-0.1`. The marketed/API alias is `grok-code-fast-1`.

## Canonical ID and aliases

The model page lists these aliases for the same identity: `grok-code-fast-1`, `grok-code-fast`, and `grok-code-fast-1-0825`. Do not count these aliases as separate models or assume that a similar future alias is the same checkpoint without rechecking the official catalog. Use `grok-build-0.1` for canonical catalog comparison; use a currently documented alias when the API integration requires that public name.

> Source: https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Capability, limits and cost

xAI positions this model for agentic coding, software engineering and workflow tasks. The model page describes text and image inputs, text output, function calling, structured outputs and reasoning. Context window is 256,000 tokens. Requests above 200K are charged at higher-context rates, so compare a long coding-context workload using the applicable rate row rather than only the base rate.

At the inspected US-region listing, the rates are $1.00 per million input tokens, $0.20 per million cached input tokens and $2.00 per million output tokens. Batch API is listed as unsupported. The page lists 37 requests per second and 10M tokens per minute for that selected region; account limits are subject to change and should be checked in the live console. The page exposes other clusters/regions, so the quoted rates should not be presented as a worldwide fixed price.

> Source: https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Availability, licensing and evidence

Availability: xAI API in the regions listed on the model page, including US East and US West in the inspected page. Confirm current access, rate limits and regional pricing. License: proprietary hosted API; public self-hosted weights were not identified. Adoption: xAI did not publish model-level usage/download telemetry in inspected official pages. Do not infer popularity from the name, launch freshness or company-wide consumer reach.

> Source: https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Choose it when

Prefer this model for coding-focused agents, repository work, software engineering and workflow automation when its task quality meets the evaluation target. It has a lower listed base input/output rate and a smaller context budget than Grok 4.7. Use Grok 4.7 for broader general work or when the larger context/reasoning choice matters. This is a use-case distinction, not proof that one is more accurate on a specific coding benchmark.

The model supports function calls, but the application still owns authorization, tool validation and action policy. A model's ability to propose a tool call does not make its action safe. Keep tests, approvals and least-privilege controls in the harness/application.

> Source: https://docs.x.ai/developers/models/grok-code-fast-1 ; https://docs.x.ai/developers/models (inspected 2026-10-16)

## Budget and lifecycle checklist

1. Check whether prompt and repository context cross 200K; higher-context pricing applies after that threshold.
2. Estimate cached and uncached input separately, then output tokens and any separately metered tools.
3. Pin one canonical ID/alias and record the region used. Avoid assuming alias stability without checking the model catalog.
4. Confirm batch support before building an offline queue; this model's detail page says batch is unsupported.
5. No release date or retirement date was established by the inspected page. Recheck official release notes and catalog for status changes.

> Source: https://docs.x.ai/developers/models/grok-code-fast-1 (inspected 2026-10-16)

## Sources

- https://docs.x.ai/developers/models/grok-code-fast-1
- https://docs.x.ai/developers/models

Fetched: 2026-10-16
