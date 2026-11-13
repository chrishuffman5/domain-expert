# Cloud availability: Bedrock, Google Cloud, Claude Platform on AWS, Microsoft Foundry (as of 2026-11-13)

Read when the workload runs on a cloud rather than a first-party API, when a Claude or OpenAI model might not exist on a given cloud, or when a feature might not exist off the first-party API. Re-verify against the source URLs. Sections still carrying 2026-08-05 data say so.

**Authority rule** (from reconciling the Anthropic platform pages): id table > per-model overview page > intro prose. Intro sentences on the Foundry and Bedrock pages are illustrative partial lists; the id tables are authoritative.

## Amazon Bedrock (Claude): two endpoints

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock and https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy (fetched 2026-11-13)

Bedrock now has two Claude surfaces. Pick the table by model:

- **bedrock-mantle** (Messages API at `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`, AWS-managed infrastructure). Use its table for every 5.x model **except Fable 5.2 / Mythos 5.2**. Examples use `anthropic-version` `2026-10-21`.
- **bedrock-runtime** (legacy `InvokeModel` / `Converse`, ARN-versioned IDs). The **only** endpoint for Fable 5.2 and Mythos 5.2. Its table omits the other 5.x models and Opus 4.8/4.7, which are reachable by InvokeModel on the same infrastructure as mantle.

### bedrock-mantle model IDs

| Model | Bedrock model ID | Access |
|---|---|---|
| Claude Fable 5.1 | `anthropic.claude-fable-5-1` | Open |
| Claude Mythos 5.1 | `anthropic.claude-mythos-5-1` | Verification |
| Claude Fable 5 | `anthropic.claude-fable-5` | Open |
| Claude Mythos 5 | `anthropic.claude-mythos-5` | not stated |
| Claude Opus 5.5 | `anthropic.claude-opus-5-5` | See Access (console-gated per account) |
| Claude Opus 5 | `anthropic.claude-opus-5` | See Access |
| Claude Opus 4.8 | `anthropic.claude-opus-4-8` | Open |
| Claude Opus 4.7 | `anthropic.claude-opus-4-7` | Open |
| Claude Sonnet 5.5 | `anthropic.claude-sonnet-5-5` | See Access |
| Claude Sonnet 5 | `anthropic.claude-sonnet-5` | Open |
| Claude Haiku 5.5 | `anthropic.claude-haiku-5-5` | See Access |
| Claude Haiku 4.5 | `anthropic.claude-haiku-4-5` | Open |

The 2026-08-05 row `anthropic.claude-mythos-preview` (invitation only, `us-east-1` regional-only) is absent from the 2026-11-13 table.

### bedrock-runtime model IDs

| Model | Base ID | Invoke with |
|---|---|---|
| Claude Fable 5.2 | `anthropic.claude-fable-5-2` | `global.anthropic.claude-fable-5-2` or `us.anthropic.claude-fable-5-2` (eu/jp/apac profiles: No) |
| Claude Mythos 5.2 (verification) | `anthropic.claude-mythos-5-2` | `global.` or `us.` prefix |
| Claude Opus 4.6 | `anthropic.claude-opus-4-6-v1` | |
| Claude Opus 4.5 | `anthropic.claude-opus-4-5-20251101-v1:0` | |
| Claude Opus 4.1 (deprecated) | `anthropic.claude-opus-4-1-20250805-v1:0` | |
| Claude Sonnet 4.6 | `anthropic.claude-sonnet-4-6` | |
| Claude Sonnet 4.5 (deprecated) | `anthropic.claude-sonnet-4-5-20250929-v1:0` | |
| Claude Sonnet 4 (deprecated) | `anthropic.claude-sonnet-4-20250514-v1:0` | |
| Claude Haiku 4.5 | `anthropic.claude-haiku-4-5-20251001-v1:0` | |

- **Models 4.6 and lower do not support API version `2026-10-21` on Bedrock**: pin the older SDK major for them.
- `computer_20251124` still works on Bedrock for Fable 5.2 (it returns 400 on every other platform).
- Bedrock sets its own lifecycle dates (AWS lifecycle page not fetched).

### Endpoint types and quotas

