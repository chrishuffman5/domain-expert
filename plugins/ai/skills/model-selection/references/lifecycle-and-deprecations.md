# Model lifecycle, deprecation, and retirement (Anthropic/OpenAI as of 2026-11-13; Google as of 2026-08-05)

Read when the question is about retirement dates, notice periods, migration targets, pinned vs floating model IDs, or auditing usage of a dying model. All dates below are snapshots: re-verify against the source URLs.

## Anthropic: policy and lifecycle terms

> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations (policy text fetched 2026-08-05; unchanged in the 2026-11-13 pass)

Lifecycle states:

- **Active**: fully supported and recommended.
- **Legacy**: no longer receives updates; may be deprecated in future.
- **Deprecated**: still functional but not recommended; Anthropic assigns a recommended replacement and a retirement date.
- **Retired**: no longer available; requests fail.

**Notice period:** at least **60 days** before retirement for publicly released models, delivered by email to customers with active deployments plus documentation updates.

**Scope caveat:** dates on Anthropic's deprecations page apply to **Anthropic-operated platforms only**: Claude API, Claude Platform on AWS, Microsoft Foundry (and Google Cloud Anthropic managed, which is Anthropic-operated; its lifecycle was not stated explicitly in the corpus). **Amazon Bedrock and Google Cloud (Google managed) set their own retirement schedules**, which can differ.

**Auditing usage:** Claude Console → Usage → Export produces a CSV broken down by API key and model: use it to find deprecated-model traffic before retirement.

Anthropic has committed to long-term preservation of model weights ("Commitments on Model Deprecation and Preservation"), with stated intent to eventually make past models available again.

### Current model status

> Source: https://platform.claude.com/docs/en/about-claude/model-deprecations and https://platform.claude.com/docs/en/release-notes/overview (fetched 2026-11-13)

| API model name | State | Deprecated | Tentative retirement |
|---|---|---|---|
| `claude-fable-5-2` / `claude-mythos-5-2` | Active (Mythos: verification required) | N/A | Not sooner than November 9, 2027 |
| `claude-fable-5-1` / `claude-mythos-5-1` | Active | N/A | Not sooner than September 1, 2027 |
| `claude-fable-5` / `claude-mythos-5` | Active | N/A | Not sooner than June 9, 2027 |
| `claude-opus-5-5` | Active | N/A | Not sooner than September 22, 2027 |
| `claude-opus-5` | Active | N/A | Not sooner than July 24, 2027 |
| `claude-opus-4-8` | Active (**fast mode** deprecated 2026-10-30, removed **2026-11-30**) | N/A | Not sooner than May 28, 2027 |
| `claude-opus-4-7` | Active | N/A | Not sooner than April 16, 2027 |
| `claude-opus-4-6` | Active | N/A | Not sooner than February 5, 2027 |
| `claude-opus-4-5-20251101` | Active | N/A | Not sooner than November 24, 2026 |
| `claude-opus-4-1-20250805` | **Retired** (Claude API) | June 5, 2026 | August 5, 2026 |
| `claude-opus-4-20250514` | **Retired** | April 14, 2026 | June 15, 2026 |
| `claude-sonnet-5-5` | Active | N/A | Not sooner than September 28, 2027 |
| `claude-sonnet-5` | Active | N/A | Not sooner than June 30, 2027 |
| `claude-sonnet-4-6` | Active | N/A | Not sooner than February 17, 2027 |
| `claude-sonnet-4-5-20250929` | **Deprecated** | September 30, 2026 | **November 30, 2026** |
| `claude-sonnet-4-20250514` | **Retired** | April 14, 2026 | June 15, 2026 |
| `claude-haiku-5-5` | Active | N/A | Not sooner than October 7, 2027 |
| `claude-haiku-4-5-20251001` | Active | N/A | Not sooner than October 15, 2026 (date passed; no deprecation announced as of 2026-11-13) |
| `claude-mythos-preview` | Deprecated | June 9, 2026 | Retirement date not captured; 2026-08-05 replacement `claude-mythos-5` |

Retired before 2026-08-05 and unchanged: `claude-3-7-sonnet-20250219`, `claude-3-5-haiku-20241022` (both Feb 19, 2026), `claude-3-haiku-20240307` (Apr 20, 2026).

`claude-opus-4-1-20250805` retired on the Claude API on 2026-08-05; the models overview still lists it on Bedrock and Google managed, and researchers can reach it through the External Researcher Access Program.

**Near-term cluster:** `claude-sonnet-4-5-20250929` retires **2026-11-30**; Opus 4.8 fast mode ends **2026-11-30**; `claude-opus-4-5-20251101` reaches its "not sooner than" date on 2026-11-24; `claude-haiku-4-5-20251001` is already past its date. Anything pinned to these needs a migration plan now.

