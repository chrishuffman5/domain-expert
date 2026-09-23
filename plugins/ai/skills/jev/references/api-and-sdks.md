# Direct API and SDKs (TypeSafe-hosted path)

Read this when you are calling jev through TypeSafe's own endpoint: raw HTTP, `typesafe-sdk` (Python) or `@typesafe-ai/sdk` (JS/TS). This file also covers gateway routes that reuse the TypeSafe request shape (Vercel AI Gateway, OpenRouter, LiteLLM). For Cloudflare Workers AI, see `cloudflare-workers-ai.md`.

## Getting access

> Source: https://docs.typesafe.ai/introduction/quickstart.md
> Source: https://typesafe.ai/blog/introducing-system-one-models-and-jev

- Access is early access behind a waitlist, open since the 2026-09-15 launch. A new user may be blocked until admitted.
- Create a key at `https://console.typesafe.ai/keys`, then export it as `TYPESAFE_API_KEY`. Both SDKs read this variable automatically.

## Raw HTTP

> Source: https://docs.typesafe.ai/api.md

```bash
curl -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"state": "text", "model": "jev-latest", "questions": {"q": {"type": "noul", "instructions": "..."}}}'
```

- Body: `state`, `model` and `questions`, all required.
- Response: `model` (the model that actually answered), `answers` and `usage` (`input_tokens`, `output_tokens`).
- Error codes: see `pricing-limits-errors.md`.

No persistent server-side configuration exists beyond the account key. Every setting is per request.

## Python SDK: `typesafe-sdk`

> Source: https://docs.typesafe.ai/sdk/python.md
> Source: https://docs.typesafe.ai/sdk/python/api/clients/sync.md
> Source: https://docs.typesafe.ai/sdk/python/api/clients/async.md

Install with `pip install typesafe-sdk` or `uv add typesafe-sdk`. Requires Python >= 3.10.

```python
from typesafe_sdk import Choice, Noul, Score, NoulCriteria, TypeSafeClient

with TypeSafeClient() as client:                      # reads TYPESAFE_API_KEY
    r = client.system_one(
        state={"ticket": "I was charged twice...", "account_tier": "business"},
        questions={
            "intent": Choice(instructions="Which team?", criteria={"billing": "...", "technical": "...", "other": "..."}),
            "is_urgent": Noul(instructions="Is this time-sensitive?", criteria=NoulCriteria(true="...", false="...")),
            "frustration": Score(instructions="How frustrated?", criteria=["Calm", "Frustrated", "Very angry"]),
        },
    )
    r.choices["intent"].choice, r.nouls["is_urgent"].noul, r.scores["frustration"].score
```

- Async: `AsyncTypeSafeClient` has the same surface with coroutines. Use `async with`, and close it with `aclose()`.
- Constructor: `TypeSafeClient(*, api_key, model, retry, timeout, headers, transport, http_client, base_url)`. `transport` and `http_client` are mutually exclusive.
- `system_one(state, questions, *, model, retry, timeout, extra_headers, extra_body, response_model)`.
- `models.list()` returns `ListModelsResponse.models`. Each entry is a `ModelMetadata` with `name`, `description` and `release_date` (YYYY-MM-DD). The HTTP path behind this call is not documented.
- Response objects:
  - `SystemOneResponse` has `model`, `usage` and `answers`, plus filtered views `nouls`, `choices` and `scores`.
  - `ChoiceAnswer` has `choice`, `confidence` and `probabilities`.
  - `ScoreAnswer` has `score`, `confidence`, `legend` and `probabilities` (dict[int, float]).
  - `NoulAnswer` has `noul`.
- Plain dicts (`NoulModel`/`ChoiceModel`/`ScoreModel` TypedDicts) work in place of the helper classes.

> Source: https://docs.typesafe.ai/sdk/python/usage.md

- **Typed responses** (SDK 0.7.0+): pass `response_model=` a Pydantic model (optionally a `SystemOneResponse` subclass) to get checked field access.
- **Forward compatibility**: `extra_body=` and raw question dicts let you send API fields the installed SDK does not model yet.
- **Logging**: the `typesafe_sdk` logger redacts secrets automatically.
- **Fail-fast**: invalid keys are detected when the client is constructed. Since 0.7.1 the key is validated early and kept out of logged exceptions.

