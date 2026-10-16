# AI Models

**As of 2026-10-16.** This is a curated, popularity-weighted catalog of 60 distinct model identities, not a claim to rank the exact global top 60. The catalog distinguishes provider-reported usage, platform traffic, downloads and weaker ecosystem proxies; missing comparable evidence stays marked unknown.

Use the family skills for model identity, capabilities, tradeoffs, versions and suitability. Use the existing `ai` plugin for API/SDK calls, agent harnesses, cloud or aggregator routing, training, and eval infrastructure. If the `ai-models` plugin is unavailable, `ai` has only its narrower Anthropic/OpenAI/Google tier references and Jev integration guidance.

## Installation and maintenance

```text
/plugin install ai-models@domain-expert
```

From the repository root, validate the catalog and its regression cases:

```bash
python plugins/ai-models/scripts/validate_catalog.py
python plugins/ai-models/scripts/test_validate_catalog.py
claude plugin validate .
claude plugin validate ./plugins/ai-models
```

Refresh model facts from the linked official sources before changing the catalog. Preserve distinct model identities, scoped adoption evidence, and explicit unknowns; update the model reference, family routing and trigger cases together. Recalculate repository skill counts from directories rather than adding model rows to the skill total.

## Catalog

Adoption evidence is explicitly classified per entry as observed usage, a proxy, or unknown. See `selection-methodology.md` for counts and limits.

Rows are grouped by family. The catalog ID is the exact identity recorded for each entry; it can be a callable provider model ID, a checkpoint repository ID, or a release name. `identity_kind` and `callable_id` distinguish the catalog identity from a universal API identifier. Providers may expose multiple deployment/profile forms, which the family reference explains. Adoption notes retain the signal scope and should not be compared across unlike counters.

### amazon-nova

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Amazon Nova 2 Lite | `us.amazon.nova-2-lite-v1:0` | general | active | Unknown | [details](skills/amazon-nova/references/versions/us-amazon-nova-2-lite-v1-0.md) |
| Amazon Nova 2 Sonic | `us.amazon.nova-2-sonic-v1:0` | multimodal | active | Unknown | [details](skills/amazon-nova/references/versions/us-amazon-nova-2-sonic-v1-0.md) |

### claude

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Claude Opus 5.5 | `claude-opus-5-5` | frontier, general, coding, agentic | active (latest) | Unknown | [details](skills/claude/references/versions/claude-opus-5-5.md) |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | general, coding, agentic | active (latest) | Unknown | [details](skills/claude/references/versions/claude-sonnet-5-5.md) |
| Claude Haiku 5.5 | `claude-haiku-5-5` | general, low-latency, classification | active (latest) | Unknown | [details](skills/claude/references/versions/claude-haiku-5-5.md) |
| Claude Fable 5.1 | `claude-fable-5-1` | reasoning, agentic, coding | active (latest) | Unknown | [details](skills/claude/references/versions/claude-fable-5-1.md) |

### cohere-command

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Cohere Command A+ | `command-a-plus-05-2026` | frontier | active | Unknown | [details](skills/cohere-command/references/versions/command-a-plus-05-2026.md) |
| Cohere Command A Reasoning | `command-a-reasoning-08-2025` | reasoning | active | Unknown | [details](skills/cohere-command/references/versions/command-a-reasoning-08-2025.md) |
| Cohere Command A Vision | `command-a-vision-07-2025` | multimodal | active | Unknown | [details](skills/cohere-command/references/versions/command-a-vision-07-2025.md) |

### deepseek

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| DeepSeek-V4.1-Flash | `deepseek-flash` | reasoning | Current hosted API model; legacy V4-Flash aliases route to this model. | OpenRouter ranked DeepSeek V4.1 Flash first in the displayed tokens-processed table with 40.5T tokens and +37%; usage data was through… | [details](skills/deepseek/references/versions/deepseek-flash.md) |
| DeepSeek-V4-Pro-0813 | `deepseek-v4-pro` | reasoning | Current hosted API model. | Quantitative usage data not found in inspected official sources; official current-model listing is availability evidence only. | [details](skills/deepseek/references/versions/deepseek-v4-pro.md) |
| DeepSeek-R1 | `DeepSeek-R1` | open-weight | Open weights remain downloadable and self-hostable; current hosted API support was not confirmed in the current model list. | HF: 14.4k likes and 244 community discussions ; platform engagement proxy, not downloads or production usage. | [details](skills/deepseek/references/versions/deepseek-r1.md) |

