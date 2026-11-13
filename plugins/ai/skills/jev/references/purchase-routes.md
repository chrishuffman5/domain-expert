# Where to buy or route jev outside api.typesafe.ai

Read this when a user wants jev through a cloud or gateway they already pay for, needs to know whether a provider carries 1.13 or 1.14, or asks "is jev on Bedrock / Azure / Vertex?". Snapshot as of **2026-11-13**; every row can change, so re-check the cited page before committing an id or price to config.

Two kinds of route exist:
- **Resale** (the provider bills you; no TypeSafe account): Cloudflare, Vercel, OpenRouter, DigitalOcean, Databricks, Netlify, Requesty, LLM Gateway, ZenMux, Lava (managed mode), probably Runware.
- **BYOK proxy** (you bring a TypeSafe key; TypeSafe bills, the gateway adds routing, logging, budgets or guardrails): LiteLLM, Portkey, Kong, TrueFoundry, Zuplo, Pydantic AI Gateway, Lava (unmanaged mode), agentgateway. Vercel and OpenRouter also accept BYOK.

For generic gateway mechanics unrelated to jev, use `inference-providers`. Cloudflare details: `cloudflare-workers-ai.md`.

## Matrix

> Source: per-provider sections below (each cites its page)

| Provider | Model ids | 1.13 / 1.14 | Endpoint | Credential | Billing | Status | Notes |
|---|---|---|---|---|---|---|---|
| Cloudflare Workers AI | `typesafe/jev`, `typesafe/jev-1.14.0` | yes / yes | `env.AI.run(...)`; REST `.../accounts/$ID/ai/run` (model in body) | CF token (Workers AI Read + Edit) or binding | Card: $0.042 in, $0 out. **Billing path not stated** | not stated | 32,000 ctx on card; ZDR "Yes"; images and Box beta |
| Vercel AI Gateway | `typesafe-ai/jev`, `typesafe-ai/jev-1.13.0`, `typesafe-ai/jev-1.14.0` | yes / yes | `https://ai-gateway.vercel.sh/typesafe/v1/systemone`; `/v1/decisions`; AI SDK | `AI_GATEWAY_API_KEY` or Vercel OIDC | Vercel bills; example shows `surchargeCost: "0"`; BYOK bills TypeSafe | no preview label | `/v1/evaluate` deprecated; decision fallbacks |
| OpenRouter | `typesafe/jev-1.14`, `typesafe/jev-1.13`, `~typesafe/jev-latest` | yes / yes | `POST https://openrouter.ai/api/alpha/decisions`; `/api/v1/systemone` | `OPENROUTER_API_KEY` | OpenRouter credits, $0.042 / $0; BYOK supported | **alpha** | 262,144 ctx (long context auto-on) |
| DigitalOcean | `typesafe-jev-1.13.0` | yes / no | `POST https://inference.do-ai.run/v1/systemone` | model access key (`MODEL_ACCESS_KEY`) | DO bills $0.042 in, output N/A, Standard tier | not stated | no images; tier-gated; Vercel upstream |
| Databricks | `system.ai.typesafeai-jev-1-14-0` (endpoint `databricks-typesafeai-jev-1-14-0`) | no / yes | Unity Gateway, System One API | Databricks token | pay-per-token via Databricks; price not stated | admin-enabled **preview** | TypeSafe terms govern |
| Netlify AI Gateway | `jev-latest`, `jev-1.14.0` | (doc'd) / yes | `@typesafe-ai/sdk` from Netlify Functions, no base URL | injected by Netlify | Netlify credits | not stated | ~32,000-token note |
| Requesty | `typesafe/jev-1.14.0`, `typesafe/jev-1.13.0`, `typesafe/jev-latest` | yes / yes | `POST https://router.requesty.ai/v1/systemone`; chat routes | Requesty key | provider rate +5% PAYG, 0% BYOK | **experimental** | 64K ctx; separate approval for decisions |
| LLM Gateway | `jev-1.14.0`, `jev-1.13.0`, `jev`, `jev-latest`, `jev-preview` | yes / yes | `https://api.llmgateway.io/v1` | LLM Gateway key | $0.042 / $0; markup not stated | not stated | request shape unverified |
| ZenMux | `typesafe/jev-1.13`, `typesafe/jev-1.14` | yes / yes | not on page | ZenMux key | $0.042 in | not stated | listing only |
| Runware | not captured | yes / ? | "compatible API" | Runware key | not captured | not stated | listing only |
| Lava | `jev-latest`, `jev-1.13.0` | yes / ? | forward proxy `https://api.lava.so/v1/forward?u=...` | Lava forward token | managed (Lava keys) or BYOK; markup not stated | not stated | |
| LiteLLM (self-hosted) | `jev-latest`, `jev-preview`, `jev-1.13.0`, `jev-1.14.0` | yes / yes | `/typesafe/v1/systemone`, `/v1/systemone`, `/v1/decisions` | proxy holds `TYPESAFE_API_KEY` | BYOK; TypeSafe bills | GA docs | forwards `TypeSafe-Danger-Zone-*` |
| Portkey | `@slug/jev-latest`, pin `jev-1.13.0` | yes / ? | `POST https://api.portkey.ai/v1/decisions` | `x-portkey-api-key` + stored TypeSafe key | BYOK | not stated | before-request guardrails only |
| Kong AI Gateway 2.2+ | `jev-latest` target | yes / ? | route `/jev` → `/jev/v1/systemone` | stored TypeSafe key | BYOK | not stated | missing/invalid key → 403 |
| TrueFoundry | `jev-1.13.0`, `jev-latest` | yes / ? | `{GATEWAY_BASE_URL}/v1/systemone`, `/v1/decisions` | `TFY_API_KEY` + stored key | BYOK | not stated | can front Cloudflare `typesafe/jev` |
| Zuplo | `jev/jev-latest`, `jev/jev-1.13.0`, `jev/jev-preview` | yes / not listed | `/v1/systemone` on your app URL | app API key + stored key | BYOK; catalog cost headers | not stated | never falls back |
| Pydantic AI Gateway | `jev-latest` | via alias | `https://gateway-us.pydantic.dev/proxy/typesafe/v1/systemone` | gateway key + stored TypeSafe key | BYOK; metered | not stated | input guardrails; no streaming |

"?" means the fetched page names no 1.14 id. Prices are list prices shown on the provider's page; none publishes a jev-specific rate limit.

## Cloudflare Workers AI

> Source: https://developers.cloudflare.com/ai/models/typesafe/jev/
> Source: https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/
> Source: https://developers.cloudflare.com/ai/models/?provider=typesafe

Two live cards: `typesafe/jev` (version 1.13) and `typesafe/jev-1.14.0` (1.14, Box beta). Both show $0.042 per 1M input, $0 cached, $0 output, 32,000 context, third-party, ZDR "Yes". No card or pricing page ties jev to Neurons, Workers Paid or Unified Billing credits, and none states a rate limit or release date. **Never state a Cloudflare billing path.** Full transport detail: `cloudflare-workers-ai.md`.

## Vercel AI Gateway

> Source: https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
> Source: https://vercel.com/docs/ai-gateway/modalities/decision
> Source: https://vercel.com/changelog/typesafe-ais-jev-1-14-is-now-available-on-ai-gateway

Three surfaces, all billed through AI Gateway:
1. **TypeSafe-compatible**: point `TypeSafeClient` at `https://ai-gateway.vercel.sh/typesafe` (`POST /typesafe/v1/systemone`, `GET /typesafe/v1/models`). Same request and response shapes plus `provider_metadata.gateway` cost fields.
2. **Decisions HTTP API (OpenAI-compatible)**: `POST https://ai-gateway.vercel.sh/v1/decisions` with `input` and a `questions` **array** of `predicate | choice | score` (+ `box`). `POST /v1/evaluate` is deprecated.
3. **AI SDK**: `experimental_decide` (`ai` 7.0.128+). `experimental_evaluate` and `gateway.evaluationModel()` are deprecated aliases; never use them in new code.

```bash
curl https://ai-gateway.vercel.sh/typesafe/v1/systemone \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "typesafe-ai/jev", "state": "I was charged twice for my subscription.",
       "questions": {"refund": {"type": "noul", "instructions": "Is the customer asking for money back?"}}}'
```

- BYOK: store a TypeSafe key under BYOK to bill TypeSafe directly.
- Upstream providers of `typesafe-ai/jev`: typesafe-ai and digitalocean.
- Long context (experimental): `providerOptions.typesafe.longContext: true`. Per-request ZDR and No Training are available.
- **Decision fallbacks**: `providerOptions.gateway.models` with `{ model, when: { question, confidenceBelow } }` re-runs uncertain decisions on another model. Fallback headers are `x-ai-gateway-decision-fallback-*` (the `-evaluation-` names are deprecated). Triggered requests bill both stages. An LLM-fallback answer returns `confidence: 0` and `probabilities: {}`, meaning *unavailable*, not zero.
- Errors: validation and auth errors use TypeSafe's shape (`message`, `error_type`); credits, unknown model and provider failures use the gateway shape (`error.message`, `error.type`). Handle both.
- In `ai` 7.0.133+ an array `state` is a list of parts, not JSON data. Wrap JSON arrays in an object.

## OpenRouter

> Source: https://openrouter.ai/blog/insights/what-is-jev/
> Source: https://openrouter.ai/docs/guides/community/jev.md
> Source: https://openrouter.ai/docs/api/reference/decisions

- Ids: `typesafe/jev-1.14` (snapshot `typesafe/jev-1.14-20261014`), `typesafe/jev-1.13`, `~typesafe/jev-latest`.
- `POST https://openrouter.ai/api/alpha/decisions` is **alpha** ("the shape may change"). `POST https://openrouter.ai/api/v1/systemone` serves TypeSafe SDKs with `base_url="https://openrouter.ai/api"`; a bare `jev-1.14` maps to `typesafe/jev-1.14`.
- $0.042 / $0 (as of 2026-10-16); each response carries `usage.cost`. With BYOK, `usage.is_byok` is true and `cost` covers only OpenRouter's fee.
- Context 262,144: OpenRouter **auto-enables long context** above about 32,000 bytes of text or with any image (slower, less accurate).
- Box is rejected with 400 on 1.13. Scores varied run to run (1.21 vs 1.17 in OpenRouter's own test), so threshold on bands.
- The model page `openrouter.ai/typesafe/jev-1.14` returned 404 at fetch time.

## LiteLLM (BYOK, self-hosted)

> Source: https://docs.litellm.ai/docs/pass_through/typesafe
> Source: https://docs.litellm.ai/docs/decisions.md

- Pass-through `POST /typesafe/v1/systemone` and `GET /typesafe/v1/models`; unified `/v1/systemone` (load balancing, fallbacks) and OpenAI-format `/v1/decisions` (since LiteLLM v1.104.2; TypeSafe images and Box need v1.106.0).
- Forwards only headers starting `TypeSafe-Danger-Zone-`. No streaming, no end-user tracking. Cost logged under the resolved version.
- Access lists: `typesafe/*` allows every jev name; `typesafe/jev-latest` does **not** allow bare `jev-latest`. A disallowed model returns 403 (`team_model_access_denied`).
- Jev can drive LiteLLM's Auto Router (`classifier_type: jev`).

## DigitalOcean

> Source: https://docs.digitalocean.com/products/inference/how-to/use-system-one-api/
> Source: https://docs.digitalocean.com/products/inference/details/pricing/

`POST https://inference.do-ai.run/v1/systemone`, model `typesafe-jev-1.13.0` (no 1.14 id documented), Bearer model access key. Not OpenAI-compatible; no streaming; no image input; 64K / 32K limits. Pricing row "Jev": $0.042 per 1M input, output N/A, tier Standard. A qualifying account tier is required. EU data residency is not currently available through DigitalOcean. Governed by TypeSafe's MCA.

## Databricks

> Source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models
> Source: https://docs.databricks.com/gcp/en/machine-learning/model-serving/query-systemone-models

- "TypeSafe AI Jev 1.14.0": service name `system.ai.typesafeai-jev-1-14-0`, endpoint `databricks-typesafeai-jev-1-14-0`, text and image input, provider-hosted by TypeSafe AI, Inc. through Unity Gateway. Only 1.14.0 is listed.
- An account admin must enable the **"TypeSafe AI Models" preview**. TypeSafe's terms and privacy policy govern use, not the Databricks customer agreement.
- Pay-per-token through Databricks. **Price, regions, rate and context limits are not stated.**
- The query page documents the System One path `https://<workspace_host>/ai-gateway/typesafe/v1/systemone` (shown for OpenJev). Do not confuse **OpenJev** (`system.ai.openjev-qwen35-4b`, an open Qwen3.5-based model hosted by Databricks) with TypeSafe's Jev; see `decision-model-alternatives.md`.

## Netlify AI Gateway

> Source: https://www.netlify.com/changelog/typesafe-jev-ai-gateway/
> Source: https://netlify.com/changelog/typesafe-jev-1-14-0-ai-gateway

Zero-config from Netlify Functions: `@typesafe-ai/sdk` with no key, provider config or base URL (the gateway injects credentials). Usage bills to Netlify credits. `jev-1.14.0` is available in Scheduled, Background and Edge functions. The original changelog documents `jev-latest` as 1.13.0 and says Node 20+; SDK 0.7.0 needs Node ≥ 22. The 2026-09-17 launch date is search-snippet only.

## Requesty

> Source: https://docs.requesty.ai/features/decisions.md
> Source: https://www.requesty.ai/models/typesafe

- **Experimental**: "request and response shapes may change without a deprecation period."
- `POST https://router.requesty.ai/v1/systemone` with `typesafe/jev-1.14.0` (text only on this endpoint). Chat Completions, Messages and Responses also accept questions via `response_format` / `output_config.format` / `text.format` with `type: "questions"`. No streaming.
- The decisions endpoint and chat APIs are approved separately; a mismatch returns 403. Refusals appear as `"refusal"` answers.
- Pricing: provider rate plus 5% pay-as-you-go, 0% with your own keys. The same site's FAQ says "no markup": internally inconsistent, verify before quoting.

## Other resale listings

> Source: https://llmgateway.io/providers/typesafe
> Source: https://zenmux.ai/typesafe
> Source: https://runware.ai/models/typesafe-jev
> Source: https://www.lava.so/docs/gateway/providers/typesafe.md

- **LLM Gateway**: ids above, $0.042 / $0, 262.1k context, vision listed. Its sample uses chat completions and conflicts with jev's System One shape, so the **request shape is unverified**.
- **ZenMux**: `typesafe/jev-1.13`, `typesafe/jev-1.14`, $0.042 per 1M input; no endpoint on the page.
- **Runware**: "Available via compatible API" for Jev 1.13; id, price and endpoint not captured.
- **Lava**: forward proxy to `api.typesafe.ai/v1/systemone`, managed (Lava keys) or unmanaged mode; markup not stated.

## BYOK gateways

> Source: https://portkey.ai/docs/integrations/llms/typesafe.md
> Source: https://developer.konghq.com/ai-gateway/ai-providers/typesafe/
> Source: https://www.truefoundry.com/docs/ai-gateway/typesafe.md
> Source: https://zuplo.com/docs/ai-gateway/jev.md
> Source: https://pydantic.dev/articles/jev-pydantic-ai-gateway.md
> Source: https://agentgateway.dev/docs/standalone/main/integrations/llm/guardrails/jev.md
> Source: https://www.getmaxim.ai/bifrost/blog/typesafe-system-one-models-and-new-v1-decisions-endpoint.md

- **Portkey**: accepts both the System One body and OpenAI-style `input` + `questions` array on `/v1/decisions`; no streaming.
- **Kong** (AI Gateway 2.2+): `decisions` capability; no guardrails, semantic caching or prompt rate limiting for it.
- **TrueFoundry**: model type "Decision", output cost 0; also fronts Cloudflare's `typesafe/jev` and unwraps the CF envelope. Its own blog from 2026-09 said "no integration"; the docs page supersedes it.
- **Zuplo**: refuses jev on chat/responses/messages routes; `X-Cost-USD` headers; budgets count output tokens too; 429 on exhausted budget.
- **Pydantic AI Gateway**: `typesafe` in the URL is the route name you chose; works with `TypeSafeClient(base_url=...)` and `TypeSafeProvider(base_url=...)`; streaming refused.
- **agentgateway**: translates OpenAI Decisions requests to jev's `/v1/systemone` and can split one virtual model between jev and an OpenAI model.
- **Bifrost** (v2.2.2): `/v1/decisions` plus a byte-for-byte `/typesafe` drop-in for TypeSafe SDKs (`TYPESAFE_BASE_URL`), with LLM fallbacks. Its blog names `jev-1.13.0`, `jev-latest`, `jev-preview`; credential and billing model were not captured.

**SDK gotcha on any gateway**: Python SDK 0.7.5 and JS SDK 0.7.0 zstd-compress request bodies by default, and TypeSafe warns "non-official APIs may not support it yet". If a gateway rejects the body, construct the client with compression disabled (`compression: false` in JS; the Python client takes a `compression` constructor argument).

## Not available (as of 2026-11-13)

> Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html
> Source: https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-model-reference.html
> Source: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure
> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners
> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models
> Source: https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm
> Source: https://www.ibm.com/docs/en/watsonx/saas?topic=solutions-supported-foundation-models

**Clean negatives** (the catalog was fetched and lists no TypeSafe/Jev):
- AWS Bedrock (serverless model cards) and Bedrock Marketplace.
- Microsoft Foundry: "sold directly by Azure" and partner/community catalogs.
- Google Vertex AI partner models (MaaS).
- Oracle OCI Generative AI.
- IBM watsonx.ai.
- Also absent from fetched catalogs: Together AI, Groq, Snowflake Cortex (its regional-availability page was not fetched), Hugging Face Hub (0 results; jev weights are unpublished).

**Weak negatives** (partial catalog or search only): Fireworks AI, Baseten (its library shows its own decision models, not jev), Eden AI.

**UNVERIFIED, not denied**: AWS Marketplace, Azure Marketplace and Google Cloud Marketplace / Model Garden search pages could not be read (JS-rendered, 403 or header overflow). Say "not in the Bedrock, Foundry or Vertex catalogs as of 2026-11-13; marketplace listings unverified."

Not a sales route: Modal ran jev inference for TypeSafe ("served 1 trillion tokens for Jev within three days of launch") but does not sell it (https://modal.com/blog/typesafeai-case-study).

## Look-alikes to reject

> Source: https://aws.amazon.com/marketplace/pp/prodview-cpbvpwpvmgu26
> Source: https://builder.aws.com/content/3K0rpiZCCJzqYrmxpWFuJtGotsx/jev-on-aws-building-fast-ai-decision-layers-with-aws (community)

- **AWS Marketplace "JEV-27B Decision Model" (seller Warp Drive) is not TypeSafe's Jev.** It is a self-hosted AMI/CloudFormation stack on a g6e GPU in your own account (OpenAI-compatible API plus `/v1/decide`), described as an Apache-2.0 base with a decision LoRA head, priced at a 5-day free trial then $0.02/hour plus AWS infrastructure. The listing never mentions TypeSafe. Never present it as jev on AWS.
- **Never use the `jevai.info` endpoint.** A community AWS Builder article POSTs to `https://jevai.info/v1/systemone`, a non-TypeSafe domain. The official endpoint is `https://api.typesafe.ai`. Sending a key or data there would hand both to an unknown party.
- On AWS today, call jev as an external HTTPS dependency (for example from Lambda) to `api.typesafe.ai`; a community review notes there is no PrivateLink or VPC endpoint (https://www.factualminds.com/examples/architecture-blog-2026/jev-typesafe-aws/README.md).

## Sources
- https://developers.cloudflare.com/ai/models/typesafe/jev/
- https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/
- https://developers.cloudflare.com/ai/models/?provider=typesafe
- https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe
- https://vercel.com/docs/ai-gateway/modalities/decision
- https://vercel.com/ai-gateway/models/jev
- https://vercel.com/ai-gateway/models/jev-1.13.0
- https://vercel.com/ai-gateway/models/jev-1.14.0
- https://vercel.com/changelog/typesafe-ais-jev-1-14-is-now-available-on-ai-gateway
- https://openrouter.ai/blog/insights/what-is-jev/
- https://openrouter.ai/docs/guides/community/jev.md
- https://openrouter.ai/docs/api/reference/decisions
- https://docs.litellm.ai/docs/pass_through/typesafe
- https://docs.litellm.ai/docs/decisions.md
- https://docs.digitalocean.com/products/inference/how-to/use-system-one-api/
- https://docs.digitalocean.com/products/inference/details/pricing/
- https://docs.digitalocean.com/products/gradient-ai-platform/details/models
- https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models
- https://docs.databricks.com/gcp/en/machine-learning/model-serving/query-systemone-models
- https://www.netlify.com/changelog/typesafe-jev-ai-gateway/
- https://netlify.com/changelog/typesafe-jev-1-14-0-ai-gateway
- https://docs.requesty.ai/features/decisions.md
- https://www.requesty.ai/models/typesafe
- https://llmgateway.io/providers/typesafe
- https://zenmux.ai/typesafe
- https://runware.ai/models/typesafe-jev
- https://www.lava.so/docs/gateway/providers/typesafe.md
- https://portkey.ai/docs/integrations/llms/typesafe.md
- https://developer.konghq.com/ai-gateway/ai-providers/typesafe/
- https://www.truefoundry.com/docs/ai-gateway/typesafe.md
- https://zuplo.com/docs/ai-gateway/jev.md
- https://pydantic.dev/articles/jev-pydantic-ai-gateway.md
- https://agentgateway.dev/docs/standalone/main/integrations/llm/guardrails/jev.md
- https://www.getmaxim.ai/bifrost/blog/typesafe-system-one-models-and-new-v1-decisions-endpoint.md
- https://docs.typesafe.ai/sdk/python/changelog.md
- https://docs.typesafe.ai/sdk/javascript.md
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-model-reference.html
- https://aws.amazon.com/marketplace/pp/prodview-cpbvpwpvmgu26
- https://aws.amazon.com/marketplace/search/results?searchTerms=typesafe (inconclusive)
- https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners
- https://marketplace.microsoft.com/en-us/marketplace/apps?search=typesafe (403)
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models
- https://cloud.google.com/model-garden (inconclusive)
- https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm
- https://www.ibm.com/docs/en/watsonx/saas?topic=solutions-supported-foundation-models
- https://docs.together.ai/docs/serverless-models
- https://console.groq.com/docs/models
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql
- https://docs.fireworks.ai/getting-started/models
- https://www.baseten.co/library/
- https://www.edenai.co/docs
- https://huggingface.co/models?search=typesafe%20jev (community)
- https://modal.com/blog/typesafeai-case-study
- https://builder.aws.com/content/3K0rpiZCCJzqYrmxpWFuJtGotsx/jev-on-aws-building-fast-ai-decision-layers-with-aws (community; endpoint NOT to be used)
- https://www.factualminds.com/examples/architecture-blog-2026/jev-typesafe-aws/README.md (community)

Fetched: 2026-11-13
