# Anthropic Claude: model catalog, pricing, and mechanics (as of 2026-11-13)

Read when the question names Claude, Anthropic, Fable, Mythos, Opus, Sonnet, or Haiku, or asks for a Claude model ID / price / limit. Re-verify against the source URLs before quoting. Sections and rows still carrying 2026-08-05 data say so.

## Current lineup

> Source: https://platform.claude.com/docs/en/models/overview, https://platform.claude.com/docs/en/models/fable-5-2/overview, https://platform.claude.com/docs/en/models/opus-5-5/overview, https://platform.claude.com/docs/en/models/sonnet-5-5/overview, https://platform.claude.com/docs/en/models/haiku-5-5/overview (fetched 2026-11-13)

Anthropic's stated default as of 2026-08-05 was **Opus** for complex agentic coding and enterprise work and **Fable** for the highest available capability. The 2026-11-13 refresh did not re-capture that overview sentence; the Fable 5.2 page describes it as "For demanding reasoning and long-horizon agentic work."

All current Claude models take text and image input and emit text. Available via the Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud (Google managed and Anthropic managed), and Microsoft Foundry, with per-platform exceptions in `cloud-availability.md`.

| Feature | Claude Fable 5.2 | Claude Opus 5.5 | Claude Sonnet 5.5 | Claude Haiku 5.5 |
|---|---|---|---|---|
| Claude API ID | `claude-fable-5-2` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Released | 2026-11-09 | 2026-09-22 | 2026-09-28 | 2026-10-07 |
| Bedrock ID | `global.anthropic.claude-fable-5-2` (bedrock-runtime only) | `anthropic.claude-opus-5-5` (mantle) | `anthropic.claude-sonnet-5-5` (mantle) | `anthropic.claude-haiku-5-5` (mantle) |
| Google Cloud ID | `claude-fable-5-2` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Price in/out per MTok | $8 / $40 | $4 / $20 | $2 / $10 | $0.10 / $0.50 up to 100K prompt; $0.50 / $2.50 above |
| Thinking | Adaptive, always on, cannot be disabled | Adaptive, always on | `disabled` rejected; `thinking:{type:"between_tools"}` at `high` effort or below | Adaptive |
| Default `effort` | `high` (levels low/medium/high/xhigh/max) | `medium` | `high` | `medium` |
| Comparative latency | Moderate | not captured 2026-11-13 | not captured | not captured |
| Context window | 1M | 1M | 1M (Google managed page: 1M for all 5.x) | 1M |
| Max output | 128K | 128K | 128K | 128K |
| Batch 300K output beta | No | Yes | Yes | Yes |
| Knowledge cutoff | Jun 2026 (reliable and training) | Jun 2026 | Jun 2026 | Jun 2026 |
| Retirement not sooner than | 2027-11-09 | 2027-09-22 | 2027-09-28 | 2027-10-07 |

**Fable 5.2 / Mythos 5.2 access.** Fable 5.2 is GA on every platform except Bedrock mantle. `claude-mythos-5-2` (released 2026-11-09) is the same model, specs and price as Fable 5.2 ("Claude Fable 5.2 for verified organizations"); status "Active (verification required)", only for organizations verified through Anthropic's Cyber Verification Program (the announcement also names a Life Sciences Verification Program). Fable carries the stronger cyber/bio safeguards. Mythos is not listed for Claude Platform on AWS. Earlier tiers: `claude-mythos-5-1` (2026-09-01, $10/$50, limited), `claude-mythos-5` (Project Glasswing invitation, per the 2026-08-05 snapshot), `claude-mythos-preview` deprecated since 2026-06-09.

**Vendor-reported Fable 5.2 claims** (anthropic.com announcement, not independently verified): outputs up to 30% faster than Fable 5.1; classifiers block about 55% fewer queries than Fable 5.1; ahead of Opus 5.5 on the vendor's own coding, agentic and HLE benchmarks. Use only as a shortlist signal.

Additional facts:

