# Jev 1.13 (superseded by 1.14)

**Superseded.** `jev-1.14.0` is the current release and both aliases point to it; see `jev-1.14.md`. Read this file only when you must keep calling `jev-1.13.0`, or when a route still serves only 1.13.

## Model

> Source: https://docs.typesafe.ai/models.md
> Source: https://docs.typesafe.ai/changelog.md

- Model id `jev-1.13.0`. Same price ($0.042 per 1M input, output free) and default limits (64k request / 32k per question) as 1.14.
- Still callable as of 2026-11-13; no deprecation date is listed. The vendor blog promises 60 days' notice before deprecating it (https://typesafe.ai/blog/jev-1-14).
- **Works on 1.13**: images (with `TypeSafe-Danger-Zone-Images: true`) and the 262k long-context header ("Also works on Jev 1.13").
- **Does not work on 1.13**: Box questions. OpenRouter rejects Box on `typesafe/jev-1.13` with a 400 (https://openrouter.ai/blog/insights/what-is-jev/).
- 1.14's main stated gain over 1.13 is multilingual support (no measured numbers published).

## Where 1.13 is still the only or default version

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/
> Source: https://docs.digitalocean.com/products/inference/how-to/use-system-one-api/
> Source: https://www.netlify.com/changelog/typesafe-jev-ai-gateway/

- Cloudflare `typesafe/jev` is 1.13; use `typesafe/jev-1.14.0` for 1.14.
- DigitalOcean documents only `typesafe-jev-1.13.0`.
- Netlify's original changelog documents `jev-latest` as 1.13.0 (a separate changelog adds `jev-1.14.0`).
- Several partner docs still pin 1.13 in examples (Pydantic AI `typesafe:jev-1.13.0`, TrueFoundry "recommended" `jev-1.13.0`, Zuplo lists no 1.14). Full matrix: `../purchase-routes.md`.

## Jaggedness page

> Source: https://docs.typesafe.ai/model-jaggedness/jev-1.13.md

The per-version URL still resolves and matches the unversioned `/model-jaggedness.md` page (nine modes plus a separate counting item). Content: `../limitations-and-security.md`.

## Do not copy 1.13 sample strings as current

> Source: https://docs.typesafe.ai/introduction/quickstart.md
> Source: https://docs.typesafe.ai/api/list-models.md

The quickstart and the Choice/Score/Noul pages still show sample responses with `"model": "jev-1.13.0"`, and the list-models example shows only `jev-latest` with `release_date` `2026-09-15`. These are stale samples. Never present them as what `jev-latest` returns today.

## SDKs

SDK release tables live in `jev-1.14.md`. The 1.13-era releases were Python 0.5.7–0.7.2 and JS 0.5.7–0.6.0; both SDKs work against 1.13 at their current versions.

## Sources
- https://docs.typesafe.ai/models.md
- https://docs.typesafe.ai/changelog.md
- https://docs.typesafe.ai/model-jaggedness/jev-1.13.md
- https://docs.typesafe.ai/introduction/quickstart.md
- https://docs.typesafe.ai/api/list-models.md
- https://typesafe.ai/blog/jev-1-14 (vendor blog)
- https://openrouter.ai/blog/insights/what-is-jev/
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://docs.digitalocean.com/products/inference/how-to/use-system-one-api/
- https://www.netlify.com/changelog/typesafe-jev-ai-gateway/

Fetched: 2026-11-13