### gemini

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Gemini 4 Argon | `gemini-4-argon` | frontier, reasoning, coding, agentic | stable | New release; public usage metric unknown | [details](skills/gemini/references/versions/gemini-4-argon.md) |
| Gemini 3.8 Flash | `gemini-3.8-flash` | general, coding, agentic, multimodal | stable | Provider labels stable; comparable usage/adoption metric unknown | [details](skills/gemini/references/versions/gemini-3-8-flash.md) |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | low-cost, high-volume, agentic | stable | Unknown | [details](skills/gemini/references/versions/gemini-3-5-flash-lite.md) |
| Gemini 3.8 Live | `gemini-3.8-live` | audio, real-time, voice-agent | stable | Unknown | [details](skills/gemini/references/versions/gemini-3-8-live.md) |
| Gemini 3.5 Transcribe | `gemini-3.5-transcribe` | audio, speech-to-text | stable | Unknown | [details](skills/gemini/references/versions/gemini-3-5-transcribe.md) |

### gemma

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Gemma 3 12B IT | `google/gemma-3-12b-it` | open-weight, general, multimodal, local | available; usage terms apply | Official Gemma 3 family has broad model-card and deployment ecosystem; exact count for this variant unknown | [details](skills/gemma/references/versions/gemma-3-12b-it.md) |
| Gemma 4 31B IT | `google/gemma-4-31B-it` | open-weight, general, reasoning, multimodal, coding | available; latest Gemma generation | Official Google HF collection showed 9.18M downloads and 4.13K likes on the 31B instruct card ; HF download window is platform-defined, not… | [details](skills/gemma/references/versions/gemma-4-31b-it.md) |
| Gemma 3 27B IT | `google/gemma-3-27b-it` | open-weight, general, multimodal | available; usage terms apply | Official Gemma 3 card and Google distribution ecosystem inspected; variant-specific usage/download count unknown. Third-party quantization… | [details](skills/gemma/references/versions/gemma-3-27b-it.md) |
| Gemma 3n E4B IT | `google/gemma-3n-E4B-it` | open-weight, multimodal, on-device | available; usage terms apply | HF: 100 Spaces using the model ; a platform integration proxy, not usage volume | [details](skills/gemma/references/versions/gemma-3n-e4b-it.md) |

### glm

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| GLM-5.3 | `glm-5.3` | code | Current flagship, available from Z.ai API and via open-weight distribution. | Z.ai Coding Plan and API availability confirmed; no provider usage count or model downloads found in inspected official sources. | [details](skills/glm/references/versions/glm-5-3.md) |
| GLM-5.3-Flash | `glm-5.3-flash` | open-weight | Current open-source multimodal Flash model; hosted FlashX is a speed tier, not a separate base model. | OpenRouter ranked GLM 5.3 Flash third in the displayed tokens-processed table with 12.9T tokens and +26%; usage data was through 2026-10-13. | [details](skills/glm/references/versions/glm-5-3-flash.md) |