### Python env vars and defaults

> Source: https://docs.typesafe.ai/sdk/python/api/constants.md

| Env var | Default |
|---|---|
| `TYPESAFE_API_KEY` | none (required) |
| `TYPESAFE_BASE_URL` | `https://api.typesafe.ai` |
| `TYPESAFE_DEFAULT_MODEL` | `jev-latest` |
| `TYPESAFE_LOG_LEVEL` | the Python default is not stated in the docs |

HTTP timeout: 10.0 s per operation.

### Python `RetryPolicy`

> Source: https://docs.typesafe.ai/sdk/python/api/retries.md

| Field | Default | Meaning |
|---|---|---|
| `max_retries` | 2 | Retries after the first attempt. `0` disables retries. |
| `backoff_initial` / `backoff_max` | 0.5 s / 5.0 s | The delay doubles on each attempt up to the cap. |
| `backoff_jitter` | 0.25 | Fraction subtracted at random from each delay. |
| `http_statuses` | {408, 429, 500–599} | Status codes that trigger a retry. 529 falls in this range. |
| `respect_retry_after` | True | Honours `Retry-After` / `retry-after-ms`. |
| `api_connection_error` / `api_timeout_error` | True / True | |
| `exceptions` / `predicate` | ∅ / None | Custom retry eligibility. |
| `timeout` | 30.0 s | **Total** retry budget per call. It is separate from the per-attempt timeout. |

If the next backoff would exceed the remaining budget, the SDK re-raises instead of sleeping. Set the policy on the client or per call. Example: `RetryPolicy(max_retries=3, timeout=10.0, http_statuses={429, 500, 502, 503, 504})`.

## JavaScript / TypeScript SDK: `@typesafe-ai/sdk`

> Source: https://docs.typesafe.ai/sdk/javascript.md
> Source: https://docs.typesafe.ai/sdk/javascript/api/classes/TypeSafeClient.md

Install with `npm install @typesafe-ai/sdk`. Requires Node.js 20+. The package ships ESM and CJS builds with bundled `.d.ts` types.

```ts
import { choice, TypeSafeClient } from "@typesafe-ai/sdk";
const client = new TypeSafeClient();                   // reads TYPESAFE_API_KEY
const res = await client.systemOne({
  state: { document: "I was charged twice. Please fix this ASAP." },
  questions: { category: choice("What is this ticket about?", { billing: null, technical: null, other: null }) },
});
res.answers.category.choice;                           // answer types inferred from questions
```

- `systemOne<Q>(request, options?)` returns an `APIPromise<SystemOneResult<Q>>`.
  - It throws client-side on an empty `questions` map or invalid Score `criteria`.
  - It throws on a non-2xx response, a connection failure, a timeout or an abort.
- `choice(instructions, criteria)` is the documented builder. `noul(...)` and `score(...)` are listed in the API index, but their pages were not fetched. Build raw `{type: ...}` objects if the helpers do not match.
- `usage` keeps snake_case (`input_tokens`, `output_tokens`) even in TS.
- `models.list()` returns `ModelCard[]`. The `ModelCard` fields are not documented in the corpus.
- `APIPromise` methods: `.withResponse()` returns the result plus the HTTP response and request id. `.asResponse()` returns the raw Response. `.map(fn)`. Non-2xx responses still reject with an `APIError`.

Config precedence: constructor options > env vars > SDK defaults. Whitespace-only env values count as absent.

> Source: https://docs.typesafe.ai/sdk/javascript/api/interfaces/TypeSafeClientConfig.md
> Source: https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy.md