### Deprecation history and replacements

| Retirement date | Deprecated model / feature | Replacement |
|---|---|---|
| Nov 30, 2026 | `claude-sonnet-4-5-20250929` | `claude-sonnet-5-5` |
| Nov 30, 2026 | Opus 4.8 fast mode (`speed:"fast"`) | Opus 5.5 fast mode |
| Aug 5, 2026 | `claude-opus-4-1-20250805` | `claude-opus-4-8` (release notes recommend Opus 5) |
| Jun 15, 2026 | `claude-sonnet-4-20250514` | `claude-sonnet-4-6` |
| Jun 15, 2026 | `claude-opus-4-20250514` | `claude-opus-4-8` |
| Apr 20, 2026 | `claude-3-haiku-20240307` | `claude-haiku-4-5-20251001` |
| Feb 19, 2026 | `claude-3-5-haiku-20241022` | `claude-haiku-4-5-20251001` |
| Feb 19, 2026 | `claude-3-7-sonnet-20250219` | `claude-sonnet-4-6` |
| Jan 5, 2026 | `claude-3-opus-20240229` | `claude-opus-4-8` |
| Oct 28, 2025 | `claude-3-5-sonnet-20240620`, `claude-3-5-sonnet-20241022` | `claude-sonnet-4-6` |
| Jul 21, 2025 | `claude-2.0`, `claude-2.1`, `claude-3-sonnet-20240229` | `claude-opus-4-8` / `claude-sonnet-4-6` |
| Nov 6, 2024 | `claude-1.x`, `claude-instant-1.x` | `claude-haiku-4-5-20251001` |

### Deprecated API parameters and version breaks

> Source: https://platform.claude.com/docs/en/api/migration-2026-10-21 (fetched 2026-11-13; breaking-changes section read in full)

- On API version **`2026-10-21`** (default in the latest SDK majors), `temperature`, `top_p` and `top_k` return **400 on every model, even at default values**. Under `2023-06-01` they already returned 400 for non-default values on Opus 4.7+ (2026-08-05), and Fable 5.2 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 reject them regardless. Keep requests that genuinely need a lower temperature (e.g. Sonnet 4.6) on `2023-06-01`; otherwise move the intent into the prompt.
- Also on `2026-10-21`: `document` blocks directly in assistant messages → 400; `citations` on user-message text blocks → 400.
- **Bedrock:** models 4.6 and lower do not support `2026-10-21`; pin the older SDK major.
- Upgrading the SDK major silently moves you to `2026-10-21`: treat an SDK bump as a model-behavior migration and re-run evals.

## OpenAI: policy and shutdown schedule

> Source: https://developers.openai.com/api/docs/deprecations (fetched 2026-11-13)

Terminology: "deprecation" is the retirement process itself. Once announced, a model is immediately deprecated and assigned a **shutdown date**; at shutdown it becomes inaccessible. OpenAI distinguishes **deprecated** (in the retirement pipeline) from **legacy** (no longer updated, will eventually be deprecated).

**Minimum notice periods** (re-confirmed 2026-11-13):

- **Generally available models**: at least **6 months**.
- **Specialized variants** (chat variants, Codex models, deep research versions): at least **3 months**.
- **Preview models**: about **2 weeks**.
- Safety or compliance concerns can accelerate any of these.

**Announcement channels:** direct email to affected customers, documentation updates, blog posts for major changes, and dashboard notifications.

**Fine-tuned models:** a fine-tune built on a deprecated base is **not** affected by that base's deprecation and keeps serving, but you can no longer create *new* fine-tunes from the deprecated base.

### Upcoming shutdowns (2027)

