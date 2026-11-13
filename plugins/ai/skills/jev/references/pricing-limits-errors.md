# Pricing, limits and errors

Read this when you are estimating cost, sizing requests, handling failures, or writing retry and credential-check logic. Gateway prices and markups: `purchase-routes.md`.

## Pricing (direct TypeSafe API)

> Source: https://docs.typesafe.ai/models.md
> Source: https://typesafe.ai
> Source: https://typesafe.ai/blog/introducing-system-one-models-and-jev (vendor blog)

- **$0.042 per million input tokens** ($42 per billion) for both `jev-1.14.0` and `jev-1.13.0`. **Output tokens are free** (`usage.output_tokens` is reported but not billed).
- Long context costs the same per token. Image tokens bill as input at the normal price and count toward context; image-token estimation guidance is "forthcoming".
- No free tier is documented by TypeSafe (VentureBeat reported $5 free credit when the waitlist dropped; unconfirmed on vendor pages).
- The vendor says pricing may be subsidised and expects it to "go down, not up". Treat current rates as early-access, not a contract.
- Cost estimate: `usage.input_tokens × 0.042 / 1e6`. State and every question's text count as input, so filtered state and short criteria cut cost directly. In the content-audit demo, 45 questions were about 40% of the $0.10 cost of scoring 279 pages.
- **Batch questions, not requests.** The parallel-questions cookbook measured one 13-question request as 12.2× cheaper and 11.8× faster than 13 single-question requests over the same ~54,000-character document, with no change in answers, because the state is billed once per request.

## Limits

> Source: https://docs.typesafe.ai/models.md
> Source: https://docs.typesafe.ai/api/errors.md
> Source: https://api.typesafe.ai/openapi.json
> Source: https://docs.typesafe.ai/images.md

