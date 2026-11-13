# Direct API and SDKs (TypeSafe-hosted path)

Read this when calling jev through TypeSafe's own endpoint: raw HTTP, `typesafe-sdk` (Python) or `@typesafe-ai/sdk` (JS/TS). Gateways that reuse this shape (Vercel, OpenRouter, LiteLLM, Pydantic AI Gateway and others) are in `purchase-routes.md`; Cloudflare is in `cloudflare-workers-ai.md`. Version history: `versions/jev-1.14.md`.

## Getting access

> Source: https://docs.typesafe.ai/introduction/quickstart.md
> Source: https://typesafe.ai/blog/series-ai (vendor blog)

- Create a key at `https://console.typesafe.ai/keys` and export it as `TYPESAFE_API_KEY`; both SDKs read it automatically.
- Waitlist status is unresolved: the quickstart no longer mentions one, while vendor posts through 2026-10-14 still say "early access". If a new account cannot create keys, that is the likely reason.
- Try questions without code in the Playground: `https://console.typesafe.ai/playground`.

## Raw HTTP

> Source: https://docs.typesafe.ai/api/system-one.md
> Source: https://api.typesafe.ai/openapi.json

```bash
curl --fail-with-body -sS https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" -H "Content-Type: application/json" \
  -d '{"model": "jev-1.14.0", "state": "text",
       "questions": {"q": {"type": "noul", "instructions": "..."}}}'
```

- Endpoints in the spec: `POST /v1/systemone` and `GET /v1/models` only.
- Body: `model`, `state`, `questions` required; `assets` optional. Content types `application/json`, or `multipart/form-data` for images (first part `request`).
- Optional headers: `TypeSafe-Danger-Zone-Images: true`, `TypeSafe-Danger-Zone-Long-Context: true`, `Content-Encoding: gzip|zstd`.
- Response: `model` (the version that actually answered; may differ from the alias you sent), `answers`, `usage` (`input_tokens` billable, `output_tokens` free). The response id header is `x-typesafe-request-id`.
- `GET /v1/models` returns `{models: [{name, description, release_date}]}` and currently lists the aliases. Issue #7 notes `release_date` is a full timestamp though the schema says `YYYY-MM-DD`.
- No server-side configuration exists beyond the account key; everything is per request.

## Python SDK `typesafe-sdk` (0.7.5)

> Source: https://docs.typesafe.ai/sdk/python.md
> Source: https://docs.typesafe.ai/sdk/python/usage/basic.md

`pip install typesafe-sdk` or `uv add typesafe-sdk`; Python ≥ 3.10. Extras: `zstd` (needed below Python 3.14 for compression), `http2`, `pil`.

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

with TypeSafeClient(model="jev-1.14.0") as client:       # reads TYPESAFE_API_KEY
    r = client.system_one(
        state={"ticket": "I was charged twice...", "account_tier": "business"},
        questions={
            "intent": Choice(instructions="Which team?", criteria={"billing": "...", "technical": "..."}),
            "is_urgent": Noul(instructions="Is this time-sensitive?"),
            "frustration": Score(instructions="How frustrated?", criteria=["Calm", "Frustrated", "Very angry"]),
        },
    )
    r.choices["intent"].choice, r.nouls["is_urgent"].noul, r.scores["frustration"].score