### gpt

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| GPT-6 Astra | `gpt-6-astra` | frontier | current | Unknown | [details](skills/gpt/references/versions/gpt-6-astra.md) |
| GPT-6.1 Sol | `gpt-6.1-sol` | frontier | current | Unknown | [details](skills/gpt/references/versions/gpt-6-1-sol.md) |
| GPT-6 Luna | `gpt-6-luna` | general | current | OpenRouter ranked GPT-6 Luna 7th in the displayed tokens-processed table with 7.1T tokens and +10%; usage data was through 2026-10-13. | [details](skills/gpt/references/versions/gpt-6-luna.md) |
| GPT-5.6 Sol | `gpt-5.6-sol` | frontier | current/api GA | Unknown | [details](skills/gpt/references/versions/gpt-5-6-sol.md) |
| GPT-5.6 Terra | `gpt-5.6-terra` | general | current/api GA | Unknown | [details](skills/gpt/references/versions/gpt-5-6-terra.md) |
| GPT-5.6 Luna | `gpt-5.6-luna` | general | current/api GA | OpenRouter ranked GPT-5.6 Luna 7th in the 30-day tokens-processed table with 25T tokens and -45%; newest bucket shown was 2026-10-13. | [details](skills/gpt/references/versions/gpt-5-6-luna.md) |
| GPT-5.5 | `gpt-5.5` | frontier | current/API | Unknown | [details](skills/gpt/references/versions/gpt-5-5.md) |
| GPT-5.5 Pro | `gpt-5.5-pro` | reasoning | current/API | Unknown | [details](skills/gpt/references/versions/gpt-5-5-pro.md) |
| GPT-5.4 | `gpt-5.4` | frontier | current/API | Unknown | [details](skills/gpt/references/versions/gpt-5-4.md) |
| GPT-5.4 Pro | `gpt-5.4-pro` | reasoning | current/API | Unknown | [details](skills/gpt/references/versions/gpt-5-4-pro.md) |

### gpt-oss

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| gpt-oss-120b | `gpt-oss-120b` | open-weight | released; weights available | Unknown | [details](skills/gpt-oss/references/versions/gpt-oss-120b.md) |
| gpt-oss-20b | `gpt-oss-20b` | open-weight | released; weights available | Unknown | [details](skills/gpt-oss/references/versions/gpt-oss-20b.md) |

### granite

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Granite 4.0 H Small | `ibm-granite/granite-4.0-h-small` | open-weight, general, enterprise, long-context | available | Official HF card documents vLLM, SGLang and Docker Model Runner; popularity counters not captured | [details](skills/granite/references/versions/granite-4-0-h-small.md) |

### grok

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Grok 4.7 | `grok-4.7` | frontier | active | Unknown | [details](skills/grok/references/versions/grok-4-7.md) |
| Grok Code Fast 1 (API alias for Grok Build 0.1) | `grok-build-0.1` | code | active | Unknown | [details](skills/grok/references/versions/grok-build-0-1.md) |

### jev-system-one

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Jev 1.13 | `jev-1.13.0` | decision | Current stable release; `jev-latest` points to 1.13.0; 1.14.0 is preview as of 2026-10-16. | Unknown | [details](skills/jev-system-one/references/versions/jev-1-13-0.md) |

### kimi

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Kimi K3 | `kimi-k3` | frontier | Current flagship; hosted API and full model weights are available. | Official Hugging Face page showed 11.7k likes and 187 community discussions ; these are platform engagement proxies, not downloads or… | [details](skills/kimi/references/versions/kimi-k3.md) |
| Kimi K2.7 Code | `kimi-k2.7-code` | code | Current specialized coding API model; high-speed variant is a serving tier and not counted as a separate identity. | Official model catalog confirms current support; no measured usage signal found. | [details](skills/kimi/references/versions/kimi-k2-7-code.md) |

### llama

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Llama 4 Scout Instruct | `meta-llama/Llama-4-Scout-17B-16E-Instruct` | open-weight, general, multimodal, long-context | available; gated download | HF: 5.0M downloads and 700 likes for the Scout family card ; family-level count and platform-specific proxy, not unique production users | [details](skills/llama/references/versions/llama-4-scout-17b-16e-instruct.md) |
| Llama 4 Maverick Instruct | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` | open-weight, general, multimodal | available; gated download | Official HF repository card lists active community and usage integrations; exact current downloads not captured in inspected source, so count… | [details](skills/llama/references/versions/llama-4-maverick-17b-128e-instruct.md) |
| Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct` | open-weight, general | available; gated download; prior-generation, still widely used | HF: 266K downloads and 3.14K likes for repository in the official Meta collection snapshot | [details](skills/llama/references/versions/llama-3-3-70b-instruct.md) |

