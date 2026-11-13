# jev on Cloudflare Workers AI (`typesafe/jev`, `typesafe/jev-1.14.0`)

Read this when you are calling jev from a Worker, through Cloudflare's REST API, or through Cloudflare AI Gateway. It covers jev-specific details only; general Workers AI usage is out of scope. Other purchase routes: `purchase-routes.md`.

## CHANGED since 2026-09-23

> Source: https://developers.cloudflare.com/ai/models/?provider=typesafe

- Cloudflare now lists **two** TypeSafe cards: `typesafe/jev` (version 1.13) and `typesafe/jev-1.14.0` (version 1.14, "successor to Jev 1.13", adds Box).
- `typesafe/jev` has **not** rolled forward to 1.14; it stays 1.13. Use the explicit 1.14 id when you need 1.14 or Box.
- Cards now show a price ($0.042 per 1M input) and "Zero data retention: Yes".
- Image input is listed as beta on both cards: "not recommended for production".
- The path `/workers-ai/models/jev/` returns 404; the live cards are under `/ai/models/typesafe/`.

## What the model cards confirm

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/
> Source: https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/

| | `typesafe/jev` | `typesafe/jev-1.14.0` |
|---|---|---|
| Reports model | `jev-1.13.0` | `jev-1.14.0` |
| Price per 1M tokens | input $0.042, cached input $0.00, output $0.00 | same |
| Context window | 32,000 tokens | 32,000 tokens |
| Box | no | beta |
| Images | beta | beta |
| Provider | third party (TypeSafe) | third party |
| Zero data retention | Yes | Yes |

- Access paths on the card: Workers AI binding (`env.AI.run`), AI Gateway REST API, or Unified API.
- "32,000 tokens" is TypeSafe's **inner** limit (state + the longest single question), not a smaller model. TypeSafe's defaults are 64k per request and 32k per question. **No card says whether Cloudflare forwards the `TypeSafe-Danger-Zone-Long-Context` header**, so assume 262k is unavailable here.
- Cloudflare still calls jev a "structured evaluation model" and publishes JSON Schemas at `.../schema-input.json` and `.../schema-output.json`. The input schema has **no `model` field** and sets `additionalProperties: false`.
- **Not stated anywhere on the cards**: billing mechanism, rate limits, release dates, status label.

## Worker binding

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/

```jsonc
// wrangler.jsonc
{ "ai": { "binding": "AI" } }
```
```ts
const response = await env.AI.run('typesafe/jev', {
  state: 'Help! My payouts have been failing for 3 days.',
  questions: {
    is_urgent: { type: 'noul', instructions: 'Does this convey urgency?',
                 criteria: { true: 'Explicitly time-sensitive', false: 'No urgency expressed' } },
    department: { type: 'choice', instructions: 'Which team should handle this?',
                  criteria: { billing: 'Payments, invoicing, refunds', technical: 'Bugs, outages, integrations', sales: 'Pricing, upgrades, new accounts' } },
    frustration: { type: 'score', instructions: 'How frustrated is the customer?',
                   criteria: ['Calm', 'Frustrated', 'Very angry'] },
  },
});
```
- Swap `'typesafe/jev'` for `'typesafe/jev-1.14.0'` to run 1.14.
- Output shape is `{model, answers, usage}`; a Noul answer is `{"type":"noul","noul":0.95}`.
- This path needs no TypeSafe API key.
- Log `response.model` on every call so you know which version answered.

## REST: the model id goes in the BODY

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/
> Source: https://developers.cloudflare.com/workers-ai/get-started/rest-api/ (fetched 2026-09-23; not re-fetched)

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"model": "typesafe/jev-1.14.0",
           "input": {"state": "...", "questions": {"q": {"type": "noul", "instructions": "..."}}}}'