```

- `AsyncTypeSafeClient` has the same surface with coroutines (`async with`).
- `system_one(state, questions, *, model, retry, timeout, extra_headers, extra_body, response_model, assets)`. `state` and `questions` can be positional.
- Response: `SystemOneResponse` with `model`, `usage`, `answers`, `request_id`, and filtered views `nouls`, `choices`, `scores`. `ChoiceAnswer` (`choice`, `confidence`, `probabilities`), `ScoreAnswer` (`score`, `confidence`, `legend`, `probabilities` as `dict[int, float]`), `NoulAnswer` (`noul`), `Box` answers since 0.7.5.
- **Typed responses**: `response_model=` a `SystemOneResponse` subclass with fields per question (`billing: NoulAnswer`), or any pydantic `BaseModel` with a nested `answers`.
- Plain dicts work in place of the helper classes; raw question dicts and `extra_body=` let you send fields the installed SDK does not model yet.
- `models.list()` returns model metadata.
- Invalid keys raise `TypeSafeError` at client construction. Since 0.7.1 the key never appears in logged exceptions; the `typesafe_sdk` logger redacts secrets.

### Images and Box in Python (0.7.5)

> Source: https://docs.typesafe.ai/sdk/python/usage/basic.md

Opt in with `TypeSafeClient(headers={"TypeSafe-Danger-Zone-Images": "true"})`. Three ways to reference an `Image` (from bytes, path, base64 string or PIL object):
1. **In content**: `state=["The customer returned this item:", Image(returned)]`; the SDK assigns a unique reference.
2. **In text**: `with client.attach_assets(photo):` then interpolate `{photo}` in an f-string. Forgetting the `with` block breaks the association.
3. **Named**: `assets={"<product>": Image(photo)}` with `<product>` in the text.
Requests with assets are sent as `multipart/form-data`.

### Python env vars, defaults and retries

> Source: https://docs.typesafe.ai/sdk/python/api/constants.md
> Source: https://docs.typesafe.ai/sdk/python/api/retries.md

| Env var | Default |
|---|---|
| `TYPESAFE_API_KEY` | none (required) |
| `TYPESAFE_BASE_URL` | `https://api.typesafe.ai` |
| `TYPESAFE_DEFAULT_MODEL` | `jev-latest` |
| `TYPESAFE_LOG_LEVEL` | unset (applied once at import) |

Timeout 10.0 s per HTTP operation. `RetryPolicy` defaults: `max_retries` 2, `backoff_initial` 0.5 s, `backoff_max` 5.0 s, `backoff_jitter` 0.25, `http_statuses` {408, 429, 500–599}, `respect_retry_after` True, connection errors and timeouts retried, `timeout` **30.0 s total budget per call** (re-raises rather than sleeping past it). Set it on the client or per call: `RetryPolicy(max_retries=3, backoff_max=0.2, timeout=1.0)`.

### Python performance

> Source: https://docs.typesafe.ai/sdk/python/usage/advanced.md

- Reuse one client; construction costs new connections and TLS handshakes. Pooled connections stay alive 30 s (since 0.7.3).
- Bodies ≥ 1 KiB are zstd-compressed by default; install the `zstd` extra on Python < 3.14 and configure or disable via the `compression` constructor argument (disable it for gateways that reject compressed bodies).
- High-rate async: pass an aiohttp-backed client (`AsyncTypeSafeClient(http_client=Httpx2AiohttpClient())` from `httpx-aiohttp`); create a client per thread for threaded code; HTTP/2 via `httpx2.AsyncClient(http2=True)`; keep a connection limit.

## JavaScript / TypeScript SDK `@typesafe-ai/sdk` (0.7.0)

> Source: https://docs.typesafe.ai/sdk/javascript.md
> Source: https://docs.typesafe.ai/sdk/javascript/api/interfaces/TypeSafeClientConfig.md

`npm install @typesafe-ai/sdk`; **Node.js ≥ 22** (0.7.0 breaking change). ESM, CJS and bundled types.

```ts
import { choice, noul, score, TypeSafeClient } from "@typesafe-ai/sdk";
const client = new TypeSafeClient({ defaultModel: "jev-1.14.0" });   // reads TYPESAFE_API_KEY
const res = await client.systemOne({
  state: { ticket: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is this ticket about?", { billing: null, technical: null, other: null }),
    urgent: noul("The message conveys urgency or time-sensitivity"),
    frustration: score("How frustrated?", ["Calm", "Frustrated", "Very angry"]),
  },
});
res.answers.category.choice;   // typed "billing" | "technical" | "other"
```

