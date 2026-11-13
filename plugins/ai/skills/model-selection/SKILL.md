---
name: model-selection
description: "Anthropic, OpenAI and Google model tier selection when platform or existing stack constrains the choice; catalog snapshot 2026-11-13 (Gemini 2026-08-05) covers IDs, prices, limits, cutoffs, lifecycle and cloud availability. WHEN: platform-constrained model choice, Claude/GPT/Gemini tier comparison, cost/limit/deprecation lookup, Claude on Bedrock/Vertex. Do NOT use for broad source-traced model comparisons or exact identity lookup across families/providers, or deciding whether Jev fits versus other decision models; route those to `ai-models-specialist` if `ai-models` is installed. If absent, answer only from this skill's covered catalog and disclose gaps. API mechanics → `claude-api`/`openai-api`; cloud routing/operations → `inference-providers`; architecture → `overview`; evals → `evals`; fine-tuning → `fine-tuning`."
license: MIT
---

# Model Selection (cross-vendor)

Choosing a capability tier within a user-constrained platform or existing Anthropic/OpenAI/Google stack, including how hosting availability constrains the choice and when catalog facts expire. For source-traced comparisons across model families/providers and canonical model identity lookup, route to `ai-models-specialist` when installed.

## Freshness contract — read first

**Anthropic and OpenAI data is a snapshot of 2026-11-13; Gemini data is still the 2026-08-05 snapshot. Treat every number as stale until re-verified.** Model IDs, prices, context limits, and retirement dates change monthly; between the two snapshots both vendors shipped a new generation.

- Always re-fetch the vendor page cited at the bottom of the relevant reference file before quoting a price, an ID, or a retirement date to a user who will act on it. Cheap to check, expensive to get wrong.
- Always state the as-of date alongside any figure you give ("as of 2026-11-13, per Anthropic's pricing page"; "as of 2026-08-05" for Gemini). A price without a date is a bug.
- Never invent or "remember" a model ID. Model IDs are string literals — a wrong one is a hard 404/400, and plausible-looking guesses (`claude-opus-5-5-20260922`, `gpt-6-codex`, `gemini-3.6-pro`) are the most common failure. Take IDs only from the reference tables here or from a live vendor page.
- Programmatic ground truth for Claude: `GET /v1/models` returns `max_input_tokens`, `max_tokens`, and a `capabilities` object per model. Run `scripts/list-claude-models.sh` instead of asserting from memory.
- Items the source docs did not publish are marked **UNVERIFIED** or "not stated" in the references, and recorded vendor conflicts are kept visible (e.g. `gpt-6-astra` release date). Repeat those markers; never launder them into facts.

## Default picks (when the user gives you no constraints)