- **Every Claude model ID is a pinned snapshot.** Dated IDs (`…-20250929`) are fixed releases; from the 4.6 generation onward IDs use a dateless format that is *also* pinned. Fable 5.2's alias row repeats the ID.
- **Tokenizer:** Fable 5.2 uses the tokenizer introduced with Opus 4.7 (~555k words per 1M tokens), producing roughly **30% more tokens** than pre-4.7 models for the same text.
- **Data retention:** Fable 5.2 requires 30-day data retention and is not available under ZDR unless expressly authorized.
- **300k output beta:** the Message Batches API supports up to 300k output on Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Haiku 5.5, Opus 4.8/4.7/4.6 and Sonnet 4.6, not Fable 5.2. The beta header recorded on 2026-08-05 was `output-300k-2026-03-24`.
- **Models API:** `GET /v1/models` returns `max_input_tokens`, `max_tokens`, and a `capabilities` object per model; between 2026-10-01 and 10-15 it gained `capabilities.thinking.types.between_tools`, `capabilities.thinking.types.disabled`, `capabilities.server_tools`, and `line`.

### Per-model request rejections (400s)

> Source: https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2, https://platform.claude.com/docs/en/models/sonnet-5-5/overview, https://platform.claude.com/docs/en/models/haiku-5-5/overview, https://platform.claude.com/docs/en/api/migration-2026-10-21 (fetched 2026-11-13)

- **Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5** reject `temperature`/`top_p`/`top_k` and forced `tool_choice` (`any`/`tool`). Use `auto` plus strict tool use.
- **Fable 5.2, Opus 5.5** also reject `thinking` `enabled`/`disabled`. Sonnet 5.5 rejects `disabled`.
- **Haiku 5.5** additionally rejects prefill, `budget_tokens`, and `computer_20250124`.
- **Fable 5.2 only:** `computer_20251124` returns 400 everywhere except Bedrock (use `computer_toolset_20260801`); replaying a thinking block after editing system/tools/earlier messages returns 400 ("The block is bound to a different conversation"; stopgap beta `thinking-binding-controls-2026-08-01`); only Fable 5.2 / Mythos 5.2 can read Fable 5.2 thinking blocks. A Fable 5.2 executor accepts only a Fable 5.2 / Mythos 5.2 advisor. Server-side fallback targets: Opus 4.8 and Opus 5.

### Previous generation (still Active)

> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations and https://platform.claude.com/docs/en/release-notes/overview (fetched 2026-11-13); spec notes marked 2026-08-05 were not re-captured

| Model | Claude API ID | Price in/out | Notes |
|---|---|---|---|
| Fable 5.1 | `claude-fable-5-1` | $10 / $50 (cache read $0.25) | Released 2026-09-01; superseded by Fable 5.2; retirement not sooner than 2027-09-01 |
| Mythos 5.1 | `claude-mythos-5-1` | $10 / $50 | Limited access, released 2026-09-01 |
| Fable 5 | `claude-fable-5` | $10 / $50 | GA since 2026-06-09; 1M / 128k; cutoff Jan 2026 (2026-08-05) |
| Opus 5 | `claude-opus-5` | $5 / $25 | 1M / 128k; cutoff May 2026 (2026-08-05); fast mode still research preview |
| Sonnet 5 | `claude-sonnet-5` | **$2 / $10 (permanent)** | 2026-08-10: the intro price became standard; the planned 2026-09-01 rise to $3/$15 was cancelled |
| Haiku 4.5 | `claude-haiku-4-5-20251001` (alias `claude-haiku-4-5`) | $1 / $5 | 200k / 64k; cutoff Feb 2025; still Active although its "not sooner than 2026-10-15" date has passed |

### Legacy models (2026-08-05 specs; status updated 2026-11-13)