| Shutdown date | Notice | Models affected | Recommended replacement |
|---|---|---|---|
| April 1, 2027 | 2026-10-01 | `gpt-5.3-codex`, `gpt-5.1` | `gpt-6-sol` |
| April 1, 2027 | 2026-10-01 | `gpt-5.4-nano` | `gpt-6-luna` |
| February 26, 2027 | 2026-08-26 | `whisper-1`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize`; endpoint `/v1/audio/translations` | Endpoint → `/v1/realtime/translations`; model replacement not stated in the corpus |
| February 10, 2027 | 2026-11-10 | `gpt-image-2`, `gpt-image-2-2026-04-21` | `gpt-image-2.6-sunburst` or `gpt-image-2.6-flare` |
| February 1, 2027 | 2026-11-05 | `gpt-5.5-cyber-preview` | not stated |
| January 20, 2027 | 2026-07-20 | `gpt-realtime`, `gpt-audio`, `gpt-4o-audio` / `gpt-4o-realtime`, `gpt-realtime-mini`, `gpt-audio-mini`, `gpt-4o-mini-audio` / `gpt-4o-mini-realtime`; `gpt-4o-mini-transcribe-2025-03-20` | `gpt-realtime-2.1`, `gpt-audio-1.5` (2026-08-05 mapping, not re-captured) |
| January 14, 2027 | 2026-10-14 | `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini` dated snapshots | `gpt-6-luna` |
| January 6, 2027 | 2026-10-01 | `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts` | `gpt-realtime-2.1-mini` |

### 2026 shutdowns

| Shutdown date | Notice | Models affected | Recommended replacement |
|---|---|---|---|
| **December 11, 2026** (confirmed) | 2026-06-11 | `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-5-pro`, `o3`, `o3-pro` | `gpt-5` / `o3` / `gpt-5-pro` / `o3-pro` → **`gpt-6.1-sol`**; `gpt-5-mini` → **`gpt-6.1-terra`**; `gpt-5-nano` → **`gpt-6-luna`** (the 2026-08-05 snapshot said `gpt-5.6-sol`: changed) |
| December 1, 2026 | — | Older GPT Image models | Newer image models (2026-08-05 entry; not re-verified) |
| October 23, 2026 (date passed) | 2026-04-22 | `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`, `gpt-4-1106-preview`, `gpt-4.1-nano`, `gpt-4o-2024-05-13`, `o1`, `o1-pro`, `o3-mini` | `gpt-5.6-terra` / `-sol` / `-luna`. Filed under "Past deprecations"; the page gives no post-shutdown confirmation, so **treat as retired** |

### Retired

- **`gpt-5.4-cyber`**: shut down **2026-10-01** (notice 2026-09-11).
- **Assistants API**: shut down **2026-08-26**.

### Not deprecated (as of 2026-11-13)

`gpt-5.5`, `gpt-5.5-pro`, `gpt-5.4`, `gpt-5.4-pro`, `gpt-5.6-sol/terra/luna`, `gpt-oss-120b`, `gpt-oss-20b` have no deprecation row; `gpt-6-sol` is superseded by `gpt-6.1-sol` but not deprecated. The `gpt-5.6-sol` $4/$20 promo ends 2026-11-30 (pricing and model pages; the changelog said "at least through November 21"): that is a price change, not a deprecation.

## Google: preview lifecycle (2026-08-05, not re-verified)

> Source: https://ai.google.dev/gemini-api/docs/models (fetched 2026-08-05)

- **Stable** models point to a specific snapshot and generally do not change under you.
- **Preview** models may be used in production but can be deprecated with **at least 2 weeks' notice**.
- **Experimental** models are not for production.
- **`-latest`** suffixes are floating pointers to the newest release in a family, not pinned snapshots.

**Concrete precedent:** `gemini-3-pro-preview` **was shut down March 9, 2026**, with migration guidance pointing to `gemini-3.1-pro-preview`. Since `gemini-3.1-pro-preview` is itself a preview and is the only Pro-tier option in the 3.x line, any Gemini Pro dependency carries 2-week-notice risk.

Retirement dates for Claude models on Google Cloud (Google managed) are set by **Google**, not Anthropic.

## Migration rules of thumb

- Pin production to snapshot IDs, never to floating pointers; upgrade deliberately behind an eval gate.
- Budget migration windows against the **shortest** notice period in your dependency set: one preview model drags the whole system to 2 weeks.
- Re-run evals on the replacement before switching; replacement recommendations are the vendor's, not a guarantee of behavioral parity.
- Re-baseline token counts and cost when crossing the Claude 4.7 tokenizer boundary (~30% more tokens for the same text).
- Strip `temperature`/`top_p`/`top_k` everywhere before adopting API version `2026-10-21` or any 5.5 / 5.2 Claude model; also drop forced `tool_choice` and explicit `thinking` enabled/disabled on those models.
- Moving off `gpt-5` / `o3` before 2026-12-11: `gpt-6.1-sol` has no `none` effort and needs the Responses API for tool calling; budget for that, not just a model-string swap.
- On OpenAI, plan re-tuning onto a supported base before a base model's shutdown, since new fine-tunes on a deprecated base are blocked.

## Sources

- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/api/migration-2026-10-21
- https://developers.openai.com/api/docs/deprecations
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/pricing.md
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://ai.google.dev/gemini-api/docs/models (2026-08-05)
- https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-preview (2026-08-05)

Fetched: 2026-11-13 (Google section 2026-08-05)