| Need | Pick | Why |
|---|---|---|
| Complex agentic coding, enterprise work (Claude) | `claude-opus-5-5` | Current Opus (Opus was Anthropic's stated default as of 2026-08-05); $4/$20, default effort `medium` |
| Highest available Claude capability | `claude-fable-5-2` | Latest generally available Fable (2026-11-09); $8/$40, 2x Opus 5.5 |
| Most production Claude workloads | `claude-sonnet-5-5` | $2/$10, cache read $0.10, default effort `high` |
| High-volume cheap Claude work | `claude-haiku-5-5` | $0.10/$0.50 up to 100K prompt ($0.50/$2.50 above), 1M context |
| Frontier OpenAI | `gpt-6-astra` | $10/$50, OpenAI's "most capable" |
| Near-frontier OpenAI at a fifth of the price | `gpt-6.1-sol` | $2/$10, "near-Astra performance" |
| Balanced OpenAI | `gpt-6.1-terra` | $1/$5, visual reasoning / computer use / writing, latest OpenAI cutoff (Jun 1 2026) |
| High-volume OpenAI, classification, scoring | `gpt-6-luna` | $0.10/$0.50; sole model on the Decisions API (output tokens not charged) |
| Frontier Google | `gemini-3.1-pro-preview` | Pro tier is preview-only in the 3.x line — accept preview risk or use `gemini-2.5-pro` |
| Balanced/agentic Google | `gemini-3.6-flash` | $1.50/$7.50, GA, default model for Antigravity |
| Cheapest Google | `gemini-3.5-flash-lite` or `gemini-2.5-flash-lite` | $0.30/$2.50 and $0.10/$0.40 |

Full tables with cloud IDs, cutoffs, and cache/batch rates: `references/claude-catalog.md`, `references/openai-catalog.md`, `references/gemini-catalog.md`.

## Cross-vendor tier map (Anthropic/OpenAI 2026-11-13; Google 2026-08-05)

Use for "what is the equivalent of X on vendor Y" and for cost comparison at equal capability tier. Prices are per million tokens, input/output, standard (non-batch, non-cached, non-long-context) first-party rates.

| Tier | Anthropic | OpenAI | Google |
|---|---|---|---|
| Above-frontier / limited | `claude-mythos-5-2` $8/$40 (verification required) | `gpt-5.5-pro` $30/$180; `gpt-6-cyber` $20/$100 (Daybreak Red access) | — |
| Frontier | `claude-fable-5-2` $8/$40 | `gpt-6-astra` $10/$50 | `gemini-3.1-pro-preview` $2–4/$12–18 (preview) |
| Workhorse-high | `claude-opus-5-5` $4/$20 | `gpt-6.1-sol` $2/$10 | `gemini-3.6-flash` $1.50/$7.50 |
| Balanced | `claude-sonnet-5-5` $2/$10 | `gpt-6.1-terra` $1/$5 | `gemini-3.5-flash` $1.50/$9 |
| Cheap/high-volume | `claude-haiku-5-5` $0.10/$0.50 (≤100K prompt) | `gpt-6-luna` $0.10/$0.50 | `gemini-3.5-flash-lite` $0.30/$2.50 |
| Floor | — | — (`gpt-6-luna` undercuts the legacy `gpt-4o-mini`, whose snapshots shut down 2027-01-14) | `gemini-2.5-flash-lite` $0.10/$0.40 |

Rows align on *positioning*, not on measured capability — vendors do not benchmark identically and tier names are marketing. Treat the map as a shortlist generator, then decide with your own evals.

Structural asymmetries worth stating out loud to users:

- **Google has no GA Pro-tier model in the 3.x line** (2026-08-05). Pro is preview (`gemini-3.1-pro-preview`) or a generation back (`gemini-2.5-pro`). A Google-only stack that needs GA frontier reasoning is constrained.
- **OpenAI's ladder is unusually steep.** `gpt-6-luna` is 1/100th of `gpt-6-astra` on input and all five GPT-6.x models share the 1.05M context and 128K output, so tier-routing inside GPT-6 is especially effective. Cutoffs differ (Apr 20 – Jun 1 2026), so check the one you need.
- **Haiku 5.5 is two price tiers in one model.** Prompts over 100K tokens cost 5x ($0.50/$2.50); other current Claude models price the full 1M window flat (2026-08-05 rule). Size a long-context Haiku design at the upper tier, not the headline rate.
- **Restricted-access tiers are not orderable.** Mythos 5.2, `gpt-6-cyber` and the Rosalind models need vendor verification or trusted-access approval.

## How to choose

**Optimize accuracy first, cost second.** Iterate on prompt and architecture until the task hits its accuracy target; only then hunt for the cheapest model that holds that accuracy. Reversing the order produces a cheap model that is wrong, which costs more than the expensive model. (OpenAI's published framework; it generalizes.)

**Derive the accuracy target from money, not from a round number.** Compare the value of a correct output against the remediation cost of a wrong one. OpenAI's worked classifier example — $50 saved per correct call, $300 lost per wrong one — yields a break-even threshold of 85.8%, not "95% because that sounds good."

**Move down the tier ladder, not across vendors, when cost hurts.** Within a family the tiers mostly share the API surface, so a tier swap is close to a one-line change and an eval re-run — but check the per-model parameter rejections first (`references/claude-catalog.md`, `references/openai-catalog.md`). Ladders as of 2026-11-13 (Gemini 2026-08-05):

- Claude: Fable 5.2 → Opus 5.5 → Sonnet 5.5 → Haiku 5.5
- OpenAI: `gpt-6-astra` → `gpt-6.1-sol` → `gpt-6.1-terra` → `gpt-6-luna`
- Gemini: Pro → Flash → Flash-Lite (Google's own heuristic; Flash is claimed to cover 80–90% of production workloads at ~1/10 Pro cost)

**Never pick a model on price alone.** Cheaper-per-token frequently loses on total cost: a weak model retries, produces longer outputs, and burns more agent turns. Compare cost *per successfully completed task*, measured on your own eval set (see the `evals` skill), not $/MTok.

**Route by task, not by one global default.** A production system usually wants two or three models: a frontier tier for planning/hard reasoning, a mid tier for the main loop, a cheap tier for classification, extraction, routing, and subagent fan-out. Anthropic's guidance is the same shape — Haiku for simple tasks, Sonnet for most production, Opus for the hardest reasoning. For pure classify/score calls on OpenAI, the Decisions API on `gpt-6-luna` returns calibrated probabilities without paying for output tokens.

**Consider a small fine-tune before a bigger model.** OpenAI's published comparison: GPT-4o few-shot hit 91.5% for $11.92 per 1,000 articles; a fine-tuned GPT-4o-mini hit the same 91.5% for $0.21. When the task is narrow, repeated, and has labeled data, tuning a small model beats renting a big one — hand off to `fine-tuning` and `training-datasets`. Note `gpt-6.1-terra` does not support fine-tuning.

## Constraints that eliminate candidates before price does

Check these first; they are hard filters, not preferences.

- **Knowledge cutoff.** If the task depends on post-cutoff facts, no amount of intelligence saves it — add retrieval or web search. Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5 are all Jun 2026; Haiku 4.5 is Feb 2025. OpenAI: `gpt-6.1-terra` Jun 1 2026, `gpt-6-luna` May 18 2026, `gpt-6-astra` / `gpt-6.1-sol` Apr 30 2026, `gpt-6-sol` Apr 20 2026, GPT-5.6 Feb 16 2026. Gemini 2.5 is Jan 2025; **Gemini 3.x cutoffs are UNVERIFIED — not published on the fetched docs pages.**
- **Context window.** All current Claude 5.x models are 1M; Haiku 4.5 is 200k. GPT-6.x and GPT-5.6 are 1.05M (922K max input); `gpt-5.5`/`gpt-5.4` are capped at 272k. Gemini 2.5 Pro/Flash and 3.1 Pro Preview are 1,048,576 input.
- **Max output.** Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5 128K; GPT-6.x 128K; Gemini 65,536 (3.6 Flash: 64,000). A 200k-token report is not one request on any of them. Claude's Message Batches API reaches 300k output on Opus 5.5 / 5 / 4.8 / 4.7 / 4.6, Sonnet 5.5 / 5 / 4.6 and Haiku 5.5 via a beta header — **not Fable 5.2**.
- **Thinking mode.** Fable 5.2 and Opus 5.5 run adaptive thinking always on and return 400 for `thinking` `enabled`/`disabled`; Sonnet 5.5 rejects `disabled` (use `thinking:{type:"between_tools"}` at `high` effort or below); Haiku 5.5 rejects `budget_tokens`. Default effort differs: `high` on Fable 5.2 and Sonnet 5.5, `medium` on Opus 5.5 and Haiku 5.5 — set it explicitly when comparing tiers.
- **Sampling params are gone.** On Claude API version `2026-10-21` (default in the latest SDK majors), `temperature`, `top_p`, `top_k` return **400 on every model, even at default values**; Fable 5.2 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 reject them on any version. `gpt-6-astra` accepts no custom `temperature`/`top_p` and no logprobs. Porting forward means deleting them and moving the intent into the prompt.
- **Forced tool choice.** Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5 return 400 for `tool_choice` `any`/`tool`; use `auto` plus strict tool use. On OpenAI, `gpt-6-astra` and `gpt-6.1-sol` need the Responses API for tool calling; `gpt-6-luna` supports Chat Completions function calling only at effort `none`.
- **Tokenizer change.** Claude 4.7+ (including Fable 5.2) uses a newer tokenizer: the same text yields roughly **30% more tokens** than Sonnet 4.6 and earlier. Re-baseline cost and context-fit estimates when migrating across that line — a prompt that fit before may not, and a budget forecast built on old counts under-reports by ~30%.
- **Platform and access gaps.** Fable 5.2 on Bedrock is bedrock-runtime only; Mythos is absent from Claude Platform on AWS; Claude Platform on AWS has no fast mode; Foundry has no Batches or Models API; OpenAI models on Google Cloud are private preview only. Details: `references/cloud-availability.md`.

## Cost levers that beat model downgrades

Apply these before dropping a tier — they often deliver a bigger saving with zero accuracy loss.

- **Prompt caching.** Claude cache reads cost **0.025x** base input on Fable 5.x / Mythos 5.x, **0.05x** on Opus 5.5 / Sonnet 5.5, 0.1x elsewhere (incl. Haiku 5.5); a 5-minute cache write costs 1.25x and pays for itself after one hit, a 1-hour write costs 2x and pays off after two. OpenAI cached input is 10x cheaper on `gpt-6-astra` ($1 vs $10) and 20x on `gpt-6.1-sol` / `gpt-6.1-terra`; OpenAI cache writes are billed (Astra $12.50, 1.25x) and 12-hour cache writes cost 2.5x input. Vertex gives a 90% discount on cached Gemini tokens. Any repeated system prompt, tool schema, or document should be cached.
- **Batch.** 50% off input and output on all three vendors (Anthropic Message Batches, OpenAI Batch API, Gemini Batch). Free money for anything not user-facing.
- **Long-context meters differ, and this is a trap.** Claude 4.6+ charges the **same rate across the full 1M window**, except **Haiku 5.5, which steps up 5x above a 100K-token prompt**. OpenAI GPT-6.x charges **2x input / 1.5x output for the whole request above 272K** (`gpt-6-astra` $10/$50 → $20/$75; `gpt-6.1-sol` $2/$10 → $4/$15). Gemini Pro tiers **step up past 200k input** (2.5 Pro $1.25 → $2.50; 3.1 Pro Preview $2.00 → $4.00), while Gemini Flash/Flash-Lite are flat. A huge-context design that is cheap on Claude Sonnet/Opus can be double-priced on OpenAI or Gemini Pro and 5x-priced on Haiku 5.5.
- **Multipliers stack against you.** Claude `inference_geo: "us"` = 1.1x on all token categories; Bedrock (Claude and OpenAI) and Google regional/multi-region endpoints = +10% over global; Vertex priority tier = 1.8x; OpenAI fast = 2x, **Ultrafast ≈ 6x** (`gpt-6-astra`, `gpt-6.1-sol`), regional residency +10% for models released on/after 2026-03-05. Claude fast mode is **GA on Opus 5.5 ($8/$40)** and available on **Fable 5.2 ($16/$80)**; Opus 5 fast is still research preview ($10/$50); **Opus 4.8 fast mode ends 2026-11-30**. Compute the effective rate, not the headline rate.
- **Promotions expire.** `gpt-5.6-sol` is $4/$20 on promo through **2026-11-30** (pricing and model pages; the changelog said "at least through November 21"); list was $5/$30. Do not build a TCO on the promo rate.
- **Tool-use overhead is real but small.** Claude tool definitions add a system-prompt surcharge that varies by model (Opus 5 `auto` 286 tokens vs Opus 4.7's 675, 2026-08-05; no 5.5 figures captured). Server tools bill separately: web search $10/1,000 searches, web fetch free beyond tokens.

## Estimating spend before committing

Give users a number, not a vibe. The estimate needs four inputs and one multiplier pass.

1. **Tokens per unit of work** — input (system + tools + context + user) and output separately. Count with the vendor's token-counting endpoint on a real sample; do not estimate from characters, especially on Claude 4.7+ where the tokenizer shift adds ~30%.
2. **Units per period** — requests/day, or agent turns/session × sessions/day. Agents multiply: one user task can be 20+ model calls.
3. **Cache hit fraction** — what share of input tokens are repeated system prompt, tool schemas, or pinned documents. This is usually the largest single lever.
4. **Batch-eligible fraction** — anything not blocking a human.

Then apply multipliers in order: cache read rate on the cached share, batch 0.5x on the batch share, long-context meter if requests exceed the vendor's threshold (100K prompt on Haiku 5.5, 272K on OpenAI, 200k on Gemini Pro), then residency/priority/fast-mode multipliers.

Anthropic's published worked examples (2026-08-05) anchor the scale: an Opus 5 agent session of 50k input + 15k output tokens costs $0.25 + $0.375 plus $0.08/hour session runtime = **$0.705**; moving 40k of those input tokens to cache reads drops it to **$0.525**. A ~3,700-token support-ticket conversation on Haiku 4.5 runs **~$37 per 10,000 tickets**. If a proposed design lands orders of magnitude above these, the token budget is the problem, not the model choice.

## Facts to establish before recommending

If the user has not stated these, ask — a recommendation made without them is a guess:

- **Latency budget.** Interactive chat, agent background loop, and overnight batch have three different answers. On 2026-08-05 Claude ran Fastest (Haiku) → Fast (Sonnet) → Moderate (Opus) → Slower (Fable); Fable 5.2 is now listed as Moderate, and 5.5-tier labels were not re-captured. Fast mode (Claude) and Fast/Ultrafast (OpenAI) buy latency for 2x–6x the price.
- **Context size per request.** Under 100K keeps Haiku 5.5 on its low tier; under 200k opens the whole catalog including Haiku 4.5 and Gemini 2.5 tiers; above 272K triggers OpenAI's long-context meter.
- **Cutoff sensitivity.** Does the task need facts newer than the model's cutoff, and is retrieval or web search already in the design?
- **Hosting constraint.** First-party, Bedrock (mantle vs runtime), Google Cloud (Google vs Anthropic managed), Foundry (Azure- vs Anthropic-hosted), Claude Platform on AWS, or "must be in EU/US region" — this can eliminate models and features before price matters.
- **Access eligibility.** Mythos 5.2, `gpt-6-cyber` and the Rosalind models require verification or trusted access; do not recommend them to an unverified organization.
- **Volume and burstiness.** Decides whether batch and caching apply, and whether Bedrock's 2M-input-TPM default quota is enough.
- **Existing evals.** If none exist, the honest answer is "start on the mid tier and build an eval" — hand to `evals` — rather than a confident tier pick.

## Non-text modalities

Text-tier reasoning quality does not carry over to audio, image, or video — those are separate model families with separate IDs and radically different unit economics. Pick them independently.

- **All current Claude models** take text and image input and emit text only. No Anthropic audio, image-generation, or video model appears in the catalog — a multimodal-output requirement forces OpenAI or Google (or a specialist vendor) for that leg of the system.
- **Audio/realtime (OpenAI):** `gpt-realtime-2.1` bills audio at $32 in / $64 out per MTok — roughly 8x its own text input rate ($4/$24); `gpt-realtime-2.1-mini` is $10/$20 audio. `gpt-live-1` (GA 2026-09-10) is full-duplex voice at $0.05/min billed per second, backend model billed separately. Transcription runs $0.0045/min (`gpt-transcribe`) to $0.017/min (`gpt-live-transcribe`). Legacy TTS, Whisper and `gpt-4o-*-transcribe` shut down in early 2027. Budget realtime separately.
- **Image generation:** OpenAI `gpt-image-2.6-sunburst` (detail) / `gpt-image-2.6-flare` (fast), released 2026-11-04, bill image tokens at $8 in / $30 out per MTok and add SVG and animated-GIF output; `gpt-image-2` shuts down 2027-02-10. Google's line (2026-08-05) is `gemini-3.1-flash-image` ("Nano Banana 2", ~$0.045–$0.151/image), `gemini-3.1-flash-lite-image`, `gemini-3-pro-image` (4K), and `gemini-2.5-flash-image` ($0.039/image standard, $0.0195 batch). Price per *image*, not per token, when comparing.
- **Video (2026-08-05, not re-verified for OpenAI):** OpenAI Sora 2 at $0.10/sec (720p) and Sora 2 Pro at $0.30–$0.70/sec; Google Veo 3.1 at $0.05–$0.60/sec. Seconds-based billing makes long clips expensive fast.
- **Embeddings:** OpenAI `text-embedding-3-small` $0.02 and `text-embedding-3-large` $0.13 per MTok; Google `gemini-embedding-001` $0.15 text, `gemini-embedding-2-preview` $0.20 text / $0.45 image / $6.50 audio / $12.00 video. Embedding cost is usually noise next to generation cost — optimize recall quality first.
- **Grounding/search is metered on top of tokens.** Claude web search $10/1,000 searches (web fetch free); Gemini Google Search grounding 5,000 free requests/month then $14/1,000 on 3.x models, 1,500 RPD free then $35/1,000 on 2.5; Vertex custom-data grounding $2.50/1,000 prompts.

## Lifecycle and migration

- **Every Claude model ID is a pinned snapshot, including the dateless ones.** From the 4.6 generation on, IDs like `claude-opus-5-5` look evergreen but are fixed releases. Do not assume they auto-upgrade, and do not assume they never retire.
- **Gemini `-latest` suffixes are the opposite: floating pointers.** `gemini-flash-latest` moves under you. Never pin production to `-latest`; pin the snapshot and upgrade deliberately.
- **Notice periods differ by an order of magnitude.** Anthropic: ≥60 days for publicly released models. OpenAI: ≥6 months GA, ≥3 months for specialized variants (Codex, deep research, chat variants), ~2 weeks for previews. Google: ≥2 weeks for preview models. Build the migration budget around the shortest-notice model you depend on.
- **Preview models are a production risk you accept explicitly.** `gemini-3-pro-preview` was shut down 2026-03-09 with migration to `gemini-3.1-pro-preview` — that is the real-world precedent for the 2-week policy. The same applies to OpenAI models on Google Cloud (private preview).
- **An SDK upgrade is a model migration.** The latest Anthropic SDK majors default to API version `2026-10-21`, which turns every sampling parameter into a 400; Bedrock models 4.6 and lower do not support that version at all.
- **Cloud retirement dates are not the vendor's dates.** Anthropic's deprecation page governs Anthropic-operated platforms only (Claude API, Claude Platform on AWS, Microsoft Foundry). **Amazon Bedrock and Google Cloud (Google managed) set their own schedules**; Bedrock's `openai.gpt-6.1-sol` card follows OpenAI's 6-month notice. Check the cloud's page for a workload running there.
- **Audit before you migrate.** Claude Console → Usage → Export gives CSV by API key and model; that is how you find who is still calling a retiring ID. OpenAI notifies affected customers by email plus dashboard notices.
- **Fine-tunes survive their base model's deprecation on OpenAI** — existing fine-tuned models keep serving, but you can no longer create new fine-tunes from that base. Plan re-tuning onto a supported base ahead of shutdown.

Retirement tables, full deprecation history, and replacement mappings: `references/lifecycle-and-deprecations.md`.

## Which platform to run on

First-party API is the default: it is the only surface with the full feature set on every vendor. Choose a cloud when procurement, data residency, or an existing commit forces it — then verify the model and the feature you depend on actually exist there.

- **Amazon Bedrock (Claude):** two endpoints. **bedrock-mantle** (Messages API, `anthropic.`-prefixed IDs such as `anthropic.claude-opus-5-5`) serves the 5.x line except Fable/Mythos 5.2; Opus 5.5, Sonnet 5.5 and Haiku 5.5 are console-gated per account. **bedrock-runtime** (InvokeModel/Converse) is the only path to Fable 5.2 (`global.anthropic.claude-fable-5-2`). Global endpoint no premium, regional +10%; default quota 2M input TPM.
- **Amazon Bedrock (OpenAI):** `openai.<model>` IDs (`openai.gpt-6.1-sol`, `openai.gpt-6.1-terra`, `openai.gpt-6-luna`, `openai.gpt-6-sol`, `openai.gpt-5.6-sol`, `openai.gpt-oss-120b`); no `gpt-6-astra` ID found.
- **Google Cloud (Claude):** **Google managed** (former Vertex page; model in the URL, global/multi-region only for anything newer than Sonnet 4.6, Google-set prices and lifecycle, 30 MB payload cap) or **Anthropic managed** (Claude API IDs, Anthropic-operated, Batch/Files/Models API and fast mode supported, Google Cloud credentials only).
- **Google Cloud (OpenAI):** private preview only for `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-6-luna`.
- **Microsoft Foundry:** Claude Azure-hosted (latest Opus/Sonnet/Haiku) or Anthropic-hosted (everything, incl. Fable/Mythos 5.2); no Batches or Models API. OpenAI GPT-6.x is GA on Azure (`gpt-6.1-sol` 2026-09-29).
- **Claude Platform on AWS:** Anthropic-operated, Claude API IDs, AWS Marketplace CCU billing ($0.01/CCU); no Mythos, no fast mode, no HIPAA readiness.
- **Vertex for Gemini (2026-08-05):** same model IDs as the Gemini API with Vertex-specific tiering (priority 1.8x, flex/batch 0.5x, 90% cached-token discount).

Endpoint types, region lists, auth paths, ID tables and the full gap list: `references/cloud-availability.md`.

## Anti-patterns

- Quoting a price or ID from memory instead of the reference tables or a live fetch. Highest-frequency, highest-damage error in this skill.
- Recommending a retired or retiring model. `claude-opus-4-1-20250805` retired 2026-08-05; `claude-sonnet-4-5-20250929` retires **2026-11-30**. `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-5-pro`, `o3` and `o3-pro` shut down **2026-12-11** (replacements `gpt-6.1-sol` / `gpt-6.1-terra` / `gpt-6-luna`); `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`, `o1`, `o3-mini` passed their 2026-10-23 shutdown; `gpt-5.4-cyber` and the Assistants API are gone.
- Naming a model that does not exist. There is **no verified `gpt-5.6-codex` or `gpt-6-codex`**; OpenAI's named successor to `gpt-5.3-codex` is the general `gpt-6-sol`. Rosalind IDs (`gpt-6-rosalind`, `gpt-rosalind-research`, `gpt-rosalind-discovery`) are verified only on the pricing page — their model pages 404.
- Recommending Mythos 5.2, `gpt-6-cyber` or Rosalind as if orderable. Mythos 5.2 needs Anthropic verification (Cyber Verification Program); `gpt-6-cyber` needs Daybreak Red approval; Rosalind is trusted access only.
- Treating Fable pricing as an Opus alternative without saying so: Fable 5.2 is **2x Opus 5.5** on both input and output (and 4x Sonnet 5.5).
- Budgeting Sonnet 5 at $3/$15. The planned 2026-09-01 increase was **cancelled** on 2026-08-10; $2/$10 is the standard price. Conversely, do not budget `gpt-5.6-sol` at its $4/$20 promo past 2026-11-30.
- Quoting a single `gpt-6-astra` release date. OpenAI's changelog says 2026-09-29; Azure's version string says 2026-09-03. State both.
- Sending `temperature`, forced `tool_choice`, or explicit `thinking` modes to a 5.5 / 5.2 Claude model (or anything on API `2026-10-21`) and blaming the model for the 400.
- Sizing a 1M-context design without checking the per-vendor long-context meter (Haiku 5.5's 100K step, OpenAI's 272K step), and the 30 MB Google managed payload cap.
- Answering "which model" without asking about latency budget, context size, and cutoff sensitivity. Those three eliminate more candidates than price does.

## Reference files

Load on demand — do not read all of them for a single-model question.

- `references/claude-catalog.md` — Read for any Anthropic question: Fable 5.2 / Mythos 5.2 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 and previous-generation IDs across API/Bedrock/Google Cloud, full pricing incl. cache write/read and batch rates, per-model 400s, fast-mode table, API version `2026-10-21` breaks, worked cost examples.
- `references/openai-catalog.md` — Read for any OpenAI question: GPT-6.x tier table and constraints, Decisions API, long-context meter, full pricing incl. GPT-5.x and the `gpt-5.6-sol` promo, Ultrafast, specialist models (cyber, Rosalind), realtime/image/transcription/embedding families, gpt-oss.
- `references/gemini-catalog.md` — Read for any Google question (2026-08-05 snapshot): Gemini 3.x and 2.5 model IDs (stable vs preview), per-model limits and thinking support, AI Studio paid-tier and Vertex pricing tables, tier-selection heuristics, image/embedding families.
- `references/lifecycle-and-deprecations.md` — Read when the question is about retirement dates, notice periods, migration targets, `-latest` vs pinned IDs, or auditing usage of a dying model.
- `references/cloud-availability.md` — Read when the workload runs on Bedrock (mantle or runtime), Google Cloud (Google or Anthropic managed), Claude Platform on AWS, or Microsoft Foundry, for OpenAI models on those clouds, or when a feature might not exist off the first-party API.

## Diagnostic scripts

- `scripts/list-claude-models.sh` — Read-only `GET /v1/models` against the Claude API using `ANTHROPIC_API_KEY`; prints IDs, display names, and per-model limits actually available to the caller's org. Run this instead of trusting the tables when the answer must be exact.

## Sources

- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/api/migration-2026-10-21
- https://platform.claude.com/docs/en/build-with-claude/fast-mode
- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
- https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
- https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
- https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/pricing.md
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/deprecations
- https://developers.openai.com/api/docs/guides/decisions
- https://developers.openai.com/api/docs/guides/model-selection (2026-08-05)
- https://ai.google.dev/gemini-api/docs/models (2026-08-05)
- https://ai.google.dev/gemini-api/docs/latest-model (2026-08-05)
- https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro (2026-08-05)
- https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash (2026-08-05)
- https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview (2026-08-05)
- https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-preview (2026-08-05)
- https://ai.google.dev/gemini-api/docs/pricing (2026-08-05)
- https://cloud.google.com/vertex-ai/generative-ai/pricing (2026-08-05)

Fetched: 2026-11-13 (Anthropic and OpenAI); Gemini sources last fetched 2026-08-05
