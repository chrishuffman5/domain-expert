# Jev 1.13 and the SDK releases that target it

Read this when you are pinning versions, upgrading an SDK, or checking whether an alias has moved.

## Model

> Source: https://docs.typesafe.ai/models.md
> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/

- **The only documented model is `jev-1.13.0`.** No earlier version or deprecation notice is published.
- `jev-latest` is the stable alias and the SDK default. It currently resolves to `jev-1.13.0`.
- `jev-preview` is "currently identical; no preview available".
- The Cloudflare `typesafe/jev` id returns `jev-1.13.0` in the model card examples.
- Pin `jev-1.13.0` for anything audited or gated, and log `response.model` on every call. Aliases can roll forward. The community reports that the Cloudflare response version may differ from the request (https://aiengineerguide.com/til/typesafe-ai-jev-cloudflare-ai-gateway/).
- Limits and pricing for this version: see `../pricing-limits-errors.md`.
- Known weaknesses: see `../limitations-and-security.md`. The jaggedness page is per version, so re-check it on every model bump.
- Public launch was 2026-09-15, into early access (source: https://typesafe.ai/blog/introducing-system-one-models-and-jev).

## Python SDK `typesafe-sdk`

> Source: https://pypi.org/project/typesafe-sdk/
> Source: https://github.com/typesafe-ai/typesafe-sdk-python/releases

| Version | Date | Change |
|---|---|---|
| 0.5.7 | 2026-09-11 | First public release. The prose changelog says 2026-09-14; PyPI and GitHub say 09-11. |
| 0.6.0 | 2026-09-15 | **Breaking**: `Score.criteria` became an ordered sequence instead of an int-keyed dict. Also: better HTTP error messages, `RetryPolicy` validation fixes, and picklable exceptions. |
| 0.7.0 | 2026-09-18 | **Breaking**: serialization moved from `msgspec` to `pydantic`. Adds `response_model=` to `system_one()`. |
| 0.7.1 | 2026-09-21 | Validates the API key early and **keeps the key out of logged exceptions**. Adds AI-gateway doc examples. |

Use Python SDK ≥ 0.7.1. Earlier versions could surface the key in exception logs.

## JS SDK `@typesafe-ai/sdk`

> Source: https://registry.npmjs.org/@typesafe-ai/sdk
> Source: https://github.com/typesafe-ai/typesafe-sdk-js/releases

| Version | Date | Change |
|---|---|---|
| 0.0.0-bootstrap.0 | — | A placeholder under the `bootstrap` dist-tag: "not a functional SDK". Never install it. |
| 0.5.7 | 2026-09-11 | First public release. |
| 0.6.0 | 2026-09-15 | Current `latest`. **Breaking**: `Score.criteria` became an ordered sequence, matching Python 0.6.0. |

The JS SDK has no equivalent yet of Python's 0.7.x (pydantic-style typing and the key-in-logs fix). This comes from comparing the registries; the vendor has not explained it. **Never assume version parity between the two SDKs.**

## Sources
- https://docs.typesafe.ai/models.md
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://pypi.org/project/typesafe-sdk/
- https://github.com/typesafe-ai/typesafe-sdk-python/releases
- https://docs.typesafe.ai/sdk/python/changelog.md
- https://registry.npmjs.org/@typesafe-ai/sdk
- https://github.com/typesafe-ai/typesafe-sdk-js/releases
- https://docs.typesafe.ai/sdk/javascript/changelog.md
- https://aiengineerguide.com/til/typesafe-ai-jev-cloudflare-ai-gateway/ (community)

Fetched: 2026-09-23
