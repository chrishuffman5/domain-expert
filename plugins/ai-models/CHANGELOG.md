# Changelog

## 1.1.0 — 2026-11-13

- Raise the catalog from 60 to 63 model identities: add `claude-fable-5-2` (released 2026-11-09, $8/$40), `gpt-6.1-terra` (2026-10-26, $1/$5) and `gpt-6-sol` (2026-09-22, missing from the 1.0.0 snapshot). `validate_catalog.py` and its regression test now expect 63 rows; evidence split is 5 observed / 19 proxy / 39 unknown.
- Re-verify every Claude, GPT and gpt-oss row against first-party docs and cloud catalogs (`retrieved` 2026-11-13). Fable 5.1 is now superseded but still Active; Sonnet 5.5 cache read is $0.10 and its release date is 2026-09-28; Haiku 5.5's release date is 2026-10-07; Opus 5.5 fast mode is GA. GPT rows now carry current pricing-page rates, including the gpt-5.6-sol $4/$20 promotion through 2026-11-30 (the changelog said "at least through November 21") and the Ultrafast tier. The gpt-6-astra release date conflict (OpenAI 2026-09-29 vs Azure 2026-09-03) is kept visible.
- Add version references `claude-fable-5-2.md`, `gpt-6-sol.md` and `gpt-6-1-terra.md`, and regenerate the other Claude, GPT and gpt-oss references with platform IDs, lifecycle dates and per-section sources.
- `claude` skill: Fable 5.2 guidance, limited-access Mythos 5.2/5.1 notes, API version `2026-10-21` sampling-parameter removal, a deprecation/replacement table (Sonnet 4.5 retires 2026-11-30, Opus 4.8 fast mode removed 2026-11-30) and per-cloud model IDs. `gpt` skill: GPT-6.1 Terra and GPT-6 Sol routing, Decisions API, specialist/limited-access models (cyber, Rosalind, image 2.5/2.6, live/realtime/transcribe) without catalog rows, the shutdown table with current replacements, and cloud availability. `gpt-oss` skill: no new gpt-oss release; Bedrock/Foundry routes noted.
- Update the `claude` positive trigger eval for Fable 5.2.

## 1.0.1 — 2026-11-13

- Refresh the Jev catalog identity from `jev-1.13.0` to `jev-1.14.0`: `jev-latest` and `jev-preview` both resolve to 1.14.0 per the official models page; add Box (beta) and image inputs, keep default 64k/32k context with the opt-in 262k header.
- Replace the `jev-1-13-0.md` version reference with `jev-1-14-0.md` (1.13 differences are in its changelog section); update `jev-system-one` lifecycle guidance to pin versions rather than rely on aliases.
- Move catalog `as_of` to 2026-11-13 (only the Jev row was re-retrieved; other rows keep 2026-10-16).

## 1.0.0 — 2026-10-16

- Add a source-traced, popularity-weighted catalog of 60 model identities, grouped into model-family skills with individual model references.
- Include frontier, reasoning, coding, open-weight and specialist decision-model coverage, including TypeSafe Jev.
- Add a specialist agent, trigger-eval cases, selection methodology and deterministic catalog validation.
