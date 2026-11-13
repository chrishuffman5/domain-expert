# OpenAI: model catalog, pricing, and selection framework (as of 2026-11-13)

Read when the question names OpenAI, GPT, Codex, o-series, Sora, gpt-oss, the Decisions API, or asks for an OpenAI model ID / price / limit. Re-verify against the source URLs before quoting. Rows and sections still carrying 2026-08-05 data say so.

Sourcing note: `platform.openai.com/docs/models` and `platform.openai.com/docs/pricing` issue a permanent 301 to `developers.openai.com/api/docs/…`. The URLs cited here are the redirect targets, OpenAI's current official API documentation host.

## Current flagship family: GPT-6 / GPT-6.1

> Source: https://developers.openai.com/api/docs/models/gpt-6-astra, …/gpt-6.1-sol, …/gpt-6-sol, …/gpt-6.1-terra, …/gpt-6-luna, and https://developers.openai.com/api/docs/changelog (fetched 2026-11-13)

All five share a 1,050,000-token context, 922,000 max input, 128,000 max output, and text+image in / text out. They differ in price, cutoff and reasoning-effort levels.

| Model | Model ID | Positioning (vendor wording) | Released | Cutoff | Effort levels | Input / cached / output $/MTok |
|---|---|---|---|---|---|---|
| GPT-6 Astra | `gpt-6-astra` | "Our most capable model for the most demanding work" | **Conflict:** 2026-09-29 (OpenAI changelog) vs 2026-09-03 (Azure version); OpenAI's model page states no date | Apr 30, 2026 | low → max (no `none`) | $10 / $1 / $50 (cache write $12.50) |
| GPT-6.1 Sol | `gpt-6.1-sol` | "Near-Astra performance for complex work at a lower cost" | 2026-09-29 | Apr 30, 2026 | low → max (no `none`), default medium | $2 / $0.10 / $10 (cache write $2.50) |
| GPT-6 Sol | `gpt-6-sol` | "Built for complex coding and agentic workflows"; page points to 6.1 Sol as the newer Sol | 2026-09-22 | Apr 20, 2026 | none → max, default medium | $2 / $0.20 / $10 |
| GPT-6.1 Terra | `gpt-6.1-terra` | "Fast, efficient model for visual reasoning, precise computer use, and clear, natural writing" | 2026-10-26 | Jun 1, 2026 | none → max, default medium | $1 / $0.05 / $5 (cache write $1.25 at 30 min, $2.50 at 12 h) |
| GPT-6 Luna | `gpt-6-luna` | "Our most efficient model for focused, high-volume tasks" | 2026-09-22 | May 18, 2026 | none → max, default medium | $0.10 / $0.01 / $0.50 (cache write $0.125) |

Effort levels are `none`, `low`, `medium`, `high`, `xhigh`, `max`. Each model ID is its only snapshot. `gpt-6-sol` is not deprecated and is not an alias of `gpt-6.1-sol`.

Model-specific constraints:

- **`gpt-6-astra`:** no `none` effort, no custom `temperature`/`top_p`, no logprobs; tool calling needs the Responses API. Ultrafast mode since 2026-09-29 (US data residency only).
- **`gpt-6.1-sol`:** Chat Completions, Responses, Batch; tool calling needs the Responses API. Ultrafast mode since 2026-10-08 (Responses API, priced separately).
- **`gpt-6.1-terra`:** Chat Completions, Responses, Batch. Not Realtime, fine-tuning or embeddings. Responses tools include web/file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP and tool search. Standard rate limits: Build 5,000 RPM / 1M TPM, Launch 10,000 / 4M, Grow 15,000 / 40M.
- **`gpt-6-luna`:** Chat Completions function calling only when effort = `none`. EU residency for Standard/Fast/Flex/Batch. Sole model on the Decisions API.
- **`gpt-6-sol` / `gpt-6-luna`:** a 2026-09-25 image-encoding bug fix affected both; re-run image-input evals built before that date.

### Decisions API (`gpt-6-luna` only)

> Source: https://developers.openai.com/api/docs/guides/decisions and https://developers.openai.com/api/docs/changelog (fetched 2026-11-13)

- **Beta 2026-10-06, GA 2026-10-22.** `POST /v1/decisions`; `gpt-6-luna` is the only supported model; "about 10x faster than the Responses API".
- Question types: **predicate** (probability 0–1), **choice** (distribution + confidence), **score** (probability-weighted level index, 2–10 levels). 1–400 questions per request, each with a unique `name`.
- Inputs: text or a message array incl. images (base64 data URL or http URL) and `input_json`; file IDs not supported.
- Pricing: uncached input $0.10/MTok, cache hits discounted, cache writes charged, **output tokens not charged**. Regional and long-context multipliers can apply. Shared input is cached by default (reusable prefix ≥1,024 tokens). ZDR and HIPAA for eligible customers.
- Use it for high-volume classification, routing and scoring where a calibrated probability is the output. Whether Jev or another decision model fits better is out of scope here (route to `ai-models-specialist`).