| Feature | Opus 4.8 | Opus 4.7 | Opus 4.6 | Sonnet 4.6 | Sonnet 4.5 | Opus 4.5 |
|---|---|---|---|---|---|---|
| Claude API ID | `claude-opus-4-8` | `claude-opus-4-7` | `claude-opus-4-6` | `claude-sonnet-4-6` | `claude-sonnet-4-5-20250929` (**deprecated, retires 2026-11-30**) | `claude-opus-4-5-20251101` |
| AWS Bedrock ID | `anthropic.claude-opus-4-8` | `anthropic.claude-opus-4-7` | `anthropic.claude-opus-4-6-v1` | `anthropic.claude-sonnet-4-6` | `anthropic.claude-sonnet-4-5-20250929-v1:0` | `anthropic.claude-opus-4-5-20251101-v1:0` |
| Google Cloud ID | `claude-opus-4-8` | `claude-opus-4-7` | `claude-opus-4-6` | `claude-sonnet-4-6` | `claude-sonnet-4-5@20250929` | `claude-opus-4-5@20251101` |
| Price in/out per MTok | $5/$25 | $5/$25 | $5/$25 | $3/$15 | $3/$15 | $5/$25 |
| Extended thinking | No | No | Yes (deprecated) | Yes (deprecated) | Yes | Yes |
| Adaptive thinking | Yes | Yes | Yes | Yes | No | No |
| Context window | 1M | 1M | 1M | 1M | 200k | 200k |
| Max output | 128k | 128k | 128k | 128k | 64k | 64k |
| Reliable knowledge cutoff | Jan 2026 | Jan 2026 | May 2025 | Aug 2025 | Jan 2025 | May 2025 |

`claude-opus-4-1-20250805` is **retired** on the Claude API (2026-08-05); the models overview still lists it on Bedrock and Google managed. Opus 4.8 fast mode is removed 2026-11-30.

## Pricing detail

> Source: https://platform.claude.com/docs/en/about-claude/pricing and the per-model overview pages (fetched 2026-11-13; rows marked 2026-08-05 were not re-captured)

Per million tokens, USD:

| Model | Base input | 5m cache write | 1h cache write | Cache hit/refresh | Output |
|---|---|---|---|---|---|
| Claude Fable 5.2 / Mythos 5.2 | $8 | $10 | $16 | $0.20 (0.025x) | $40 |
| Claude Fable 5.1 / Mythos 5.1 | $10 | not captured | not captured | $0.25 (0.025x) | $50 |
| Claude Fable 5 / Mythos 5 (2026-08-05) | $10 | $12.50 | $20 | $1 (see conflict note) | $50 |
| Claude Opus 5.5 | $4 | $5 | $8 | $0.20 (0.05x) | $20 |
| Claude Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 (2026-08-05) | $5 | $6.25 | $10 | $0.50 | $25 |
| Claude Sonnet 5.5 | $2 | $2.50 | $4 | **$0.10** (0.05x; cut from $0.20 on 2026-10-07) | $10 |
| Claude Sonnet 5 (2026-08-05 intro rows; base made permanent 2026-08-10) | $2 | $2.50 | $4 | $0.20 | $10 |
| Claude Sonnet 4.6 / 4.5 (2026-08-05) | $3 | $3.75 | $6 | $0.30 | $15 |
| Claude Haiku 5.5, prompt ≤100K | $0.10 | $0.125 | $0.20 | $0.01 | $0.50 |
| Claude Haiku 5.5, prompt >100K | $0.50 | $0.625 | $1 | $0.05 | $2.50 |
| Claude Haiku 4.5 (2026-08-05) | $1 | $1.25 | $2 | $0.10 | $5 |
| Claude Opus 4.1 (retired on Claude API; 2026-08-05) | $15 | $18.75 | $30 | $1.50 | $75 |

**Conflict, cache reads:** the models overview says cache reads cost 10% of input; its footnote says 2.5% for Fable 5.x / Mythos 5.x and 5% for Opus 5.5 / Sonnet 5.5, and the per-model tables agree with the footnote. Whether "Fable 5.x" covers the original Fable 5 (shown at $1 = 10% on 2026-08-05) is not stated: re-verify before quoting a Fable 5 cache price.

