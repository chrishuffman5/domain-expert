# Pricing, limits and errors

Read this when you are estimating cost, sizing requests, handling failures, or writing retry and credential-check logic.

## Pricing (direct TypeSafe API)

> Source: https://docs.typesafe.ai/models.md
> Source: https://typesafe.ai
> Source: https://typesafe.ai/blog/introducing-system-one-models-and-jev

- **$0.042 per million input tokens**, which is $42 per billion. **Output tokens are free.**
- No free tier or trial credit is documented. Access is waitlisted early access. The no-free-tier point is also reported by the Requesty gateway page: https://www.requesty.ai/model/typesafe/jev.
- The vendor says the pricing may be subsidised: "We can't prove it isn't subsidized; we'll need the long-term to prove the sustainability of our pricing (which we expect to go down, not up)." Treat current rates as early-access, not a contract.
- Cost estimate: sum `usage.input_tokens` × $0.042/1M. State and every question's text count as input, so trim state to cut cost.
- Real-world cost varies by workload (press tier). One early adopter found jev "10 to 20 times more expensive" than Gemini for his workload (TechCrunch). Benchmark your own traffic before you assume savings.

Gateway pricing:
- **Cloudflare**: unconfirmed. See `cloudflare-workers-ai.md`.
- **OpenRouter**: states the same rate as direct.
- **Requesty**: "pay as you go adds 5% on top, or 0% if you bring your own provider keys" (vendor gateway).
- **Vercel AI Gateway**: bills through Vercel. BYOK bills TypeSafe directly.

## Limits

> Source: https://docs.typesafe.ai/models.md
> Source: https://docs.typesafe.ai/primitives/choice.md
> Source: https://docs.typesafe.ai/primitives/score.md

| Limit | Value | Note |
|---|---|---|
| Request context | **64k tokens** per request | The outer limit. |
| State + longest single question | **32k tokens** | A nested inner limit. Cloudflare's "32,000" is this number. |
| Choice options | 255 max | Prose limit only. The JSON Schema does not enforce it. |
| Score levels | 2–10 | The schema enforces min 2. Max 10 is prose only. |
| Rate limit | 250,000 tokens/s and 1,200 requests/min | "Adjusting dynamically … can change without notice". Custom and enterprise plans get more. |
| Input modality | Text only | String, JSON object or array of text. |
| Customization | None | No fine-tuning or LoRA. Customize with `state`, `instructions` and `criteria`. |

Never hardcode the rate-limit numbers as guaranteed ceilings. The contract is 429 handling.

Streaming and batch: no streaming or batch surface is documented. The LiteLLM pass-through and the Vercel AI SDK provider both state streaming is not supported. For Cloudflare it is simply unstated.

## Unified error table

> Source: https://docs.typesafe.ai/api.md
> Source: https://github.com/typesafe-ai/skills/issues/8
> Source: https://docs.typesafe.ai/sdk/python/api/exceptions.md
> Source: https://docs.typesafe.ai/sdk/javascript/api/classes/APIError.md

| HTTP | Documented meaning | Python exception | JS class | Action |
|---|---|---|---|---|
| 400 | Invalid request | `TypeSafeBadRequestError` | `BadRequestError` | Fix the payload. Do not retry. |
| **401** | **Invalid** API key (documented) | `TypeSafeAuthenticationError` | `AuthenticationError` | Fix or rotate the key. |
| **403** | **Missing** API key. This is the **observed behaviour**; the docs say 401. | `TypeSafePermissionDeniedError` | `PermissionDeniedError` | Check that the key is set. See the defect below. |
| 404 | Resource not found | `TypeSafeNotFoundError` | `NotFoundError` | Check the base URL or path. |
| 422 | Request validation failure (bad question shape, criteria and so on) | `TypeSafeUnprocessableEntityError` | `UnprocessableEntityError` | Fix the payload. Do not retry. |
| 429 | Rate limit exceeded | `TypeSafeRateLimitError` (`retry_after_ms`) | `RateLimitError` (`retryAfterMs`) | Back off. The SDKs retry automatically. |
| 529 | Service overloaded | *Inferred:* `TypeSafeInternalServerError` (the 5xx class; no source names the class for 529) | *Inferred:* `InternalServerError` | Exponential backoff. It is in the default retry set. |
| 5xx | Server failure | `TypeSafeInternalServerError` | `InternalServerError` | Retried by default. Circuit-break if it persists. |
| — | No HTTP response | `TypeSafeAPIConnectionError` | `APIConnectionError` | Retried by default. |
| — | Timeout | `TypeSafeAPITimeoutError` (`.timeout`) | `APITimeoutError` (`timeoutMs`) | Retried by default. Check per-attempt vs total budgets. |
| — | Caller aborted | — | `APIUserAbortError` | |
| 2xx | Body missing or structurally invalid | `TypeSafeAPIResponseValidationError` (`field_path`) | — | Upgrade the SDK and report it. |

Vendor guidance for 429 and 529: "Retry the request with exponential backoff instead of retrying immediately."

### The 401-vs-403 defect (GitHub typesafe-ai/skills#8, open as of 2026-09-21)

The docs promise 401 for a missing or invalid key. The server actually returns:
- **Missing** key → **403**, with body `"error_type":"authentication_error"`.
- **Invalid** key → **401**, with the same `error_type`.

Both SDKs map exceptions by status code, so a missing key surfaces as `PermissionDeniedError` and not `AuthenticationError`.

**Always catch both** 401 and 403 classes when checking whether the credential is the problem, or branch on `body.error_type == "authentication_error"`. Catching `AuthenticationError` alone silently misses the missing-key case. Re-check the issue before you remove the workaround.

### Debugging fields

- Python `TypeSafeAPIError`: `status`, `body`, `headers`, `endpoint`, `request_id`.
- JS `APIError`: `status`, `body`, `headers`, `requestId` (from the `x-typesafe-request-id` header).
- Quote the request id when you contact support.

### Retry defaults (both SDKs)

- 2 retries.
- Backoff starts at 0.5 s and doubles up to a 5 s cap, with 0.25 jitter.
- Retried statuses: {408, 429, 500–599}. `Retry-After` is honoured.
- Python adds a **30 s total** budget on top of the 10 s per-attempt timeout. JS has a 10 s per-attempt timeout and no total budget.
- Full tables are in `api-and-sdks.md`.

## Cloudflare-path errors

> Source: https://developers.cloudflare.com/workers-ai/get-started/rest-api/

On Cloudflare you authenticate with a Cloudflare token (Workers AI Read + Edit), not a TypeSafe key, so the TypeSafe 401/403 table does not apply to credentials there.
- Community report, unverified: an AI-Gateway-only token gets `401` with code `10000` on `/ai/*`.
- Community report, unverified: an empty credit balance gives "Insufficient AI Gateway credits".

## Sources
- https://docs.typesafe.ai/models.md
- https://typesafe.ai
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://www.requesty.ai/model/typesafe/jev (vendor gateway)
- https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/ (press)
- https://docs.typesafe.ai/primitives/choice.md
- https://docs.typesafe.ai/primitives/score.md
- https://docs.typesafe.ai/api.md
- https://github.com/typesafe-ai/skills/issues/8
- https://docs.typesafe.ai/sdk/python/api/exceptions.md
- https://docs.typesafe.ai/sdk/python/api/retries.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/APIError.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/RateLimitError.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/APIPromise.md
- https://docs.litellm.ai/docs/pass_through/typesafe
- https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
- https://developers.cloudflare.com/workers-ai/get-started/rest-api/

Fetched: 2026-09-23