### Long-context meter

> Source: https://developers.openai.com/api/docs/pricing and the GPT-6.x model pages (fetched 2026-11-13); GPT-5.6 rows 2026-08-05

OpenAI charges a **higher rate for the whole request once input exceeds 272K tokens**, unlike Claude 4.6+ (flat across 1M, except Haiku 5.5's 100K step).

| Model | Standard in/out | >272K in/out | Basis |
|---|---|---|---|
| `gpt-6-astra` | $10 / $50 | **$20 / $75** | Pricing page |
| `gpt-6.1-sol` | $2 / $10 | $4 / $15 | Page rule: 2x input/cache, 1.5x output |
| `gpt-6.1-terra` | $1 / $5 | $2 / $7.50 | Page rule: 2x input/cache, 1.5x output |
| `gpt-6-luna` | $0.10 / $0.50 | not stated (page: ">272K costs more") | — |
| `gpt-6-sol` | $2 / $10 | not stated (price given for ≤272K) | — |
| `gpt-5.6-sol` (2026-08-05, at the $5/$30 rate) | $5 / $30 | $10 / $45 | 2026-08-05 pricing page |
| `gpt-5.6-terra` (2026-08-05) | $2 / $12 | $4 / $18 | 2026-08-05 pricing page |
| `gpt-5.6-luna` (2026-08-05) | $0.20 / $1.20 | $0.40 / $1.80 | 2026-08-05 pricing page |

The long-context rate for `gpt-5.6-sol` under the $4/$20 promo was not captured.

## Full current pricing table

> Source: https://developers.openai.com/api/docs/pricing.md and https://developers.openai.com/api/docs/models/all (fetched 2026-11-13); rows marked 2026-08-05 were not re-captured

Per 1M tokens, Standard, prompts ≤272K, USD:

| Model | Input | Cached input | Output | Notes |
|---|---|---|---|---|
| `gpt-6-astra` | $10.00 | $1.00 | $50.00 | Batch $5/$25; Fast $20/$100; Ultrafast ~6x |
| `gpt-6.1-sol` | $2.00 | $0.10 | $10.00 | Ultrafast ~6x (Bedrock Global Ultrafast: $12/$60) |
| `gpt-6-sol` | $2.00 | $0.20 | $10.00 | Superseded by 6.1 Sol; not deprecated |
| `gpt-6.1-terra` | $1.00 | $0.05 | $5.00 | |
| `gpt-6-luna` | $0.10 | $0.01 | $0.50 | |
| `gpt-5.6-sol` (alias `gpt-5.6`) | **$4.00** | $0.40 | **$20.00** | Promo from 2026-08-21 (was $5/$0.50/$30). **Ends 2026-11-30** per pricing + model pages; the changelog said "at least through November 21". 1.05M ctx, 922K in, 128K out, cutoff Feb 16, 2026 |
| `gpt-5.6-terra` | $2.00 | $0.20 | $12.00 | Listed, not deprecated |
| `gpt-5.6-luna` | $0.20 | $0.02 | $1.20 | Listed, not deprecated |
| `gpt-5.5` | $5.00 | $0.50 | $30.00 | 272K context limit (2026-08-05); not deprecated |
| `gpt-5.5-pro` | $30.00 | — | $180.00 | Not deprecated |
| `gpt-5.4` | $2.50 | $0.25 | $15.00 | 272K context limit (2026-08-05); not deprecated |
| `gpt-5.4-pro` | $30.00 | — | $180.00 | Not deprecated |
| `gpt-5.4-mini` | $0.75 | not re-captured | $4.50 | |
| `gpt-5.4-nano` | $0.20 | $0.02 (2026-08-05) | $1.25 | **Deprecated, shutdown 2027-04-01 → `gpt-6-luna`** |
| `gpt-5.2` (2026-08-05) | $1.75 | $0.175 | $14.00 | Status UNVERIFIED 2026-11-13 |
| `gpt-5` / `gpt-5-mini` (2026-08-05) | $1.25 / $0.25 | $0.125 / $0.025 | $10.00 / $2.00 | **Shutdown 2026-12-11** |
| `gpt-4o` / `gpt-4o-mini` (2026-08-05) | $2.50 / $0.15 | $1.25 / $0.075 | $10.00 / $0.60 | Dated snapshots shut down 2027-01-14 → `gpt-6-luna` |
| `o3` (2026-08-05) | $2.00 | $0.50 | $8.00 | **Shutdown 2026-12-11** |

`gpt-oss-120b` / `gpt-oss-20b` have no OpenAI price (open weights). The 2026-08-05 `o1` row is dropped: its 2026-10-23 shutdown date has passed (see `lifecycle-and-deprecations.md`).

**Pricing modifiers** (2026-11-13): Batch about **50%**; Flex near Batch; Fast about **2x**; **Ultrafast about 6x Standard** (`gpt-6-astra`, `gpt-6.1-sol`; `gpt-5.6-sol` limited preview from 2026-08-13); **+10%** regional/FedRAMP uplift for models released on or after 2026-03-05. **12-hour prompt cache writes cost 2.5x input** (2026-10-20). Usage tiers cut from five to three on 2026-10-06: Build, Launch, Grow. Fast mode for >272K prompts on `gpt-5.6-sol/terra/luna` since 2026-08-05.

## Specialist and restricted-access models

> Source: https://developers.openai.com/api/docs/changelog, https://developers.openai.com/api/docs/models/gpt-6-cyber, https://developers.openai.com/api/docs/pricing.md, https://developers.openai.com/api/docs/deprecations (fetched 2026-11-13)

| Model ID | Access | Released | Price $/MTok in / cached / out | Notes |
|---|---|---|---|---|
| `gpt-6-cyber` | Daybreak Red access + approval | 2026-11-05 | ≤272K $20 / $2 / $100 (cache write $25); >272K $40 / $4 / $150 | 1.05M / 922K / 128K; Chat Completions + Responses |
| `gpt-5.6-cyber` | Restricted | 2026-08-07 | not stated | Launched with `gpt-daybreak-blue-latest` and `gpt-daybreak-red-latest` (red tier needs separate approval) |
| `gpt-5.5-cyber-preview` | — | — | — | **Deprecated, shutdown 2027-02-01** (notice 2026-11-05) |
| `gpt-5.4-cyber` | — | — | — | **Retired 2026-10-01** |
| `gpt-6-rosalind` | Life Sciences trusted access | 2026-10-30 | $15 / $1.50 / $75 | Model page 404s; ID from changelog + pricing only |
| `gpt-rosalind-research` | Life Sciences trusted access | GA 2026-09-08 (billing from 2026-10-05) | $5 / $0.50 / $25 | Coexists with `gpt-6-rosalind` |
| `gpt-rosalind-discovery` | Life Sciences trusted access | not found | $5 / $0.50 / $25 | Seen only on the pricing page |

The models index shows a single "GPT-Rosalind" entry with no ID. Treat all three Rosalind IDs as **pricing-page-verified only**.

## Other families

> Source: https://developers.openai.com/api/docs/pricing.md, https://developers.openai.com/api/docs/models, https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst, …/gpt-image-2.6-flare, …/gpt-live-1, …/gpt-transcribe (fetched 2026-11-13)

- **Realtime / voice:** `gpt-realtime-2.1`: audio $32 / $0.40 cached / $64, text $4 / $0.40 / $24, image $5 / $0.50 (gap-fill confirmed the 2026-08-05 figures). `gpt-realtime-2` has the same audio/text/image rates. `gpt-realtime-2.1-mini`: audio $10 / $20, text $0.60 / $2.40. `gpt-realtime-translate` (speech-to-speech translation) and `gpt-realtime-1.5` are listed without prices.
- **`gpt-live-1`** (GA 2026-09-10): full-duplex voice, audio+text in/out, **$0.05/min billed per second** (backend model and tools billed separately), `v1/live/sessions` only; concurrent sessions Build 50 / Launch 300 / Grow 500; cutoff Jul 31, 2025. Outbound SIP calling for all orgs since 2026-11-02.
- **Transcription:** `gpt-transcribe` $0.0045/min; `gpt-live-transcribe` and `gpt-realtime-whisper` $0.017/min; `gpt-4o-transcribe` $0.006, `gpt-4o-mini-transcribe` $0.003, `whisper` $0.006 (the last three are deprecated, shutdown 2027-02-26).
- **TTS:** `tts-1` $15 / 1M chars, `tts-1-hd` $30; both deprecated with `gpt-4o-mini-tts`, shutdown 2027-01-06 → `gpt-realtime-2.1-mini`.
- **Image generation:** `gpt-image-2.6-sunburst` ("detailed visual work") and `gpt-image-2.6-flare` (interactive/fast), released 2026-11-04: text in $5 / $1.25 cached, image in $8 / $2 cached, **image out $30**; adjustable complexity, SVG and animated-GIF output; `v1/images/generations` and `v1/images/edits` only. `gpt-image-2.5-sunburst` / `gpt-image-2.5-flare` (2026-09-08): prices not captured (2.5 page unfetched); markup-guided editing on 2.5 and 2.6. `gpt-image-2` is **deprecated, shutdown 2027-02-10** → 2.6 sunburst/flare. `gpt-image-1.5` (2026-08-05: text $5 / $1.25 / $10, image $8 / $2 / $32) not re-verified.
- **Video (Sora, 2026-08-05, not re-verified):** `sora-2` $0.10/sec at 720p; `sora-2-pro` $0.30–$0.70/sec (720p–1080p).
- **Embeddings / moderation:** `text-embedding-3-small` $0.02/MTok; `text-embedding-3-large` $0.13; `text-embedding-ada-002` $0.10. `omni-moderation-latest` free.

## Open-weight: gpt-oss (no new release)

> Source: https://developers.openai.com/api/docs/models/gpt-oss-120b (fetched 2026-11-13)

- No gpt-oss model newer than `gpt-oss-120b` / `gpt-oss-20b` was found; both are listed under "Open-weight models" and are not deprecated.
- `gpt-oss-120b`: Apache 2.0; 117B total / 5.1B active parameters; 131,072 context and output; cutoff Jun 1, 2024; text only; effort low/medium/high; Responses and Batch only on the OpenAI API; Hugging Face `openai/gpt-oss-120b`; Bedrock `openai.gpt-oss-120b`; Azure preview. `gpt-oss-20b`'s page was not fetched.

## GPT-5-Codex (agentic coding, 2026-08-05)

> Source: https://developers.openai.com/api/docs/models/gpt-5-codex (fetched 2026-08-05; not re-verified)

- **Model ID:** `gpt-5-codex`
- Pricing: input $1.25/MTok, cached input $0.125/MTok, output $10.00/MTok.
- Context window 400,000 tokens; max input 272,000; max output 128,000.
- "A version of GPT-5 optimized for agentic coding tasks," available **exclusively through the Responses API**, not Chat Completions.
- Knowledge cutoff: **September 30, 2024**.
- Smaller variant referenced on the same page: `codex-mini-latest` ($1.50 input / $6 output per MTok); full specs not confirmed there.

`gpt-5.3-codex` exists and is **deprecated** (shutdown 2027-04-01 → `gpt-6-sol`), so OpenAI's named Codex successor is the general `gpt-6-sol`. **UNVERIFIED:** no `gpt-5.6-codex` or `gpt-6-codex` ID appears in any fetched doc; treat such claims as unverified.

## Official model-selection framework (2026-08-05)

> Source: https://developers.openai.com/api/docs/guides/model-selection (fetched 2026-08-05; not re-verified)

Two-phase optimization:

1. **Optimize for accuracy first**: iterate on prompting and architecture until the accuracy target is met.
2. **Optimize for cost and latency second**: then maintain that accuracy with the cheapest, fastest model possible.

**Set the accuracy target from financial impact**, not an arbitrary round number. Worked example (fake-news classifier): each correctly classified article saves ~$50 in review costs; each misclassification costs ~$300 in remediation. That asymmetry computes to a break-even minimum accuracy of **85.8%**.

**Cost/latency tactics once the target is hit:** reduce API requests per task; minimize input volume and constrain output length; move to a smaller model that still clears the bar.

**Worked comparison** (1,000 articles, fake-news classification):

| Approach | Accuracy | Cost | Latency |
|---|---|---|---|
| GPT-4o zero-shot | 84.5% (below target) | $1.72 | <1s |
| GPT-4o few-shot (5 examples) | 91.5% (meets target) | $11.92 | <1s |
| GPT-4o-mini fine-tuned | 91.5% (meets target) | $0.21 | <1s |

Takeaway: a smaller fine-tuned model matched few-shot accuracy at under 2% of the cost, once the accuracy target was pinned down.

**Tier positioning (2026-11-13, from model-page wording):** `gpt-6-astra` for the most demanding work, `gpt-6.1-sol` for near-Astra quality at a fifth of the price, `gpt-6.1-terra` for fast visual reasoning / computer use / writing, `gpt-6-luna` for focused high-volume work. The guide itself still described the GPT-5.6 tiers when last fetched.

## Sources

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/all
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/models/gpt-6-sol
- https://developers.openai.com/api/docs/models/gpt-6.1-terra
- https://developers.openai.com/api/docs/models/gpt-6-luna
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/models/gpt-6-cyber
- https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst
- https://developers.openai.com/api/docs/models/gpt-image-2.6-flare
- https://developers.openai.com/api/docs/models/gpt-live-1
- https://developers.openai.com/api/docs/models/gpt-transcribe
- https://developers.openai.com/api/docs/models/gpt-oss-120b
- https://developers.openai.com/api/docs/guides/decisions
- https://developers.openai.com/api/docs/pricing.md
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/deprecations
- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure (gpt-6-astra date conflict)
- https://developers.openai.com/api/docs/models/gpt-5-codex (2026-08-05)
- https://developers.openai.com/api/docs/guides/model-selection (2026-08-05)

Fetched: 2026-11-13 (rows and sections marked 2026-08-05 were carried forward, not re-verified)