### Prompt caching multipliers (relative to base input)

| Cache operation | Multiplier | Duration |
|---|---|---|
| 5-minute cache write | 1.25x base input | Valid 5 minutes |
| 1-hour cache write | 2x base input | Valid 1 hour |
| Cache read (hit) | 0.1x default; **0.05x** Opus 5.5 / Sonnet 5.5; **0.025x** Fable 5.x / Mythos 5.x | Same duration as the preceding write |

Caching pays off after **one** cache read on the 5-minute tier (1.25x write) or **two** reads on the 1-hour tier (2x write); the cheaper reads on 5.5 / 5.x models only shorten the payback. Multipliers stack with the Batch API discount and the data-residency multiplier.

### Batch API (50% off input and output)

| Model | Batch input | Batch output |
|---|---|---|
| Claude Fable 5.2 / Mythos 5.2 | $4 | $20 |
| Claude Fable 5.1 / Fable 5 / Mythos 5.1 / Mythos 5 | $5 | $25 |
| Claude Opus 5.5 | $2 | $10 |
| Claude Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 | $2.50 | $12.50 |
| Claude Sonnet 5.5 / Sonnet 5 | $1 | $5 |
| Claude Sonnet 4.6 / 4.5 | $1.50 | $7.50 |
| Claude Haiku 5.5 (≤100K / >100K prompt) | $0.05 / $0.25 | $0.25 / $1.25 |
| Claude Haiku 4.5 | $0.50 | $2.50 |

Fable 5.2's $4/$20 is stated directly and Haiku 5.5's page says "50% batch". The Opus 5.5, Sonnet 5.5, Fable 5.1 and Sonnet 5 rows apply the pricing page's 50% batch rule (2026-08-05) arithmetically: confirm on the pricing page before quoting.

### Long context, data residency, fast mode

> Source: https://platform.claude.com/docs/en/about-claude/pricing and https://platform.claude.com/docs/en/build-with-claude/fast-mode (fetched 2026-11-13)

- **Long context:** Claude 4.6+ models include the full 1M window at **one rate** (2026-08-05 rule): a 900k-token request costs the same per token as a 9k one. **Exception: Haiku 5.5 steps up 5x once the prompt exceeds 100K tokens** ($0.10/$0.50 → $0.50/$2.50, cache rates likewise).
- **Data residency:** on Claude 4.6+, `inference_geo: "us"` applies a **1.1x multiplier** to every token category; global routing is standard price. The 1.1x also applies to Haiku 5.5's higher price tier.
- **Fast mode** (`speed:"fast"`), up to 2.5x output tokens/sec:

| Model | Fast price in/out | Status | Where |
|---|---|---|---|
| Fable 5.2 / Mythos 5.2 | $16 / $80 | Available since 2026-11-09, no beta header | Claude API, Google Cloud (Anthropic managed), Google Cloud (Google managed; Google sets the price), Foundry Anthropic-hosted (`claude-fable-5-2-fast`, `claude-mythos-5-2-fast`) |
| Opus 5.5 | $8 / $40 | **GA 2026-10-15**, no beta header, default fast rate limit in Start/Build/Scale tiers | Claude API, Foundry Azure-hosted (`claude-opus-5-5-fast`, 2026-10-15), Google Cloud Anthropic managed (2026-10-22) |
| Opus 5 | $10 / $50 | Research preview, needs `fast-mode-2026-02-01` beta | Claude API |
| Opus 4.8 | $10 / $50 (2026-08-05) | **Deprecated 2026-10-30, removed 2026-11-30**; `speed:"fast"` then errors; migrate to Opus 5.5 | Claude API |

Not available on Claude Platform on AWS. Not available with the Batch API (2026-08-05). Stacks with caching and data-residency multipliers.

### Tool-use token overhead (2026-08-05)

System-prompt tokens added by tool definitions. No 5.5 / 5.2 figures were captured on 2026-11-13; those models reject `any`/`tool` anyway.