- **Global** endpoint covers Fable 5.1, Fable 5, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Sonnet 5.5, Sonnet 5, Haiku 5.5, Haiku 4.5 (no Mythos). No premium.
- **Regional** endpoints: **+10%**. Use an inference profile (US/EU/JP/AU) to route within a geography (2026-08-05 detail).
- Default quota **2M input tokens/minute**; raisable to **4M input TPM** without additional Anthropic approval (2026-08-05). RPM limits are enforced by AWS.

### Authentication (2026-08-05, not re-verified)

1. **Bedrock service role** (recommended): AWS-managed keys, longest-lived.
2. **IAM assumed roles**: federated identity, 12-hour max session.
3. **Bearer tokens**: short-term, 12-hour max, least preferred; minted via the `aws-bedrock-token-generator` CLI and passed as the `x-api-key` header.

### Feature gaps vs. first-party API (2026-08-05, not re-verified)

Not supported on Bedrock: URL sources for images/documents, Files API, server-side tools (code execution, web search, web fetch, advisor), Agent Skills, MCP connector, programmatic tool calling, Message Batches / Admin / Compliance / Usage-Cost API endpoints, Claude Managed Agents, and server-side fallback (implement client-side fallback instead).

## Amazon Bedrock (OpenAI)

> Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html and the OpenAI model pages, e.g. https://developers.openai.com/api/docs/models/gpt-6.1-terra (fetched 2026-11-13)

- ID pattern **`openai.<model>`**. IDs named on OpenAI's model pages: `openai.gpt-6.1-sol`, `openai.gpt-6.1-terra`, `openai.gpt-6-luna`, `openai.gpt-6-sol`, `openai.gpt-5.6-sol`, `openai.gpt-oss-120b`. **No Bedrock ID for `gpt-6-astra` appears in the corpus**; per-model Bedrock cards for terra, astra and luna were not fetched.
- `gpt-6.1-sol` card: launched 2026-09-29, Active, EOL not announced, follows OpenAI's 6-month GA deprecation notice. Context 1M, max output 131,072. Geo profile `us.openai.gpt-6.1-sol`, global `global.openai.gpt-6.1-sol`; bedrock-mantle in-Region is `us-east-1` only. **Standard Global CRIS $2 / $10**; US CRIS and in-Region **+10% ($2.20 / $11)**; **Ultrafast Global $12 / $60**; Priority, Flex and Reserved not supported.

## Google Cloud (Claude): Google managed vs Anthropic managed

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed (fetched 2026-11-13)

Anthropic's docs now describe two offerings. **"Claude Models on Google Cloud (Google managed)"** is the former "Vertex AI" page: SDK still `AnthropicVertex`, endpoint `.../publishers/anthropic/models/<id>:rawPredict`, model in the URL not the body.

Google managed model IDs: `claude-fable-5-2`, `claude-mythos-5-2`, `claude-fable-5-1`, `claude-mythos-5-1`, `claude-fable-5`, `claude-mythos-5`, `claude-opus-5-5`, `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-opus-4-5@20251101`, `claude-opus-4-1@20250805` (deprecated), `claude-opus-4@20250514` (deprecated), `claude-sonnet-5-5`, `claude-sonnet-5`, `claude-sonnet-4-6`, `claude-sonnet-4-5@20250929` (deprecated), `claude-sonnet-4@20250514` (deprecated), `claude-haiku-5-5`, `claude-haiku-4-5@20251001`.

- **Endpoints:** global; multi-region (`us`, `eu`); regional **only for Sonnet 4.6 and earlier**. Multi-region and regional cost **+10%**. Provisioned throughput needs a regional endpoint (2026-08-05), so newer models cannot use it.
- **1M context** for all 5.x models plus Opus 4.8/4.7/4.6 and Sonnet 4.6. Request payloads capped at **30 MB** (2026-08-05).
- **Fast mode** on Fable 5.2 / Mythos 5.2; Google sets the price. **Google sets lifecycle dates.**
- **Request body version (conflict to re-verify):** the 2026-08-05 page fixed the body field `anthropic_version` at `vertex-2023-10-16`; the 2026-10-21 migration page says Google managed examples now use `2026-10-21`. Check the live page before coding.
- **Feature gaps (2026-08-05, not re-verified):** no URL sources, Files API, server-side tools, Agent Skills, MCP connector, programmatic tool calling, Message Batches / Models / Admin / Compliance / Usage-Cost endpoints, Managed Agents, server-side fallback.

