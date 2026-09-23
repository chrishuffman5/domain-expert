# Architectural patterns for building with jev

Read this when you are designing where jev sits in an application: fan-out, routing, gating or composite ranking. All four named patterns come from TypeSafe's docs. The hybrid LLM patterns come from the official smart-home demo.

## Governing principle

> Source: https://docs.typesafe.ai/concepts/how-to-build-with-system-one.md

"Keep code in control; use AI only for narrow, structured decisions."
- Control flow stays in application code, and jev answers atomic sub-decisions inside it. Compare an LLM agent, which self-directs and compounds error with every loop.
- **Decompose**: replace one "Is this spam?" with about 6 independent Nouls (credential request, sender mismatch, unexpected reward, and so on) and recombine them in code.
- **Minimal context**: include only what the decision needs. Pull current facts from your own knowledge base rather than relying on model weights.
- **Parallel independence**: questions in one request do not share hidden context.
- Vendor latency claim: "most queries complete in ~100ms".

## Speculative fan-out

> Source: https://docs.typesafe.ai/patterns/fan-out.md
> Source: https://docs.typesafe.ai/demos/smart-home.md

Put every question you *might* need into one call, then let code read only the relevant answers. Questions run in parallel, so extra questions barely change latency. Example: support triage asks for the category plus severity and reproducibility (relevant only if it is a bug) plus refund and frustration signals, all in one request. This replaces a sequential classify-then-follow-up chain.

## Confidence-gated routing

> Source: https://docs.typesafe.ai/patterns/confidence-routing.md

"The answer tells you what; confidence tells you whether to act." Set one low floor and layer action-specific bars above it. Voice-banking example:
- confidence < 0.6 → human support
- `check_balance` at ≥ 0.6 → execute (low stakes)
- `transfer` at 0.6–0.85 → ask the user to confirm
- `transfer` at > 0.85 → execute automatically

## Composite scoring

> Source: https://docs.typesafe.ai/patterns/composite-scoring.md

Use one Score per dimension, normalize each to 0–1 (`score / (len(criteria)-1)`) and weight in code. Resume example with four dimensions scored 0–4:
- Senior IC weights: 40% Python, 40% system design, 10% leadership, 10% generalist.
- Engineering Manager weights: 40% leadership, 25% generalist, 20% system design, 15% Python.

Re-weighting needs no new model calls.

## Intent routing

> Source: https://docs.typesafe.ai/patterns/intent-routing.md

Classify cheaply first, then spend expensive resources only where they are needed. Per message, ask a Choice for intent and a Score for complexity in parallel:
- confidence < 0.5 → human
- `order_status` → a deterministic DB lookup, with no LLM
- `product_question` / `return_exchange` → specialist LLMs
- `complaint` → routed further by complexity

## Hybrid with a generative LLM

> Source: https://docs.typesafe.ai/demos/smart-home.md
> Source: https://flaviocopes.com/jev/ (community)

jev never writes text. When the output needs prose, code or a decomposition, hand that step to an LLM:
- **Request decomposition**: a Choice flags a compound request. An LLM splits it, and each part goes back through jev.
- **Fallback conversation**: when jev decides structured evaluation does not fit, fall back to a chat LLM.
- Community framing: "Jev decides, the LLM writes."

## Agent-assisted adoption (TypeSafe's own coding-agent skill)

> Source: https://docs.typesafe.ai/agent-skill.md

TypeSafe ships an agent skill for Claude Code, Codex and "other agent environments":
- Claude Code: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`. Invoke with `/typesafe:typesafe-ai`.
- Other agents: `npx skills add typesafe-ai/skills --skill typesafe-ai` (`-g` installs globally).
- Manual: copy `skills/typesafe-ai`.

Its documented workflows:
- **Discovery**: find regex or keyword-matching code that a jev call could replace.
- **Experimentation**: run test queries on real data and refine `instructions`/`criteria`.
- **Pattern matching**: refactor code toward the cookbook patterns.

Directives from the same page:
- Keep all questions and thresholds in one reviewed place.
- Review the question and criteria wording an agent proposes. Do not accept it blindly.
- When routing misbehaves, check thresholds first.
- Keep the skill updated. Stale references cause "field hallucinations".

## Sources
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one.md
- https://docs.typesafe.ai/patterns.md
- https://docs.typesafe.ai/patterns/fan-out.md
- https://docs.typesafe.ai/patterns/confidence-routing.md
- https://docs.typesafe.ai/patterns/composite-scoring.md
- https://docs.typesafe.ai/patterns/intent-routing.md
- https://docs.typesafe.ai/demos/smart-home.md
- https://docs.typesafe.ai/agent-skill.md
- https://flaviocopes.com/jev/ (community)

Fetched: 2026-09-23
