# Jev 1.14 (current) and the SDK releases that target it

Read this when you are pinning a model id, checking where an alias points, upgrading an SDK, or deciding whether a feature (Box, images, long context) works on the version you call. For 1.13-only facts see `jev-1.13.md`.

## Model

> Source: https://docs.typesafe.ai/models.md
> Source: https://docs.typesafe.ai/changelog.md

| | Jev 1.14 | Jev 1.13 |
|---|---|---|
| Model id | `jev-1.14.0` | `jev-1.13.0` |
| Released | "Available from October 14, 2026" | not stated (launch 2026-09-15) |
| Status | "Newest Jev release" | still callable; no deprecation date listed |
| Price | $0.042 per 1M input tokens ($42 per billion); output free | same |
| Context (default) | 64k per request, 32k per question | same |
| Context (opt-in) | 262k for both, with `TypeSafe-Danger-Zone-Long-Context: true` | same ("also works on Jev 1.13") |
| Input | Text, PNG/JPEG images (images need `TypeSafe-Danger-Zone-Images: true`) | same ("also works on Jev 1.13") |
| Question types | Choice, Score, Noul, **Box** | Choice, Score, Noul |

Changelog entry for Jev 1.14 (the page's only entry): better multilingual support; new Box question type (needs 1.14); images in `state`, `instructions` or `criteria`; long-context header.

- No newer model was found: models.md, changelog.md, llms.txt and the blog index list nothing past `jev-1.14.0` as of 2026-11-13. That is absence from fetched pages, not a vendor statement.
- Audio and video input are not supported on either version.

## Aliases

> Source: https://docs.typesafe.ai/models.md
> Source: https://typesafe.ai/blog/jev-1-14 (vendor blog)

- `jev-latest` → `jev-1.14.0`: "Most recent stable official release and the SDK default."
- `jev-preview` → `jev-1.14.0`: no preview build is currently available, so it matches `jev-latest`.
- `GET /v1/models` lists the aliases; versioned ids are accepted whether or not they appear in the list.
- The blog announced 1.14 under `jev-preview` first, with `jev-latest` to move "in about a week". **The date the alias actually moved is undocumented.** Treat models.md (current state) as authoritative over the blog (point-in-time).
- The JS SDK docs still say to use `jev-preview` for Box. Both aliases resolve to 1.14.0 today; pin `jev-1.14.0` instead of relying on either alias.
- Third-party pages lag: Netlify's changelog documents `jev-latest` as 1.13.0, Cloudflare's `typesafe/jev` card is 1.13, and DigitalOcean lists only 1.13.0. See `../purchase-routes.md`.

## Deprecation intent (not yet a policy)

> Source: https://typesafe.ai/blog/jev-1-14 (vendor blog)

- 60 days' notice before `jev-1.13.0` is deprecated; 30 days for `jev-1.14.0`.
- `jev-1.13.0` "stays available for a while."
- A formal deprecation policy is "promised but not yet published."

## What 1.14 does NOT have

> Source: https://docs.typesafe.ai/model-jaggedness.md
> Source: https://docs.typesafe.ai/llms.txt

- **No jev-1.14 jaggedness page exists.** `https://docs.typesafe.ai/model-jaggedness/jev-1.14.md` and `.../jev-1.14` both return 404; llms.txt lists only the unversioned `/model-jaggedness.md`. Never invent 1.14-specific weaknesses beyond what the sources below state.
- Vendor-stated 1.14 caveats (blog): multimodal is worse than text-only; reliability drops on longer contexts; the Danger-Zone features (images, Box, long context) have "way too much jaggedness" for production; internal benchmark numbers are a "best guess" and likely biased toward TypeSafe's models.
- Third-party data on 1.14 (community, unverified by TypeSafe): see `../limitations-and-security.md` (issues #17 and #19).

## Python SDK `typesafe-sdk`

> Source: https://pypi.org/pypi/typesafe-sdk/json
> Source: https://docs.typesafe.ai/sdk/python/changelog.md

| Version | Date (PyPI UTC) | Change |
|---|---|---|
| **0.7.5** | 2026-10-14 | **zstd request compression ON by default** ("non-official APIs may not support it yet"); `Image` assets from bytes, path, base64 or PIL; `Box` questions and answers; `attach_assets`. |
| 0.7.4 | 2026-10-09 | Non-finite numbers serialized as strings instead of invalid JSON. |
| 0.7.3 | 2026-10-09 | Async crash with `truststore<=0.10.4` fixed; pooled connections kept alive 30 s. |
| 0.7.2 | 2026-09-26 | `http2` extra. |
| 0.7.1 | 2026-09-21 | API key validated early and kept out of logged exceptions. |
| 0.7.0 | 2026-09-18 | **Breaking**: `msgspec` → `pydantic`; adds `response_model=`. |
| 0.6.0 | 2026-09-15 | **Breaking**: `Score.criteria` is an ordered sequence, not an int-keyed dict. |
| 0.5.7 | 2026-09-11 | First public release (changelog says 09-14 and GitHub 09-12; PyPI upload time wins). |

Python ≥ 3.10. Extras: `http2`, `pil`, `zstd` (install `typesafe-sdk[zstd]` on Python < 3.14).

## JS SDK `@typesafe-ai/sdk`

> Source: https://registry.npmjs.org/@typesafe-ai/sdk
> Source: https://docs.typesafe.ai/sdk/javascript/changelog.md

| Version | Date | Change |
|---|---|---|
| **0.7.0** (`latest`) | 2026-10-14 | **Breaking**: Node.js ≥ 22; request payload types no longer exported. Adds experimental images (`image()`, `Image.fromBase64()`, `withAssets`, `assets`), `box` questions, zstd for bodies ≥ 1 KiB on Node 22.15+ (`compression: false` opts out). Invalid requests now reject the promise instead of throwing. |
| 0.6.0 | 2026-09-15 | **Breaking**: `Score.criteria` ordered sequence. |
| 0.5.7 | 2026-09-11 | First public release. |
| 0.0.0-bootstrap.0 | — | `bootstrap` dist-tag placeholder; never install it. |

- The quickstart still says Node 20+; npm `engines` and the SDK page say ≥ 22. Trust npm.
- The two SDKs are now near parity on images and Box but still differ: Python has `response_model`, JS has none documented. Never assume version-number parity.

## Agent skill package

> Source: https://github.com/typesafe-ai/skills/commits/main

TypeSafe's own `typesafe-ai/skills` repo shipped "Release v0.6.2" on 2026-10-23, and its SKILL.md targets Jev 1.14 (Box, companion Noul). Its version number is unrelated to the SDK numbers.

## Sources
- https://docs.typesafe.ai/models.md
- https://docs.typesafe.ai/changelog.md
- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/model-jaggedness.md
- https://docs.typesafe.ai/model-jaggedness/jev-1.14.md (404)
- https://typesafe.ai/blog/jev-1-14 (vendor blog)
- https://pypi.org/pypi/typesafe-sdk/json
- https://pypi.org/project/typesafe-sdk/
- https://docs.typesafe.ai/sdk/python/changelog.md
- https://github.com/typesafe-ai/typesafe-sdk-python/releases
- https://registry.npmjs.org/@typesafe-ai/sdk
- https://docs.typesafe.ai/sdk/javascript/changelog.md
- https://docs.typesafe.ai/sdk/javascript.md
- https://github.com/typesafe-ai/skills/commits/main

Fetched: 2026-11-13