| Model | `auto` / `none` | `any` / `tool` |
|---|---|---|
| Opus 5 | 286 | 406 |
| Opus 4.8 | 290 | 410 |
| Opus 4.7 | 675 | 804 |
| Opus 4.6 | 497 | 589 |
| Sonnet 5 | 354 | 474 |
| Sonnet 4.6 | 497 | 589 |
| Haiku 4.5 | 496 | 588 |

Server tool pricing (2026-08-05): **web search** $10 per 1,000 searches plus tokens; **web fetch** free beyond token costs; **code execution** free with `web_search_20260209`+ or `web_fetch_20260209`+, otherwise billed by execution time (5-minute minimum, 1,550 free org-hours/month, then $0.05/hour/container).

## Billing and API changes that affect model choice

> Source: https://platform.claude.com/docs/en/release-notes/overview and https://platform.claude.com/docs/en/api/migration-2026-10-21 (fetched 2026-11-13; the migration page's breaking-changes section was read in full, its per-language SDK sections only skimmed)

- **API version `2026-10-21`** (default in the latest SDK majors: Python `anthropic` 2.0.0, TypeScript `@anthropic-ai/sdk` 1.0.0, Go v2.0.0, Java 3.0.0, C# 13.0.0, PHP 1.0.0, Ruby 2.0.0, `ant` CLI 2.0.0): `temperature`, `top_p`, `top_k` return **400 on every model, even at default values**, with no replacement. A model that still honored them (e.g. Sonnet 4.6) loses the ability to lower temperature; keep such requests on `2023-06-01`. Also: `document` blocks directly in assistant messages → 400 (inside tool results is fine); `citations` on user-message text blocks → 400. The SDKs send the key as `Authorization: Bearer` (not `X-Api-Key`, except Foundry clients) and drop Text Completions.
- **Bedrock:** models 4.6 and lower do not support `2026-10-21` on Bedrock; pin the older SDK major for them.
- **Refusal billing (2026-09-24):** refusals before any output are billed again when `stop_details.category` is `bio`, `frontier_llm` or `reasoning_extraction`.
- **Watermark (2026-11-03):** text watermark on Mythos 5, Opus 4.7 and Sonnet 4.6 output.
- **Computer/browser toolsets (2026-08-19/20):** `computer_toolset_20260801` and `browser_toolset_20260801` on the Claude API and Google Cloud for Fable 5, Mythos 5, Opus 5, Sonnet 5 and Opus 4.8.
- **Fable 5.2 betas:** compaction on demand (`compact-2026-09-04`), mid-conversation tool changes (`inline-tools-2026-09-15`).

### Worked cost examples (2026-08-05)

- Claude Managed Agents, Opus 5, one-hour session, 50,000 input + 15,000 output tokens, no caching: input $0.25 + output $0.375 + session runtime (1 hr × $0.08) = **$0.705**. With 40,000 of the input tokens served as cache reads: **$0.525**.
- Support tickets at ~3,700 tokens per conversation on Haiku 4.5: **≈$37.00 per 10,000 tickets**.

### Anthropic's own cost-optimization guidance (2026-08-05)

1. Match model to task: Haiku for simple work, Sonnet for most production workloads, Opus for the most complex reasoning.
2. Use prompt caching for repeated context.
3. Batch non-time-sensitive operations.
4. Monitor usage patterns to find optimization opportunities.

## Sources

- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/models/fable-5-2/overview
- https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- https://platform.claude.com/docs/en/models/mythos-5-2/overview
- https://platform.claude.com/docs/en/models/opus-5-5/overview
- https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- https://platform.claude.com/docs/en/models/haiku-5-5/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/build-with-claude/fast-mode
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/api/migration-2026-10-21
- https://www.anthropic.com/claude-fable-and-mythos-5-2
- https://platform.claude.com/docs/en/about-claude/models/overview (2026-08-05 rows)

Fetched: 2026-11-13 (rows and sections marked 2026-08-05 were carried forward, not re-verified)
