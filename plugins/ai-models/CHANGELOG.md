# Changelog

## 1.0.1 — 2026-11-13

- Refresh the Jev catalog identity from `jev-1.13.0` to `jev-1.14.0`: `jev-latest` and `jev-preview` both resolve to 1.14.0 per the official models page; add Box (beta) and image inputs, keep default 64k/32k context with the opt-in 262k header.
- Replace the `jev-1-13-0.md` version reference with `jev-1-14-0.md` (1.13 differences are in its changelog section); update `jev-system-one` lifecycle guidance to pin versions rather than rely on aliases.
- Move catalog `as_of` to 2026-11-13 (only the Jev row was re-retrieved; other rows keep 2026-10-16).

## 1.0.0 — 2026-10-16

- Add a source-traced, popularity-weighted catalog of 60 model identities, grouped into model-family skills with individual model references.
- Include frontier, reasoning, coding, open-weight and specialist decision-model coverage, including TypeSafe Jev.
- Add a specialist agent, trigger-eval cases, selection methodology and deterministic catalog validation.