- Builders shown in the docs: `choice(instructions, criteria)`, `noul(instructions)`, `score(instructions, levels)`, `box(instructions)`. The JS docs show no Noul `criteria` argument and no raw-object question form; put the boundary in the instruction text, or use the Python SDK (`NoulCriteria`) or raw HTTP when you need explicit `criteria`.
- `systemOne<Q>(request, options?)` returns an `APIPromise<SystemOneResult<Q>>`; since 0.7.0 invalid requests (empty `questions`, bad Score criteria) **reject** the promise instead of throwing synchronously. `.withResponse()` adds the HTTP response and request id; `.asResponse()` returns the raw `Response`.
- `usage` keeps snake_case (`input_tokens`, `output_tokens`), and token counts may be `null`.
- Images: `image(bytesOrBlob)` or `Image.fromBase64()`; place them in content, inside `withAssets` tagged templates (`withAssets.join` for lists), or under `assets` with named references. An image in an untagged template literal rejects before sending. Opt in with `defaultHeaders: { "TypeSafe-Danger-Zone-Images": "true" }` or per-call `headers`.
- Box answers: `answers.x.box` (`top`, `bottom`, `left`, `right`) and `confidence` that may be `null`. The JS docs say to use `jev-preview` for Box; pin `jev-1.14.0` instead.

| Config field | Env var | Default |
|---|---|---|
| `apiKey` | `TYPESAFE_API_KEY` | required |
| `baseURL` | `TYPESAFE_BASE_URL` | `https://api.typesafe.ai` |
| `defaultModel` | `TYPESAFE_DEFAULT_MODEL` | `jev-latest` |
| `logLevel` | `TYPESAFE_LOG_LEVEL` | `warn` |
| `timeout` | — | `10000` ms per attempt; no total budget |
| `compression` | — | `"zstd"` on Node 22.15+, else `false`; bodies < 1 KiB never compressed |
| `dangerouslyAllowBrowser` | — | `false`; enabling it exposes the key client-side |
| `defaultHeaders`, `fetch`, `retry` | — | partial `RetryPolicy` inherits defaults |

Config precedence: constructor > env vars > defaults; whitespace-only env values count as absent. JS retry defaults match Python's in milliseconds (`maxRetries: 2`, `backoffInitialMs: 500`, `backoffMaxMs: 5000`, `backoffJitter: 0.25`, `respectRetryAfter: true` up to `maxRetryAfterMs: 60000`).

## Pointing an SDK at another endpoint

> Source: https://docs.typesafe.ai/sdk/python/usage/basic.md

Set `base_url` / `baseURL` (or `TYPESAFE_BASE_URL`) to any server that follows the TypeSafe OpenAPI spec, with that server's key and model id:

| Endpoint | `base_url` | Key | Model |
|---|---|---|---|
| OpenRouter | `https://openrouter.ai/api` | `OPENROUTER_API_KEY` | `~typesafe/jev-latest` or `typesafe/jev-1.14` |
| Vercel AI Gateway | `https://ai-gateway.vercel.sh/typesafe` | `AI_GATEWAY_API_KEY` | `typesafe-ai/jev` |
| Pydantic AI Gateway | `https://gateway-us.pydantic.dev/proxy/typesafe` | `PYDANTIC_AI_GATEWAY_API_KEY` | `jev-latest` |
| Local System One server (Kev, Ollaya, Ollama, ...) | e.g. `http://localhost:11435` | any non-empty | the server's model name |

If the endpoint rejects compressed bodies, disable SDK compression. Local servers: `decision-model-alternatives.md`.

## Sources
- https://docs.typesafe.ai/introduction/quickstart.md
- https://typesafe.ai/blog/series-ai (vendor blog)
- https://docs.typesafe.ai/api/system-one.md
- https://docs.typesafe.ai/api/list-models.md
- https://api.typesafe.ai/openapi.json
- https://github.com/typesafe-ai/skills/issues (issue #7)
- https://docs.typesafe.ai/sdk/python.md
- https://docs.typesafe.ai/sdk/python/usage/basic.md
- https://docs.typesafe.ai/sdk/python/usage/advanced.md
- https://docs.typesafe.ai/sdk/python/api/constants.md
- https://docs.typesafe.ai/sdk/python/api/retries.md
- https://docs.typesafe.ai/sdk/python/changelog.md
- https://docs.typesafe.ai/sdk/javascript.md
- https://docs.typesafe.ai/sdk/javascript/changelog.md
- https://docs.typesafe.ai/sdk/javascript/api/interfaces/TypeSafeClientConfig.md
- https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy.md
- https://docs.typesafe.ai/sdk/javascript/api/classes/APIPromise.md (2026-09-23)
- https://github.com/ollaya-dev/ollaya (community)

Fetched: 2026-11-13