Install (2026-08-05): `pip install -U "anthropic[vertex]"`, `npm install @anthropic-ai/vertex-sdk`, `dotnet add package Anthropic.Vertex`, `go get github.com/anthropics/anthropic-sdk-go`. Auth: `gcloud auth application-default login`.

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed and https://platform.claude.com/docs/en/models/overview (fetched 2026-11-13)

**Google Cloud (Anthropic managed)** is a second, Anthropic-operated offering billed through Google Cloud Marketplace in CCUs ($0.01).

- Uses the **same model IDs as the Claude API** (e.g. `claude-opus-5-5`). The page has no model table; the models-overview column for it lists `claude-fable-5-2`, `claude-mythos-5-2`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`. The real gate is per organization: a model not enabled returns "Model {model} is not available for this organization's inference configuration."
- **Supported:** fast mode (Opus 5.5 since 2026-10-22; Fable 5.2), Batch API, Models API, Files API, effort and per-message effort, advisor tool, server-side fallback (beta).
- **Not supported:** API keys (Google Cloud credentials only), MCP tunnels, memory stores on self-hosted environments, pre-built self-hosted sandbox workers.

## Google Cloud (OpenAI): private preview

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai (fetched 2026-11-13)

**Private Preview only:** `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-6-luna`; global and `us` multi-region endpoints; access through the Google account team. The page brands the platform "Gemini Enterprise Agent Platform". gpt-oss is not mentioned. Do not design a production OpenAI-on-Google workload around these until GA.

## Microsoft Foundry (Claude)

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry and https://platform.claude.com/docs/en/build-with-claude/fast-mode (fetched 2026-11-13)

Deployment name defaults to the model ID. Two hosting options: **Hosted on Azure** (Global Standard and US Data Zone Standard; latest Opus/Sonnet/Haiku only) and **Hosted on Anthropic** (Global Standard; all models).

| Hosting | Model IDs |
|---|---|
| Both Azure-hosted and Anthropic-hosted | `claude-opus-5-5`, `claude-opus-5`, `claude-opus-4-8`, `claude-sonnet-5-5`, `claude-sonnet-5`, `claude-haiku-5-5`, `claude-haiku-4-5` |
| Anthropic-hosted only | `claude-fable-5-2`, `claude-mythos-5-2`, `claude-fable-5-1`, `claude-mythos-5-1`, `claude-fable-5`, `claude-mythos-5`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-opus-4-5`, `claude-sonnet-4-6`, `claude-sonnet-4-5` (deprecated) |
| Fast-mode deployments | `claude-fable-5-2-fast`, `claude-mythos-5-2-fast` (Anthropic-hosted), `claude-opus-5-5-fast` (Azure-hosted, since 2026-10-15) |

- The page's intro sentence lists Fable 5.2 among "available models" without the hosting caveat; the table (authoritative) shows it Anthropic-hosted only. Fast IDs appear only on the fast-mode page.
- Billing in Claude Consumption Units via Azure Marketplace ($0.01/CCU). **Follows the Claude API lifecycle.** No Message Batches or Models API on Foundry.
- US Data Zone Standard is the Foundry equivalent of `inference_geo: "us"`: 1.1x (2026-08-05).

## Microsoft Foundry (OpenAI)

> Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure (page updated 2026-10-29) and https://ai.azure.com/catalog/models/gpt-6.1-sol (fetched 2026-11-13)