| Config field | Env var | Default |
|---|---|---|
| `apiKey` | `TYPESAFE_API_KEY` | required |
| `baseURL` | `TYPESAFE_BASE_URL` | `https://api.typesafe.ai` |
| `defaultModel` | `TYPESAFE_DEFAULT_MODEL` | `jev-latest` |
| `logLevel` | `TYPESAFE_LOG_LEVEL` | `warn` |
| `timeout` | — | `10000` ms **per attempt**. JS has no total retry budget. |
| `dangerouslyAllowBrowser` | — | `false`. Enabling it exposes the key client-side. |
| `retry` | — | A partial `RetryPolicy`; unset fields inherit the defaults. |

JS retry defaults match Python's in milliseconds:
- `maxRetries: 2`
- `backoffInitialMs: 500`, `backoffMaxMs: 5000`, `backoffJitter: 0.25`
- `httpStatuses: {408, 429, 500–599}`
- `respectRetryAfter: true`, with `maxRetryAfterMs: 60000` as the cap. A longer server wait falls back to computed backoff.

## Gateway routes that reuse the TypeSafe shape

> Source: https://docs.typesafe.ai/sdk/python/usage.md
> Source: https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
> Source: https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
> Source: https://docs.litellm.ai/docs/pass_through/typesafe
> Source: https://openrouter.ai/blog/insights/what-is-jev/

| Route | How | Credential | Notes |
|---|---|---|---|
| Vercel AI Gateway (TypeSafe-compatible) | `baseURL`/`base_url` = `https://ai-gateway.vercel.sh/typesafe`. Endpoints: `POST /typesafe/v1/systemone`, `GET /typesafe/v1/models` | AI Gateway key (`AI_GATEWAY_API_KEY`) or a Vercel OIDC token as Bearer. BYOK is optional. | Same request, response and error shapes. Adds `provider_metadata.gateway` cost metadata. Model id in examples: `typesafe-ai/jev`. Vercel recommends its generic "evaluation API" for new code. |
| Vercel AI SDK provider | `pnpm add @ai-sdk/typesafe-ai`; `experimental_evaluate({ model: typeSafeAi.evaluationModel('jev-latest'), state, questions })` | Env var is **`TYPESAFE_AI_API_KEY`**, not `TYPESAFE_API_KEY` | The `experimental_` prefix marks the surface unstable. No streaming, language, embedding or image models. |
| OpenRouter via the Python SDK | Override `base_url`; model `~typesafe/jev-latest` | OpenRouter key | Documented by TypeSafe's Python usage page. |
| OpenRouter decisions endpoint | `POST https://openrouter.ai/api/alpha/decisions`, model `typesafe/jev-1.13` | OpenRouter key | `/alpha/` path, so the surface is unstable. The model id differs from the SDK route above; verify it before use. |
| LiteLLM pass-through | Call `LITELLM_PROXY_BASE_URL/typesafe/...`; model `typesafe/<model>` | The proxy needs `TYPESAFE_API_KEY`. `TYPESAFE_API_BASE` is optional. | Any path under `/typesafe/` is forwarded. The docs say "Streaming not supported". |

Vercel's error example: `{"message": "questions.refund.type: expected one of 'noul', 'choice', 'score'", "error_type": "invalid_request"}`.

## Sources
- https://docs.typesafe.ai/introduction/quickstart.md
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://docs.typesafe.ai/api.md
- https://docs.typesafe.ai/sdk/python.md
- https://docs.typesafe.ai/sdk/python/usage.md
- https://docs.typesafe.ai/sdk/python/api/clients/sync.md
- https://docs.typesafe.ai/sdk/python/api/clients/async.md
- https://docs.typesafe.ai/sdk/python/api/constants.md
- https://docs.typesafe.ai/sdk/python/api/retries.md
- https://docs.typesafe.ai/sdk/python/api/types/responses.md
- https://docs.typesafe.ai/sdk/python/api/types/questions.md
- https://docs.typesafe.ai/sdk/javascript.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/TypeSafeClient.md
- https://docs.typesafe.ai/sdk/javascript/api/interfaces/TypeSafeClientConfig.md
- https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/APIPromise.md
- https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
- https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
- https://docs.litellm.ai/docs/pass_through/typesafe
- https://openrouter.ai/blog/insights/what-is-jev/

Fetched: 2026-09-23