### minimax

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| MiniMax-M3 | `MiniMax-M3` | frontier | Current M-series flagship; hosted API and downloadable open weights are available. | Official GitHub repository showed 491 stars and 59 forks ; repository-interest proxy only, not model downloads or production usage. | [details](skills/minimax/references/versions/minimax-m3.md) |

### mistral

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Mistral Large 3 675B Instruct 2512 | `mistralai/Mistral-Large-3-675B-Instruct-2512` | open-weight, general, multimodal, frontier | available; current open-weight release | Official HF repository displayed 20.1K provider followers and 14 discussion items; direct downloads/production use unknown | [details](skills/mistral/references/versions/mistral-large-3-675b-instruct-2512.md) |
| Ministral 3 14B Instruct 2512 | `mistralai/Ministral-3-14B-Instruct-2512` | open-weight, general, multimodal, edge-to-cloud | available | Official HF card shows an active community and distribution; exact download count was not exposed in inspected result | [details](skills/mistral/references/versions/ministral-3-14b-instruct-2512.md) |
| Mistral Small 4 119B A6B | `mistralai/Mistral-Small-4-119B-2603` | open-weight, general, reasoning, code, multimodal | available; current open-weight hybrid model | Official Mistral HF collection showed 74.9K downloads and 452 likes on the main checkpoint listing ; download window is HF-defined and not… | [details](skills/mistral/references/versions/mistral-small-4-119b-2603.md) |

### nemotron

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Nemotron 3 Nano 30B A3B NVFP4 | `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4` | open-weight, reasoning, agentic, small-MoE | available | HF: 190 likes and 12 community discussions ; modest but directly measurable platform signal | [details](skills/nemotron/references/versions/nvidia-nemotron-3-nano-30b-a3b-nvfp4.md) |

### perplexity-decider

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Perplexity Decider 27B | `pplx-decider-v1.1-27b` | decision | active | OpenRouter listed Decider V1.1 27B among new/trending models with 184B tokens processed; newest bucket shown was 2026-10-13. This is an early… | [details](skills/perplexity-decider/references/versions/pplx-decider-v1-1-27b.md) |

### phi

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Phi-4 | `microsoft/phi-4` | open-weight, general, reasoning, small | available | HF: 426,836 downloads in the last month  | [details](skills/phi/references/versions/phi-4.md) |
| Phi-4 Multimodal Instruct | `microsoft/Phi-4-multimodal-instruct` | open-weight, multimodal, small | available | Official HF repository card showed 98 community Spaces ; integrations proxy only | [details](skills/phi/references/versions/phi-4-multimodal-instruct.md) |

### qwen

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Qwen3.8-Max | `qwen3.8-max` | frontier | Current Alibaba Cloud Model Studio hosted model. | Official API and model catalog list the exact ID; no usage telemetry found. Availability is not a popularity metric. | [details](skills/qwen/references/versions/qwen3-8-max.md) |
| Qwen3.8-Flash | `qwen3.8-flash` | general | Current Alibaba Cloud Model Studio hosted model. | Official API availability confirmed; no usage count or comparative adoption statistic found. | [details](skills/qwen/references/versions/qwen3-8-flash.md) |
| Qwen3.8-27B | `Qwen/Qwen3.8-27B` | open-weight | Current open-weight release with official Hugging Face/ModelScope distribution and Model Studio API availability. | HF: 17.8k likes and 209 community discussions ; these are platform engagement proxies, not downloads or production usage. | [details](skills/qwen/references/versions/qwen3-8-27b.md) |