- Azure model versions: `gpt-6.1-sol` (2026-09-29), `gpt-6.1-terra` (2026-10-26), `gpt-6-astra` (**2026-09-03**, conflicts with OpenAI's 2026-09-29 changelog date), `gpt-6-luna` (2026-09-22, Decisions API support listed), `gpt-6-sol` (2026-09-22), `gpt-5.6-sol/terra/luna` (2026-07-09). Separate short- and long-context pricing categories; some tiers need quota requests.
- `gpt-6.1-sol` catalog card: GA, Chat + Responses, 1050k context, 128k output, pay-as-you-go and reserved PTU; no prices listed.
- `gpt-oss-120b` / `gpt-oss-20b`: Preview; 120b needs a Foundry project; managed compute.
- Images: `gpt-image-1`, `-1-mini`, `-1.5`, `-2`, `-2.5-flare`, `-2.5-sunburst` (2.6 not yet listed). Realtime: `gpt-realtime-2` (2026-05-07), `gpt-realtime-2.1` and `-2.1-mini` (2026-07-07), `gpt-live-transcribe` (2026-07-29).

## Claude Platform on AWS

> Source: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws and https://platform.claude.com/docs/en/about-claude/pricing (fetched 2026-11-13; last 6.8K of 106.8K chars of the platform page unread)

Anthropic-operated, AWS Marketplace billing in CCUs ($0.01), **IDs identical to the Claude API** (no `anthropic.` prefix, no ARNs), follows Anthropic's lifecycle. New models typically launch there the same day.

- Model table: `claude-fable-5-2`, `claude-fable-5-1`, `claude-fable-5`, `claude-opus-5-5`, `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-opus-4-5`, `claude-sonnet-5-5`, `claude-sonnet-5`, `claude-sonnet-4-6`, `claude-sonnet-4-5` (deprecated), `claude-haiku-5-5`, `claude-haiku-4-5`.
- **No Mythos** (5, 5.1 or 5.2) on the page, and the Mythos 5.2 page omits this platform: treat Mythos as unavailable there.
- **Not available:** fast mode, HIPAA readiness, OAuth, OpenAI-compatible endpoints, workspace member management, Claude Code workspace/analytics.
- All AWS commercial regions; endpoint `aws-external-anthropic.{region}.api.aws`; the region does not pin inference: use `inference_geo` (1.1x for `"us"`, 2026-08-05).

## CCU billing and partner pricing (2026-08-05)

> Source: https://platform.claude.com/docs/en/about-claude/pricing (fetched 2026-08-05)

Claude Platform on AWS, Microsoft Foundry and (per the 2026-11-13 fetch) Google Cloud Anthropic managed use **Claude Consumption Units**: token usage is rated in USD at standard per-model rates, discounts applied, then converted at **$0.01/CCU** and reported to the marketplace. Postpaid only, no prepaid credits.

Bedrock and Google Cloud (Google managed) are **partner-operated** with **independent pricing and lifecycle**. Anthropic's $/MTok rates are the first-party reference; confirm partner rates on the AWS Bedrock and Google Cloud pricing pages. **Gap:** the Google Cloud pricing page did not surface a Claude table in the 2026-08-05 pass.

## Choosing a platform

- Default to the **first-party API**: it is the only surface with the complete feature set.
- Need **Fable 5.2 on Bedrock**? Only bedrock-runtime (`global.`/`us.` profiles) serves it; mantle does not.
- Need **Mythos** with marketplace billing? Not on Claude Platform on AWS; Foundry (Anthropic-hosted), both Google offerings and Bedrock list Mythos IDs, all limited access (Mythos 5.2 needs Anthropic verification).
- Need **fast mode** off first-party? Foundry and Google Cloud have it for Fable 5.2 and/or Opus 5.5; Claude Platform on AWS does not.
- Need **Batches/Files/Models API** on Google Cloud? Choose the Anthropic managed offering; the Google managed one lacked them (2026-08-05).
- **OpenAI on a hyperscaler:** Azure Foundry is GA (e.g. `gpt-6.1-sol`); Bedrock serves `openai.<model>` IDs (no astra found); Google Cloud is private preview only.
- Prefer **global endpoints** unless residency forces regional: regional costs 10% more on Bedrock (Claude and OpenAI) and Google.
- Choose an **Anthropic-operated** marketplace surface (Claude Platform on AWS, Foundry, Google Cloud Anthropic managed) when you want Anthropic's deprecation timeline rather than the cloud's.

## Sources

- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
- https://platform.claude.com/docs/en/build-with-claude/fast-mode
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/api/migration-2026-10-21
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html
- https://developers.openai.com/api/docs/models/gpt-6.1-terra
- https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/openai
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- https://ai.azure.com/catalog/models/gpt-6.1-sol
- https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai (2026-08-05 sections)

Fetched: 2026-11-13 (sections marked 2026-08-05 were carried forward, not re-verified)