| Limit | Value | Note |
|---|---|---|
| Context per request | **64k tokens** | state + all questions |
| Context per question | **32k tokens** | state + the longest single question; the limit long conversations hit first |
| Long context (opt-in) | **262k** for both | header `TypeSafe-Danger-Zone-Long-Context: true`; 1.13 and 1.14; "slower and less accurate" |
| Over the context limit | 400 with `max_tokens_exceeded` | |
| Request body | 32 MiB (headers excluded), compressed and decompressed | 413 above |
| Body format | UTF-8 JSON without BOM, or `multipart/form-data` for images | |
| JSON nesting | ≤ 64 levels in each of `state`, `instructions`, `criteria` | |
| Numbers | finite only (NaN, Infinity, `1e400` rejected) | send ids and big quantities as strings |
| Compression | `Content-Encoding: gzip`/`x-gzip` or `zstd`, one layer, zstd window ≤ 8 MiB | 415 otherwise |
| Choice options | 1–255 (spec); "works reliably up to roughly 240" (cookbook) | |
| Score levels | 2–10 (prose) vs 1–10 (OpenAPI 0.2.0 and API reference) | conflict; the API enforces ≤ 10 (issue #6) |
| Questions per request | **no documented cap** | only context length limits it |
| Images | PNG/JPEG stills, 16 MiB per file, each side 280–1,568 px, 78,400–2,458,624 total pixels | never resized; one bad image fails the request |
| Asset references | ≤ 1,024 bytes each, 65,536 bytes total; every asset must be referenced | 400 otherwise |
| Rate limits | **per organisation, in tokens/s and requests/s, shown in the developer console** | CHANGED: published numbers removed |

- **Never hardcode rate-limit numbers.** The old "250,000 tokens/s and 1,200 requests/min" figures are gone from the docs. Read your limits in the console; the contract is 429 handling. One official cookbook capped itself at 4 concurrent workers because "more workers hits the public rate limit" (https://docs.typesafe.ai/cookbooks/verify_llm_outputs.md).
- No streaming and no batch endpoint exist: the OpenAPI spec has only `GET /v1/models` and `POST /v1/systemone`.
- Gateway catalogs publish one of the two default numbers: Cloudflare and Vercel show 32,000 (the per-question limit), Requesty 64K (the request limit). OpenRouter shows 262,144 because it auto-enables long context.

## Unified error table

> Source: https://docs.typesafe.ai/api/errors.md
> Source: https://docs.typesafe.ai/api/system-one.md
> Source: https://docs.typesafe.ai/sdk/python/api/exceptions.md
> Source: https://docs.typesafe.ai/sdk/javascript/api/classes/APIError.md (fetched 2026-09-23)

| HTTP | Documented meaning | Python exception | JS class | Action |
|---|---|---|---|---|
| 400 | Rule broken, malformed compressed body, images not enabled, unreferenced asset, bad multipart, or `max_tokens_exceeded` | `TypeSafeBadRequestError` | `BadRequestError` | Fix the payload; shrink state or opt into long context. Never retry. |
| **401** | API key missing or invalid (documented) | `TypeSafeAuthenticationError` | `AuthenticationError` | Fix or rotate the key. |
| **403** | **Missing** key, observed (issue #8, open); not in the docs | `TypeSafePermissionDeniedError` | `PermissionDeniedError` | Treat as a credential error. |
| 404 | Not found | `TypeSafeNotFoundError` | `NotFoundError` | Check base URL and path. |
| 413 | Body over 32 MiB | no dedicated class documented | — | Shrink the body; prefer multipart over base64 for images (base64 adds ~33%). |
| 415 | Unsupported or multiple `Content-Encoding` | no dedicated class documented | — | Send one gzip or zstd layer, or disable SDK compression for a non-official endpoint. |
| 422 | Validation failed; body names the field (`detail[]` with `loc`, `msg`, `type`) | `TypeSafeUnprocessableEntityError` | `UnprocessableEntityError` | Fix the payload. Never retry. |
| 429 | Rate limited | `TypeSafeRateLimitError` (`retry_after_ms`) | `RateLimitError` (`retryAfterMs`) | Back off; SDKs retry. |
| 529 | Overloaded ("retry after short delay") | *inferred* `TypeSafeInternalServerError` | *inferred* `InternalServerError` | Exponential backoff; in the default retry set. |
| 5xx | Server failure | `TypeSafeInternalServerError` | `InternalServerError` | Retried by default; circuit-break if persistent. |
| — | No response / timeout | `TypeSafeAPIConnectionError` / `TypeSafeAPITimeoutError` | `APIConnectionError` / `APITimeoutError` | Retried by default. |
| 2xx | Body structurally invalid | `TypeSafeAPIResponseValidationError` (`field_path`) | — | Upgrade the SDK and report it. |

- The OpenAPI spec lists only 400 (`HTTPBadRequestError`, `detail` string or object) and 422; every other status lives only in the errors page.
- Issue #1 (open): request-body validation can return 400 where docs say 422. Handle both as "fix the payload".
- Invalid API keys raise `TypeSafeError` when the Python client is constructed, before any request (keys are stripped of surrounding whitespace; internal whitespace, control and non-ASCII characters are rejected).

### The 401-vs-403 defect (typesafe-ai/skills#8, still open 2026-11-13)

> Source: https://github.com/typesafe-ai/skills/issues/8
> Source: https://developer.konghq.com/ai-gateway/ai-providers/typesafe/

- Missing or empty key → **403**; invalid key → **401**. Both carry `error_type: "authentication_error"`. The docs still promise 401 for both, and no maintainer has responded.
- Both SDKs map exceptions by status only, so an unset `TYPESAFE_API_KEY` surfaces as `PermissionDeniedError`, not `AuthenticationError`.
- **Always catch both** classes when checking credentials, or branch on `body.error_type == "authentication_error"`. Kong's docs independently note a 403 (docs say 401) for missing or invalid keys.
- Re-check the issue before removing the workaround.

### Debugging fields

- Python `TypeSafeAPIError`: `status`, `body`, `headers`, `endpoint`, `request_id`. Typed responses also expose `request_id`.
- JS `APIError`: `status`, `body`, `headers`, `requestId` (from `x-typesafe-request-id`).
- Quote the request id to support. Error bodies can echo submitted state; do not log them blindly (LangChain JS docs).

### Retry defaults (both SDKs)

> Source: https://docs.typesafe.ai/sdk/python/api/retries.md
> Source: https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy.md

- 2 retries (3 attempts); backoff 0.5 s doubling to a 5 s cap, 25% jitter; statuses {408, 429, 500–599}, so 529 is included; `Retry-After` / `retry-after-ms` honoured (JS caps the wait at 60 s).
- Python: 10 s per HTTP operation **plus a 30 s total budget per call**; if the next backoff would exceed the remaining budget it re-raises. JS: 10 s per attempt, **no total budget**.

## Gateway error shapes

> Source: https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
> Source: https://docs.litellm.ai/docs/pass_through/typesafe
> Source: https://docs.requesty.ai/features/decisions.md

- Vercel `/typesafe/v1/systemone`: validation and auth errors use TypeSafe's shape (`message`, `error_type`); insufficient credits, unknown model or provider failure use the gateway's `error` object. `GET /typesafe/v1/models` always uses the gateway shape.
- LiteLLM returns 403 (`team_model_access_denied`) for a model outside the key's access list.
- Requesty returns 403 when the decisions endpoint and chat APIs are not both approved.
- On Cloudflare you authenticate with a Cloudflare token, so TypeSafe's 401/403 semantics do not apply to credentials there.

## Sources
- https://docs.typesafe.ai/models.md
- https://typesafe.ai
- https://typesafe.ai/blog/introducing-system-one-models-and-jev (vendor blog)
- https://docs.typesafe.ai/images.md
- https://docs.typesafe.ai/demos/content-audit.md
- https://docs.typesafe.ai/cookbooks/parallel_questions.md
- https://docs.typesafe.ai/cookbooks/classification_using_confidence.md
- https://docs.typesafe.ai/cookbooks/verify_llm_outputs.md
- https://docs.typesafe.ai/api/errors.md
- https://docs.typesafe.ai/api/system-one.md
- https://api.typesafe.ai/openapi.json
- https://github.com/typesafe-ai/skills/issues/8
- https://github.com/typesafe-ai/skills/issues (issues #1, #6)
- https://docs.typesafe.ai/sdk/python/api/exceptions.md
- https://docs.typesafe.ai/sdk/python/api/retries.md
- https://docs.typesafe.ai/sdk/python/usage/basic.md
- https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/APIError.md (2026-09-23)
- https://docs.langchain.com/oss/javascript/integrations/providers/typesafe.md
- https://developer.konghq.com/ai-gateway/ai-providers/typesafe/
- https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
- https://docs.litellm.ai/docs/pass_through/typesafe
- https://docs.requesty.ai/features/decisions.md
- https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)

Fetched: 2026-11-13