### seed

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| Doubao Seed 2.1 Pro | `doubao-seed-2-1-pro-260628` | general | Current hosted model in the Seed2.1 family; available through Volcano Engine API and consumer/developer products. | Launch/distribution: Doubao and TRAE with API availability; distribution signal only, no usage counts published on inspected pages. | [details](skills/seed/references/versions/doubao-seed-2-1-pro-260628.md) |
| Dola Seed 2.1 Turbo (Seed2.1 Turbo) | `dola-seed-2-1-turbo-260628` | general | Current hosted Turbo tier in the Seed2.1 family. | Launch/distribution: the Seed2.1 released model family; usage/download counts not found. | [details](skills/seed/references/versions/dola-seed-2-1-turbo-260628.md) |
| Seed-OSS-36B-Instruct | `ByteDance-Seed/Seed-OSS-36B-Instruct` | open-weight | Official weights and model card remain downloadable; current hosted API status not established. | Official Hugging Face page showed 506 likes and 34 community discussions ; engagement proxy, not download or production-usage count. | [details](skills/seed/references/versions/seed-oss-36b-instruct.md) |

### tabicl

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| TabICLv2 | `TabICLv2` | predictive-tabular | current release in official repository; v2.2.0 is listed as latest release | Repo: 1.4k GitHub stars; official Hugging Face model card states downloads are not tracked | [details](skills/tabicl/references/versions/tabiclv2.md) |

### tabpfn

| Model | Catalog ID | Role | Status | Adoption evidence | Family reference |
|---|---|---|---|---|---|
| TabPFN-3.5 | `TabPFN-3.5` | predictive-tabular | current model line; official TabPFN repo says TabPFN-3.5 is used by default | Proxy: Prior Labs official homepage displayed 8K GitHub stars and 4M downloads. | [details](skills/tabpfn/references/versions/tabpfn-3-5.md) |

## Selection method and limits

Selection is use-first where comparable public evidence exists, then uses dated distribution/interest proxies, and finally applies current-availability and distinct-capability coverage where telemetry is unknown. The snapshot has 5 observed platform-usage entries, 19 proxy-supported entries, and 36 entries with unknown comparable public use; no global rank is claimed. Every row records its evidence class and selection rationale. Unknown-use entries were retained only for current distinct provider tiers/capabilities or explicit specialist coverage, not because their popularity was demonstrated. No single numeric score combines provider usage, router tokens, repository downloads, stars, likes, or integration counts because these have different scopes and denominators.

For each candidate, researchers inspected official model documentation/cards and recorded canonical ID, release/status, capabilities, context/output limits, pricing, availability, license, limitations, dated source URLs and retrieval date. Where a first-party or transparent platform measure was available, the record includes its unit, window and scope. Open-weight downloads and repository counters are distribution or interest proxies, not active users. Unknown means no comparable model-level signal was found in the inspected sources; it does not mean zero use.

OpenRouter publishes public token-volume rankings for traffic routed through its service only. Its tables exclude private traffic and direct-provider calls; token volume is not users, spend, task preference, quality or accuracy. Hugging Face downloads are repository distribution requests, can include automated/repeated fetches and are not unique active deployments. These measurements are useful within their own scopes only.

The 60 entries are deduplicated across aliases, API routes/profiles, quantizations and mirrors of the same weights. Distinct model releases/tiers remain separate catalog rows when the underlying identity materially differs. Decision-oriented models are not treated as general chat models: Jev returns typed semantic judgments; Perplexity Decider returns structured probabilities; TabPFN and TabICL are predictive tabular models. They answer different problem shapes.

Limitations: public model-level usage is unavailable for many vendors; API model lists and rates change quickly; availability can vary by region/account/contract; some model references contain carefully labeled unknowns; and this curation does not cover every active model. Recheck the cited provider source before selecting an ID or budget for production.

### Method sources

- [OpenRouter model rankings and scope](https://openrouter.ai/rankings?benchmark=intelligence)
- [OpenRouter daily token totals dataset API](https://openrouter.ai/docs/api/api-reference/datasets/daily-token-totals-for-top-50-models)
- [Hugging Face model download statistics](https://huggingface.co/docs/hub/models-download-stats)
- [Hugging Face publisher analytics](https://huggingface.co/docs/hub/publisher-analytics)
- Provider-specific official sources are recorded in each family reference and the machine-readable `catalog.json`.

Fetched: 2026-10-16 UTC.
