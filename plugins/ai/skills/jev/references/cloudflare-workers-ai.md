# jev on Cloudflare Workers AI (`typesafe/jev`)

Read this when you are calling jev from a Worker, through Cloudflare's REST API, or through Cloudflare AI Gateway. It covers jev-specific details only. General Workers AI platform usage is out of scope.

## What the model card confirms

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/

- Model id is `typesafe/jev`. It is a **third-party** model from provider TypeSafe, in the category "Text Generation / Structured Evaluation".
- The example responses report `jev-1.13.0`.
- It uses the same Noul/Choice/Score payload as the direct API. The published input schema has **no `model` field** and sets `additionalProperties: false`.
- "Context Window: 32,000 tokens" on the card is the **inner** limit (state + the longest question). TypeSafe's docs define nested limits: 64k per request and 32k for state + the longest question. It is not a smaller model.
- Pricing: the card says only "View pricing in the Cloudflare dashboard".
- Terms: the card links to TypeSafe's own legal page. Cloudflare publishes no separate jev EULA.
- The card does not mention streaming, batch, an OpenAI-compatible endpoint or AI Gateway specifics. These are **absent, not denied**.

## Worker binding

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/
> Source: https://developers.cloudflare.com/workers-ai/get-started/workers-wrangler/

```jsonc
// wrangler.jsonc
{ "ai": { "binding": "AI" } }
```
```ts
const res = await env.AI.run('typesafe/jev', {
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
- Scaffold with `npm create cloudflare@latest`.
- Run `wrangler types` after every binding change.
- Test with `npx wrangler dev` and ship with `npx wrangler deploy`.
- This path needs no TypeSafe API key. Usage bills to the Cloudflare account.

## REST: the model id goes in the BODY

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/
> Source: https://developers.cloudflare.com/workers-ai/get-started/rest-api/

```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "typesafe/jev",
    "input": { "state": "...", "questions": { "q": { "type": "noul", "instructions": "..." } } }
  }'
```

Send `model` and `input` as **siblings** at the top level, and POST to the bare `.../ai/run` endpoint.
- Never append the model to the path. The path form `.../ai/run/@cf/meta/llama-...` on Cloudflare's generic get-started page is for first-party `@cf/` models.
- Never put `model` inside `input`. The schema rejects extra properties.

Token and envelope details:
- The token needs **Workers AI - Read** and **Workers AI - Edit**. Create it on the dashboard's Workers AI → "Use REST API" page, which also shows the Account ID.
- The generic REST page documents a `{result, success, errors, messages}` envelope. The jev model card shows the `{model, answers, usage}` payload unwrapped. Expect the payload under `result` on REST, and verify against a live response.

## AI Gateway

> Source: https://developers.cloudflare.com/ai-gateway/integrations/worker-binding-methods/
> Source: https://developers.cloudflare.com/ai-gateway/usage/rest-api/

```js
await env.AI.run("typesafe/jev", { state, questions }, { gateway: { id: "default" } });
```
- `gateway.id` is required. `"default"` auto-creates a gateway on the first authenticated request.
- Other options: `skipCache`, `cacheTtl`, `cacheKey`, `collectLog`, `metadata`.
- Retry and fallback behaviour for the gateway route is **not documented**.
- REST: use the universal `/ai/run` endpoint, with model params nested under `input` and the third-party model addressed as `typesafe/jev`. Workers AI models routed through a gateway need the `cf-aig-gateway-id` header.
- `/ai/v1/chat/completions` (OpenAI-compatible) and `/ai/v1/messages` (Anthropic-compatible) are for chat models. No source says they accept jev. Use `/ai/run`.
- Do not confuse this with **Vercel** AI Gateway, which is a different company's product. See `api-and-sdks.md`.

## Unconfirmed: billing path and rate limits

> Source: https://developers.cloudflare.com/ai-gateway/features/unified-billing/
> Source: https://developers.cloudflare.com/workers-ai/platform/pricing/
> Source: https://developers.cloudflare.com/workers-ai/platform/limits/

**Billing path: UNCONFIRMED.** No official Cloudflare page says how `typesafe/jev` is billed.
- The Workers AI pricing page (Neurons: 10,000 free per day, then $0.011 per 1,000 on Workers Paid) does not list jev.
- The Unified Billing page (prepaid AI Gateway credits, 5% markup) names OpenAI, Anthropic, Google AI Studio, Vertex, xAI and Groq. It does not name TypeSafe.
- Community sources claim jev bills only through prepaid AI Gateway credits with no free tier, failing with "Insufficient AI Gateway credits". This is community-tier and unverified (https://github.com/Mumega-com/mupot/issues/1437).

Tell users to check the Cloudflare dashboard (`https://dash.cloudflare.com/?to=/:account/ai/models/typesafe/jev`) and the current Cloudflare pricing docs. Never assert either billing mechanism.

A general Unified Billing gotcha is documented for eligible providers and not confirmed for jev: requests default to Unified Billing credits even when BYOK keys are configured, unless "Require provider credentials" is enabled.

**Rate limits: UNCONFIRMED for jev.**
- The Workers AI limits page is organised by task type and does not name jev. The 300 req/min text-generation figure is only an inference.
- Models that require Workers Paid get 20 req/min on standard billing, or 50 req/min with AI Gateway credits. Whether jev falls into that bucket is unknown.
- Handle 429s instead of hardcoding a ceiling.

## Data handling and token scope

> Source: https://developers.cloudflare.com/workers-ai/platform/data-usage/
> Source: https://developers.cloudflare.com/workers-ai/get-started/rest-api/

Cloudflare's data commitments:
- It does not train on Customer Content, does not share it with other customers, and does not persist inputs or outputs unless you wire in storage yourself (R2, KV and similar).
- It does not describe what reaches TypeSafe when a third-party model runs. TypeSafe's own privacy terms are the only sourced material; see `limitations-and-security.md`.

Token scope:
- Workers AI Read/Edit scopes are **account-wide**. A token can call every Workers AI model, and you cannot scope a token to jev only.
- Community report, unverified: a token with only AI Gateway permission returns `401` with code `10000` on `/ai/*` endpoints. The two scopes are separate.

## Lifecycle gaps

> Source: https://developers.cloudflare.com/workers-ai/changelog/
> Source: https://aiengineerguide.com/til/typesafe-ai-jev-cloudflare-ai-gateway/

- Neither Cloudflare changelog mentions jev. There is no dated addition and no deprecation policy.
- Community observation: "the model version specified in responses may differ from your request". `typesafe/jev` does not pin a build. Log `response.model` on every call.

## Sources
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://developers.cloudflare.com/ai/models/typesafe/jev/schema-input.json
- https://developers.cloudflare.com/workers-ai/get-started/workers-wrangler/
- https://developers.cloudflare.com/workers-ai/get-started/rest-api/
- https://developers.cloudflare.com/ai-gateway/integrations/worker-binding-methods/
- https://developers.cloudflare.com/ai-gateway/usage/rest-api/
- https://developers.cloudflare.com/ai-gateway/features/unified-billing/
- https://developers.cloudflare.com/workers-ai/platform/pricing/
- https://developers.cloudflare.com/workers-ai/platform/limits/
- https://developers.cloudflare.com/workers-ai/platform/data-usage/
- https://developers.cloudflare.com/workers-ai/changelog/
- https://developers.cloudflare.com/changelog/product/workers-ai/
- https://aiengineerguide.com/til/typesafe-ai-jev-cloudflare-ai-gateway/ (community)
- https://github.com/Mumega-com/mupot/issues/1437 (community)

Fetched: 2026-09-23
