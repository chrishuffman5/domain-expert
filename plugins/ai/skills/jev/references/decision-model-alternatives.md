# Decision-model alternatives: wire compatibility, porting and local serving

Read this when you need to know which APIs accept jev-shaped requests, how much code changes when porting jev code to or from Gemini/OpenAI Decisions or a System One-compatible host, or how to run a local `/v1/systemone` server (Kev, Ollama ≥ 0.35). Snapshot as of **2026-11-13**. Every benchmark and calibration figure below is **self-reported by the vendor or author** unless labelled otherwise.

**Selection guidance lives elsewhere.** Whether Jev or another decision or chat model fits a workload, and source-traced model comparisons, belong to `ai-models-specialist` when the `ai-models` plugin is installed. This file is the fallback fact base for that question, not a recommendation engine. For general LLM choice, use `model-selection`.

Naming note: TypeSafe deliberately calls jev a "System One model", not a "decision model" ("Jev makes judgments, code makes decisions"), while conceding "decision models" is the common category name (https://typesafe.ai/blog/dont-call-it-a-decision-model).

## Facts that constrain any comparison

> Source: https://artificialanalysis.ai/articles/decision-index-v2 (press/third-party)
> Source: https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index (press/third-party)

- **No independent head-to-head numbers for jev vs `gemini-decision-1` vs `gpt-6-luna` (Decisions) are sourceable.** Artificial Analysis Decision Index v2 (2026-11-08) gives no readable index score for Jev, Gemini Decision 1, Microsoft-Decision-1, d1-ultra or Perplexity; its leaderboard values sit in an interactive chart. In the article text, Jev 1.14 appears only with a latency of 92 ms per task. Its top readable entries are language models (Claude Haiku 5.5 (Max) 77, GPT-6 Luna (Max) 76) at far higher cost per task.
- **Anthropic decision model: NOT FOUND** as of 2026-11-13, after two search passes over platform.claude.com release notes, anthropic.com/news, claude.com/blog and the structured-outputs docs. The nearest capability is Claude structured outputs, which is **not** a decision model: schema-constrained JSON, no probabilities or logprobs, and any "confidence" field is model-generated text you define in the schema.
- Benchmark on your own labelled data before porting production traffic. The AI SDK "does not promise calibration across providers."

## Wire compatibility at a glance

> Source: https://ai-sdk.dev/docs/ai-sdk-core/decisions

| Shape | Who | Shared-context field | Questions | Yes/no primitive |
|---|---|---|---|---|
| **System One** (jev's) | jev, Microsoft-Decision-1, Liquid d1-ultra, Cloudflare Clef, Baseten, Perplexity, Parallel, Kev and most local models | `state` | named map | `noul` |
| Gemini Decisions | Google | `input` | named map (1–1,000) | `noul` (criteria `true_description` / `false_description`) |
| OpenAI Decisions | OpenAI; also Vercel `/v1/decisions`, LiteLLM, Portkey, agentgateway | `input` | **array** with `name` | `predicate` |

- Changing only `baseURL` and `model` on a TypeSafe SDK client works for servers that implement `POST /v1/systemone` (Cloudflare says Clef "follows the System One API"; Kev, Ollaya, Strands Decider and others say the TypeSafe SDK works unchanged).
- AI SDK `experimental_decide` abstracts all three shapes (`boolean`, `choice`, `score`, `box`): `typeSafeAi.decisionModel('jev-latest')`, `google.decisionModel('gemini-decision-1')` and `openai.decisionModel('gpt-6-luna')` are native; `anthropic.decisionModel(...)` is "adapted from structured language-model output" with prompted P(true) estimates and no choice/score distributions.
- LiteLLM serves any configured decision model on both `/v1/systemone` and `/v1/decisions` (https://docs.litellm.ai/docs/decisions.md).

## Hosted products

> Source: https://aistudio.google.com/docs/decisions-api
> Source: https://developers.openai.com/api/docs/guides/decisions.md
> Source: https://docs.perplexity.ai/docs/decisions/quickstart
> Source: https://developers.cloudflare.com/workers-ai/models/clef/

| Product | Model id | Status (as sourced) | $ / 1M input | Max questions | Input | Tier of sourcing |
|---|---|---|---|---|---|---|
| **jev** (reference) | `jev-1.14.0` | early access; GA label not used | $0.042 | no documented cap (context-bound) | text; PNG/JPEG behind a "dreamer" header | official |
| Google Gemini Decisions API | `gemini-decision-1` | announced 2026-11-11; no official status label (Vercel AI SDK says "EAP") | $0.10; free tier | 1,000 | text, image, audio, video, PDF; 262,144 ctx | official |
| OpenAI Decisions API | `gpt-6-luna` | GA 2026-10-22 (changelog only) | $0.10; caching | 400 | text, images, `input_json`, tool outputs | official |
| Microsoft-Decision-1 | deployment of `Microsoft-Decision-1` | public preview (2026-10-09) | $0.042 (US/EU Datazone) | not stated | text | vendor blog |
| Perplexity Decisions | `pplx-decider-v1.3`, `pplx-decider-flash-v1.3` | not stated | $0.02 / $0.01 | 100 (grounded), 128 (`locate`) | text, images; <256K | official docs |
| Liquid AI | `d1-ultra` | 2026-10-15 | $0.042 | not stated | text, images | vendor blog |
| Cloudflare Clef | `@cf/cloudflare/clef`, `@cf/cloudflare/clef-flash` | available 2026-10-01 | $0.24 (clef) | 64 | text, up to 4 images; 65,536 ctx | official |
| Baseten | `decision-models/baseten-elephant-9b-latest`, `...-mammoth-27b-latest` | available 2026-10-21 | not stated | not stated | not stated | vendor |
| Parallel Decisions | not stated | not stated (self-reported launch 2026-10-25) | self-reported $1 per 1,000 requests | 100 | text (web-grounded) | vendor docs; pricing competitor-authored |

### Google: Gemini Decisions API

> Source: https://aistudio.google.com/docs/decisions-api
> Source: https://aistudio.google.com/docs/rate-limits
> Source: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/ (vendor blog)

- `POST https://generativelanguage.googleapis.com/v1beta/decisions`, header `x-goog-api-key`; `google-genai` ≥ 3.2 (`client.decisions.create`). Gemini API and AI Studio only; Google Cloud "coming soon".
- Choice 2–255 options; Score 2–255 levels (2–10 recommended). Noul is clamped to 0.01–0.99 and **does** return `confidence` (top outcome's probability, or max(noul, 1−noul)), unlike jev.
- Choice keys are sorted in UTF-8 byte order and exact ties go to the alphabetically first key; add a catch-all option.
- Rate limits: Free 200 RPM / 50,000 TPM / 10,000 RPD up to Tier 3 15,000 RPM / 10M TPM. No caching, Batch, Flex or Priority.
- Vendor claims (no per-benchmark scores): lowest calibration error in its suite; 150–250 ms end-to-end, nearly flat from 1 to 100 questions up to 16K context.

```json
{
  "model": "gemini-decision-1",
  "input": "The blue mug I ordered on Monday arrived cracked on Wednesday.",
  "questions": {"is_damaged": {"type": "noul", "instructions": "Did the item arrive damaged?"}}
}
```

### OpenAI: Decisions API

> Source: https://developers.openai.com/api/docs/guides/decisions.md
> Source: https://developers.openai.com/api/reference/resources/decisions/methods/create
> Source: https://developers.openai.com/api/docs/changelog

- `POST /v1/decisions`, model `gpt-6-luna` only. Timeline: public beta 2026-10-06, GA 2026-10-22 (400 questions, shared-input caching, images in instructions, `input_json`).
- Types `predicate` (returns `probability`), `choice` (2–255, `probabilities` as `[{value, probability}]`), `score` (2–10 levels). A per-question `refusal` answer can coexist with answered questions.
- `input` may be a string or messages including tool calls and tool outputs. Caching: `prompt_cache_key`, `ttl` `30m`; reusable prefix ≥ 1,024 tokens. Cache writes are billed at standard rates (the beta post said otherwise; the GA guide wins).
- No rate limits or error codes in the guide. Integrations: LangChain `OpenAIDecisions` (`@langchain/openai` ≥ 1.8.0, beta), Pydantic AI `OpenAIDecisionsModel`, AI SDK `openai.decisionModel('gpt-6-luna')`.

### Others (competitor or press-tier sourcing unless noted)

> Source: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742 (vendor blog)
> Source: https://www.liquid.ai/blog/d1-ultra (vendor blog)
> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/
> Source: https://www.baseten.co/resources/changelog/elephant-1-and-mammoth-1-available-on-baseten/ (vendor)
> Source: https://docs.parallel.ai/decisions/decisions-quickstart (vendor docs)
> Source: https://parallel.ai/articles/jev-alternatives.md (competitor-authored)

- **Microsoft-Decision-1**: built on Qwen3.5-9B; `POST {AZURE_ENDPOINT}/providers/microsoft/v1/systemone` with `state` + `questions`. The sample authenticates with an Entra token while the prose mentions `FOUNDRY_API_KEY`; confirm before use. Microsoft does not claim full System One compatibility.
- **Perplexity**: `POST https://api.perplexity.ai/v1/decisions` (Bearer only). `state` + `questions` map with `noul`, `choice`, `score` and `locate` (text spans, v1.3); optional `mode: "web_grounding"` ($1 per 1,000 searches). 10 req/s per org.
- **Liquid d1-ultra**: `https://api.liquid.ai/decisions/v1/systemone`. Claims it "outperforms Jev 1.14 across all tasks" and better calibration; the figures are images, so unverifiable. Each question is billed as a separate prompt including its images.
- **Cloudflare Clef**: 27B (`clef`) and 9B (`clef-flash`); "switch from Jev by changing endpoint and model"; open weights under Apache 2.0 on Hugging Face per the changelog. Called via the `@cf/` path form.
- **Baseten**: `https://inference.baseten.co/v1/systemone`. Prices and licence appear only on Parallel's competitor page.
- **Parallel**: `POST https://api.parallel.ai/v1/decisions`, `x-api-key`; web-grounded with citations for the whole call; `refusal` answers are HTTP successes. Its article ranks itself first.
- Named only on a competitor page (unverified): Upstage Solar Decide, Inception Mercury Decide, Fastino GLiDE, Nace.AI Drex, SubQ Snap.

## Local and open-weight alternatives

> Source: https://github.com/jaredpalmer/kev
> Source: https://github.com/ollama/ollama/releases/tag/v0.35.0
> Source: https://github.com/strands-labs/strands-decider
> Source: https://github.com/ollaya-dev/ollaya

| Name | Id / install | Base, size | Licence | System One API | Maturity (as fetched) |
|---|---|---|---|---|---|
| **Kev** (Jared Palmer) | `jaredpalmer/kev-{0.8b,4b,9b,27b}` | Qwen3.5 0.8/4/9B LoRA; Qwen3.8-27B full fine-tune | Apache-2.0 | yes, `/v1/systemone`, `kev-latest` | 10.0k stars; Kev 1.0 2026-09-24 |
| **Ollama ≥ 0.35** | `ollama pull nimble`, `ollama pull tev1:4b` | runtime | per model | yes, `/v1/systemone` | official release notes |
| Nimble (Bespoke Labs) | `bespokelabs/Bespoke-Nimble-9B`; hosted `nimble-v4.1-max` | Qwen3.5-9B LoRA; v4-max 27B | Apache-2.0 (v1 card); later versions unclear | via Ollama | 93.5K Ollama pulls |
| Tev1 (Together AI) | `tev1:4b`, `tev1:0.8b` | Qwen3.5 4B / 0.8B | not stated | via Ollama | Ollama library |
| Strands Decider 2B (AWS Strands Labs) | `StrandsAgents/strands-decider-2B-qwen3.5-v1-2610` | Qwen3.5-2B-Base, 1.9B | Apache-2.0 | yes | ~1.2k stars; experiment, not a managed AWS service |
| Laya (Convai) | `convaiinnovations/laya` | ModernBERT-large 421M | Apache-2.0 | yes | ~5.96k likes; base is **not** zero-shot |
| Ollaya | `ollaya-dev/ollaya` | runtime, 29 families | Apache-2.0 (models vary) | yes, "wire-identical" | 1.5k stars, community |
| Bosun v3.1 | `Hanno-Labs/bosun-v3.1-1.7b` | Qwen3-1.7B LoRA | Apache-2.0 | no HTTP shape stated | 365 downloads/mo |
| jevos | `feder-cr/jev` | not stated | MIT | yes | 967 stars; CPU ~1 GB |
| jev-style | `lawrence3699/jev-style` | Qwen3.5 0.8B / 2B | Apache-2.0 | yes | 134 stars |
| open-alternative-jev | `pip install open-alternative-jev` | any open LLM (option-letter logits) | Apache-2.0 | library, no server | 80 stars |
| System One Adapter (TypeSafe) | `pip install 'system-one-adapter[openai]'` | your LLM API | MIT | drop-in `system_one` | 410 stars; last updated 2026-09-22 |

Also seen, all community and less mature: WaterSheep, WebJev-35B-A3B, NeoHorse-Jev-4B, usejev (Bun/ONNX server for Laya), Local-Jev (claims conflict; unverified), and awesome-list entries vev (weights CC BY-NC 4.0), OneJev, RSI-Jev, jevmlx, Open Medical Jev, openjev-sglang (archived), PlayJev (games only).

**Databricks OpenJev** (`system.ai.openjev-qwen35-4b`) is an open Qwen3.5-based model *hosted* by Databricks behind the System One API (`/ai-gateway/typesafe/v1/systemone`). Its maker, licence and price are not stated officially. Two unrelated community repos use the same name (`shenjunhao/OpenJev-4B`, `AlexWortega/openjev`).

### How to run them (verbatim commands)

> Source: https://github.com/jaredpalmer/kev
> Source: https://huggingface.co/jaredpalmer/kev-4b
> Source: https://huggingface.co/espetro/kev-0.8b-gguf (community repack)
> Source: https://ollama.com/library/nimble
> Source: https://ollama.com/library/tev1
> Source: https://github.com/strands-labs/strands-decider
> Source: https://huggingface.co/convaiinnovations/laya
> Source: https://github.com/ollaya-dev/ollaya

Kev (Python 3.12/3.13 + uv; `--device cpu|cuda|mps`):
```bash
git clone https://github.com/jaredpalmer/kev.git && cd kev
uv sync --extra serve
uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b --port 8009
# pinned: uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b@v1.0 --port 8008
```
Kev is **not** in the Ollama library. A third-party GGUF repack of the 0.8B exists (`ollama run hf.co/espetro/kev-0.8b-gguf:F16`, `llama-server -hf espetro/kev-0.8b-gguf:Q8_0`), but only its llama.cpp fork is documented to serve `/v1/systemone`; stock Ollama exposing the decision endpoint for it is unconfirmed. Ollaya ships `kev` tags.

Ollama (≥ 0.35.0; later releases added d3, Liquid d1 2B and AutoTrust decision models):
```bash
ollama pull nimble
curl http://localhost:11434/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{"model": "nimble", "state": "Hello World", "questions": {"says_hello": {"type": "noul", "instructions": "Does the state text contain a greeting?", "criteria": {"true": "The state text contains a greeting.", "false": "The state text does not contain a greeting."}}}}'
```
```bash
ollama pull tev1:4b
ollama pull tev1:0.8b
```

Strands Decider:
```bash
pip install strands-decider
strands-decider ask StrandsAgents/strands-decider-2B-qwen3.5-v1-2610 \
  --state "Help! My payouts have been failing for 3 days! " \
  --choice "Which team should handle this?=billing,sales,retail"
strands-decider serve StrandsAgents/strands-decider-2B-qwen3.5-v1-2610 --port 8000
```

Laya: `pip install "laya[serve]"` then `LAYA_DEVICE=cuda LAYA_PRELOAD=1 laya-serve`.

Ollaya: `curl -fsSL https://ollaya.dev/install.sh | sh` (Windows: `irm https://ollaya.dev/install.ps1 | iex`; Docker `ghcr.io/ollaya-dev/ollaya:cuda` on port 11435). Point the TypeSafe SDK at it with `TYPESAFE_BASE_URL=http://localhost:11435` and any non-empty `TYPESAFE_API_KEY`.

To point the AI SDK at any local System One server: `TYPESAFE_AI_BASE_URL=http://127.0.0.1:<port>/v1` (the server must implement `POST /systemone`) (https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai).

### Hardware and self-reported results

> Source: https://github.com/jaredpalmer/kev
> Source: https://raw.githubusercontent.com/bespokelabsai/nimble/main/README.md
> Source: https://github.com/strands-labs/strands-decider
> Source: https://huggingface.co/convaiinnovations/laya

- **Kev**: 0.8B runs on any 4 GB GPU or Apple Silicon; 4B/9B want an L40S/H100 or a 32 GB Mac; 27B needs ~66 GB serving memory (80 GB GPU). One global temperature per checkpoint (2.35 / 2.41 / 2.19 / 1.32), `KEV_TEMPERATURE=1` for raw probabilities. Over 65,536 tokens returns 422. English only. Author's own comparison (dev sets, "not a controlled comparison"): held-out index Kev-27B 52.3 and Kev-4B 38.0 vs Jev 54.0; MMLU-Pro Kev-27B 0.675 vs Jev 0.840.
- **Nimble**: reference-label agreement 90.12% vs Jev 1.13.0 93.21% (324 examples). Calibration caveat from its own README: the latest checkpoint uses T=1.0 with no separate fit, and ECE on 64 rating questions rose 0.105 → 0.177 under the earlier fitted temperature.
- **Strands Decider 2B**: 115 ms median per question on an RTX 3090; JevBench public v1 accuracy 0.779, ECE 0.072; claims 0.9+ confidence is right about 95% of the time on unseen short classification.
- **Laya**: post-temperature ECE 0.081 vs Jev's published 0.246; beats Jev 1.13.0 on some sets, loses badly on Banking77 (0.425 vs 0.870). The 0.766 headline is a fine-tuned checkpoint, not zero-shot.
- Pattern across the field: authors' own tables usually show hosted jev ahead on general accuracy (jev-style "well ahead", jevos "higher on most tasks", Kev trails at every size), with local models winning on latency, cost and offline use. Bosun's lead over Jev comes with the caveat that it was trained on the benchmark's task families.

## Not decision models: structured-output libraries

> Source: https://developers.openai.com/api/docs/guides/structured-outputs
> Source: https://aistudio.google.com/docs/structured-output
> Source: https://platform.claude.com/docs/en/build-with-claude/structured-outputs

| Tool | Mechanism | Difference from jev |
|---|---|---|
| OpenAI Structured Outputs | schema-constrained generation | guarantees shape, not calibrated probabilities |
| Gemini structured output | JSON Schema with `enum` | enum labels, no distribution; Google's own docs redirect calibrated yes/no, choice and rubric needs to `gemini-decision-1` |
| Claude structured outputs | `output_config.format` JSON Schema, constrained decoding | no logprobs; "confidence" is a field the model writes |
| BAML | DSL for typed output from any LLM | confidence comes from the LLM; streams typed partials |
| Instructor | Pydantic validation plus retries | extraction tool, not a calibrated classifier |
| Outlines | token-level constraints for self-hosted models | you build any calibration yourself |

The BAML, Instructor and Outlines rows are carried from the 2026-09-23 corpus and were not re-fetched. No fetched source positions Outlines-style constrained decoding as a jev alternative; `open-alternative-jev` (option-letter logits from an open LLM plus temperature scaling) is the closest sourced instance.

Decision-model APIs return a bounded, typed answer with a probability; generative models are needed when the output must be text, code or an explanation. For a recommendation between them, use `ai-models-specialist` when installed.

## Sources
- https://typesafe.ai/blog/dont-call-it-a-decision-model (vendor blog)
- https://aistudio.google.com/docs/decisions-api
- https://aistudio.google.com/docs/models/gemini-decision-1
- https://aistudio.google.com/docs/rate-limits
- https://aistudio.google.com/docs/pricing
- https://aistudio.google.com/docs/structured-output
- https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/ (vendor blog)
- https://developers.openai.com/api/docs/guides/decisions.md
- https://developers.openai.com/api/reference/resources/decisions/methods/create
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/structured-outputs
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- https://www.anthropic.com/news
- https://www.claude.com/blog (partial)
- https://ai-sdk.dev/docs/ai-sdk-core/decisions
- https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
- https://docs.litellm.ai/docs/decisions.md
- https://docs.perplexity.ai/docs/decisions/quickstart
- https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742 (vendor blog)
- https://www.liquid.ai/blog/d1-ultra (vendor blog)
- https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/
- https://developers.cloudflare.com/workers-ai/models/clef/
- https://www.baseten.co/resources/changelog/elephant-1-and-mammoth-1-available-on-baseten/ (vendor)
- https://docs.parallel.ai/decisions/decisions-quickstart (vendor)
- https://parallel.ai/articles/jev-alternatives.md (competitor-authored)
- https://artificialanalysis.ai/articles/decision-index-v2 (press/third-party)
- https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index (press/third-party)
- https://github.com/jaredpalmer/kev
- https://huggingface.co/jaredpalmer/kev-4b
- https://huggingface.co/espetro/kev-0.8b-gguf (community)
- https://github.com/ollama/ollama/releases/tag/v0.35.0
- https://github.com/ollama/ollama/releases
- https://ollama.com/library/nimble
- https://ollama.com/library/tev1
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/README.md
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B
- https://github.com/strands-labs/strands-decider
- https://docs.databricks.com/gcp/en/machine-learning/model-serving/query-systemone-models
- https://huggingface.co/convaiinnovations/laya
- https://github.com/ollaya-dev/ollaya (community)
- https://huggingface.co/Hanno-Labs/bosun-v3.1-1.7b
- https://github.com/feder-cr/jev
- https://github.com/lawrence3699/jev-style
- https://github.com/ikermoel/open-alternative-jev
- https://github.com/typesafe-ai/system-one-adapter-python
- https://github.com/Anil-matcha/awesome-jev-by-typesafe (community)
- https://docs.boundaryml.com/home (2026-09-23)
- https://python.useinstructor.com/ (2026-09-23)
- https://dottxt-ai.github.io/outlines/latest/ (2026-09-23)

Fetched: 2026-11-13