```

- Send `model` and `input` as **siblings** and POST to the bare `.../ai/run`.
- Never append the model to the path. The path form `.../ai/run/@cf/...` is for first-party `@cf/` models (including Cloudflare's own Clef).
- Never put `model` inside `input`; the schema rejects extra properties.
- The token needs **Workers AI - Read** and **Workers AI - Edit**. These scopes are account-wide; you cannot scope a token to jev alone.
- The generic REST page documents a `{result, success, errors, messages}` envelope, while the jev card shows the payload unwrapped. Expect it under `result` on REST and verify against a live response.

## AI Gateway

> Source: https://developers.cloudflare.com/ai-gateway/integrations/worker-binding-methods/ (fetched 2026-09-23; not re-fetched)
> Source: https://developers.cloudflare.com/ai-gateway/usage/rest-api/ (fetched 2026-09-23; not re-fetched)

```js
await env.AI.run("typesafe/jev-1.14.0", { state, questions }, { gateway: { id: "default" } });
```
- `gateway.id` is required; `"default"` auto-creates a gateway on the first authenticated request.
- For REST through AI Gateway, use the universal `/ai/run` endpoint with the model in the body. No source says the OpenAI-compatible `/ai/v1/chat/completions` or Anthropic-compatible `/ai/v1/messages` routes accept jev.
- Retry and fallback behaviour for jev through AI Gateway is not documented.
- Not to be confused with **Vercel** AI Gateway (a different company); see `purchase-routes.md`.

## Billing and rate limits: NOT STATED

> Source: https://developers.cloudflare.com/workers-ai/platform/pricing/
> Source: https://developers.cloudflare.com/ai-gateway/features/unified-billing/
> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/
> Source: https://developers.cloudflare.com/workers-ai/platform/limits/

The only official jev figure is the card price ($0.042 per 1M input, $0 output). **No Cloudflare page ties jev to a billing path.**
- The Workers AI pricing page (Neurons: 10,000 free per day, then $0.011 per 1,000 on Workers Paid) does not mention jev. It says some third-party providers' models need Workers Paid or prepaid AI Gateway credits, naming moonshotai, zai-org, deepseek-ai and thinkingmachines, not typesafe.
- Unified Billing (prepaid credits, 5% fee on purchases, inference passed through with no markup) names OpenAI, Anthropic, Google AI Studio, Vertex, xAI and Groq, not TypeSafe. The 2026-08-07 changelog extended credits to Workers AI and names kimi and glm models, not jev.
- The limits page is organised by task type (Text Generation 300 rpm, paid-gated models 20 rpm standard / 50 rpm with credits) and does not name jev or its task type.

**Never state a Cloudflare billing path or rate limit for jev.** Say "not stated" and send the user to the dashboard (`https://dash.cloudflare.com/?to=/:account/ai/models/typesafe/jev`). Handle 429s instead of hardcoding a ceiling.

## Lifecycle

> Source: https://developers.cloudflare.com/workers-ai/changelog/

Neither Cloudflare changelog mentions jev: there is no dated addition, no 1.14 announcement and no deprecation policy. Since `typesafe/jev` stayed on 1.13 after 1.14 shipped, treat each Cloudflare id as pinned to the version its card names, and re-read the card before relying on that.

## Third-party adapters that call this route

> Source: https://www.truefoundry.com/docs/ai-gateway/typesafe.md
> Source: https://vercel.com/i/jev-integrations

- TrueFoundry can front Cloudflare: base URL `https://api.cloudflare.com/client/v4/accounts/<account_id>`, model `typesafe/jev`; it unwraps the Cloudflare envelope. Do not call `/ai/run` directly through it.
- TanStack AI ships `cloudflareDecider('typesafe/jev')` in `@tanstack/ai-cloudflare` (auth `CLOUDFLARE_ACCOUNT_ID` + `CLOUDFLARE_API_TOKEN`).
- Cloudflare's own decision model, **Clef** (`@cf/cloudflare/clef`), is a competitor, not jev: see `decision-model-alternatives.md`.

## Sources
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://developers.cloudflare.com/ai/models/typesafe/jev/index.md
- https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/
- https://developers.cloudflare.com/ai/models/?provider=typesafe
- https://developers.cloudflare.com/ai/models/typesafe/jev/schema-input.json
- https://developers.cloudflare.com/workers-ai/get-started/rest-api/ (2026-09-23)
- https://developers.cloudflare.com/ai-gateway/integrations/worker-binding-methods/ (2026-09-23)
- https://developers.cloudflare.com/ai-gateway/usage/rest-api/ (2026-09-23)
- https://developers.cloudflare.com/workers-ai/platform/pricing/
- https://developers.cloudflare.com/ai-gateway/features/unified-billing/
- https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/
- https://developers.cloudflare.com/workers-ai/platform/limits/
- https://developers.cloudflare.com/workers-ai/changelog/
- https://www.truefoundry.com/docs/ai-gateway/typesafe.md
- https://vercel.com/i/jev-integrations

Fetched: 2026-11-13
