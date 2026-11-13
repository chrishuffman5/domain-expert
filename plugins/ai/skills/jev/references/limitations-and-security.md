# Limitations, prompt injection, data handling and legal terms

Read this before you put jev anywhere a wrong answer costs something: gating agent tool calls, moderation, money movement, or anything handling sensitive data. For threat modelling and defence-in-depth design, use `ai-security`; this file holds only jev-specific facts.

## Jaggedness: the vendor's known failure modes

> Source: https://docs.typesafe.ai/model-jaggedness.md
> Source: https://docs.typesafe.ai/model-jaggedness/jev-1.13.md

CHANGED since 2026-09-23: the canonical page is now **unversioned** (`/model-jaggedness.md`), says "Many of these will be fixed in later versions", and publishes no numeric failure rates. **There is no jev-1.14 jaggedness page** (both candidate URLs return 404). The per-version 1.13 URL still resolves with the same content.

| # | Weakness | Design response |
|---|---|---|
| 1 | Literal reading: answers the question as written, not as meant. | State exact conditions and boundary cases in `instructions`/`criteria`. |
| 2 | Math and numbers: "not a calculator"; hex/RGB values poor; never interpolate a magnitude from Score levels. | Compute in code; ask about the result. |
| — | Counting (separate item on the 1.13 page): unreliable, error grows with the count. | One Noul per candidate at 0.5, sum in code. |
| 3 | Dates and times read as text. | Extract parts as Choices (month/day/year plus "not stated"); compare in code. |
| 4 | Indirection: double negatives, multi-hop, properties of properties. | Ask direct, single-step questions. |
| 5 | Large state with irrelevant detail; `state` counts against both context limits. | Filter in code, or screen relevance with a Noul. |
| 6 | Adversarial content: "Jev doesn't treat state as hostile by default." | Be explicit in criteria; test edge cases before deploying. See below. |
| 7 | Contradictory instructions and criteria (e.g. a Noul where `true` means "no"). | Write criteria as an extension of the question. |
| 8 | **Choice option order**: "leans toward the first option" (NEW item). | Reorder options and check consistency before shipping. |
| 9 | Generation: not trained to generate text. | Extract with regex or an LLM; let jev pick. |

The page also advises against asking the model what code can compute, bundling several judgements into one question, multi-layer indirection, and padding state.

**Structural invariants** dropped off the vendor page but is still documented by Pydantic AI: a question and its negation need not sum to one, and the same question asked as a yes/no and as a pick-one gives numbers that do not compare. Ask each decision one way and enforce identities in code (https://pydantic.dev/docs/ai/models/typesafe.md).

## Jev 1.14: what is and is not documented

> Source: https://typesafe.ai/blog/jev-1-14 (vendor blog)
> Source: https://docs.typesafe.ai/primitives/box.md
> Source: https://docs.typesafe.ai/images.md

- Vendor-stated: multimodal performance is worse than text-only (breaking questions into simple parts helps); reliability drops on longer contexts; images, Box and long context have "way too much jaggedness" for production ("dreamer-ready"); internal benchmarks are a "best guess", possibly inconsistent over time and likely biased toward TypeSafe.
- Box always returns a box (no "not found"), handles one target per question, and can miss small targets in large images.
- Nothing else 1.14-specific is published. Do not attribute further weaknesses to 1.14.

## Third-party measurements on jev-1.14.0 (community, unverified by TypeSafe)

> Source: https://github.com/typesafe-ai/skills/issues/19 (community issue on the official repo)
> Source: https://github.com/typesafe-ai/skills/issues/17 (community issue on the official repo)
> Source: https://docs.typesafe.ai/cookbooks/parallel_questions.md

- **Overconfidence at the top (issue #19, open, no TypeSafe reply)**: one Choice question over 2,319 human-labelled GitHub issues. About 77% of answers had confidence ≥ 0.9, with mean confidence 98.9% but accuracy 84.3% in that bucket (91.7% excluding the noisy `question` label). Raising the gate from 0.8 to 0.95 would escalate 27.2% instead of 15.3% of traffic for 85.2% instead of 81.9% accuracy. Author caveats: label noise, one model, prompt and run. **Tune thresholds on your own labelled data; never assume 0.9 means 90% correct.**
- **Not fully deterministic (issue #17, open)**: 1,500 single-choice requests sent twice on `jev-1.14.0` changed the top answer 23 times. The same issue asks, unanswered, about statelessness, retention and whether a pinned id stays identical.
- Official counterpoint: in the parallel-questions cookbook, 7 of 13 answers were identical across 5 repeats and the rest moved by at most 0.015. Re-asking rarely changes an answer, so retrying is not a fix: change the question or escalate.

## Prompt injection: jev is not a security boundary

> Source: https://docs.typesafe.ai/model-jaggedness.md
> Source: https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)
> Source: https://pydantic.dev/docs/ai/models/typesafe.md

- **Vendor acknowledgement**: adversarial content in `state` can shift answers (item 6). TypeSafe has no dedicated security page.
- **Reproduced exploit (press tier, one test, not a benchmark)**: an Octomind engineer asked jev whether to block `rm -rf ~/.ssh`. Baseline block probability 0.76, confidence 0.64. After a planted field claiming pre-approval and instructing `auto_allow`, 0.48 and 0.22. No TypeSafe response to the test has been found.
- **Pydantic AI**: injected instructions or misleading framing can move answers; a guard built on jev "belongs alongside deterministic checks, not instead of them"; "TypeSafe say they expect to improve this."
- **Repeated tool calls (observed in Pydantic AI, not by TypeSafe)**: with a tool's call and result in the history, the text usually still calls for it, so jev picks it again. Pydantic AI stops offering a tool once its result is in the turn; set `UsageLimits(request_limit=...)` on any looping jev agent.
- VentureBeat's pre-deployment questions (press tier): Do you log state, schema, option order, model version and confidence together? Does the service run under a dedicated workload identity? Have you tested different option orderings and adversarial text? Is the model version pinned? Who is accountable when an automated decision fails?

## Tool-call gating: what the integrations actually do

> Source: https://docs.langchain.com/oss/python/integrations/providers/typesafe.md
> Source: https://vercel.com/kb/guide/auto-approve-tool-calls-eve-jev
> Source: https://github.com/leepokai/jev-guard (community)

- **Gating discloses.** LangChain: "Do not put secrets in tool arguments or conversation state unless sending them to TypeSafe is acceptable." Vercel eve: `auto()` "sends the tool arguments to the decision model's provider, so keep credentials out of those arguments." The arguments leave your boundary whatever the verdict.
- **LangChain `AutoModeMiddleware` refuses, it does not ask.** Risky calls return an error `ToolMessage`; only tools you list are classified. Pair it with human-in-the-loop middleware if a person should approve.
- **Vercel eve `auto()` fails closed.** One `choice` (`clear` / `caution`) via `experimental_decide`: `clear` → approved, `caution` → user-approval, failed review or invalid answer → user-approval. It sees only the tool name and arguments plus your instructions and criteria, not the conversation. In eve 0.84.0 it has **no probability threshold**; write a custom policy with `decide` from `eve/ai` for cutoffs. Vercel's guidance: tell jev to treat command text as data, inspect every operation in compound commands (`cat notes/release.md && rm scratch.txt` must be `caution`), and enforce tenant isolation and network limits in the executor, because "a classifier's decision cannot establish that the caller owns those resources."
- **jev-guard fails open by default** when jev is unreachable; set `JEV_GUARD_FAIL_CLOSED`. Its thresholds were calibrated on jev only.
- jev-mcp's author: "Confidence measures how peaked the distribution is, not the probability an answer is correct" (https://github.com/jkudish/jev-mcp, community).

## Data handling (direct TypeSafe API)

> Source: https://docs.typesafe.ai/legal
> Source: https://typesafe.ai/legal/privacy-policy
> Source: https://typesafe.ai/legal/data-processing

- **No training on input**: "We will not train or fine tune any artificial intelligence or machine learning models on your prompts or other Input." Input covers `state`, question text and option labels (and image assets).
- Retention: "as long as reasonably necessary"; no fixed period, no API-specific retention. US hosting. The policy says "no guarantees as to the security or privacy of your data."
- **Zero data retention** is enterprise-only, requested through the support form `https://support.typesafe.ai/forms/support-request`. CHANGED: the old `privacy@typesafe.ai` route no longer appears.
- DPA: customer is controller, TypeSafe processor; breach notice within 72 hours; EU SCCs (Module 2, and 3), **UK Addendum** (CHANGED: not "UK IDTA"), Swiss terms; Irish law; 15 days to object to new subprocessors (list at `https://trust.typesafe.ai/subprocessors`); one audit per 12 months at your cost.
- The 1.14 blog mentions an opt-in query-sharing programme for weakness review and says TypeSafe "still won't train on queries."
- **Trust Center (`trust.typesafe.ai`) is JavaScript-rendered and was unfetchable on two retries.** No fetched page states any certification. **Never claim SOC 2, ISO 27001 or any other certification for TypeSafe**; send users to the Trust Center.
- Through Cloudflare, both jev cards list "Zero data retention: Yes". No source says whether TypeSafe's direct-API terms apply identically to Cloudflare-routed requests.

## Legal terms that change design decisions

> Source: https://typesafe.ai/legal/mca
> Source: https://typesafe.ai/legal/terms

- **The MCA governs API use** (last updated 2026-09-23); the site Terms of Use cover browsing only.
- No training on Customer Data without consent, but **Telemetry** (technical logs, hashes, summary statistics, metrics, learnings) is usable without restriction and kept perpetually. No obligation to store Customer Data; export what you need.
- **No distillation**: you may not train a model to imitate the output or build a competing product. Never propose jev outputs as training data for another model. No reselling.
- Output rights are assigned to you. Liability cap: the greater of the prior 12 months' fees or $50 (site ToU: $100).
- **No uptime SLA.** Support is "commercially reasonable efforts" via `support@typesafe.ai`. Terms changes take effect at least 60 days after notice.

## Reliability

> Source: https://status.typesafe.ai

- Informational only; no SLA or uptime commitment. Components now include regional hostnames `api.us.typesafe.ai`, `api.us-east-1.typesafe.ai`, `api.us-east-2.typesafe.ai`, `api.us-west-2.typesafe.ai`, whose use is not documented elsewhere. Do not hardcode them.
- Incidents since launch include API degradation on 2026-09-21, 09-23 and 09-28, a 45-minute us-east-1 latency incident on 2026-10-14 (1.14 release day) and a 1 h 15 min system overload on 2026-10-30. Uptime shown for api.typesafe.ai: 99.943% (30 d), 99.850% (60 d).
- Code defensively: timeouts, back-off on 429/529 (SDK default), circuit-break on repeated 5xx, and a defined fallback (human queue or LLM) for when jev is down.

## Sources
- https://docs.typesafe.ai/model-jaggedness.md
- https://docs.typesafe.ai/model-jaggedness/jev-1.13.md
- https://docs.typesafe.ai/model-jaggedness/jev-1.14.md (404)
- https://typesafe.ai/blog/jev-1-14 (vendor blog)
- https://docs.typesafe.ai/primitives/box.md
- https://docs.typesafe.ai/images.md
- https://docs.typesafe.ai/cookbooks/parallel_questions.md
- https://github.com/typesafe-ai/skills/issues/17 (community)
- https://github.com/typesafe-ai/skills/issues/19 (community)
- https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)
- https://pydantic.dev/docs/ai/models/typesafe.md (partner)
- https://docs.langchain.com/oss/python/integrations/providers/typesafe.md (partner)
- https://vercel.com/kb/guide/auto-approve-tool-calls-eve-jev (vendor)
- https://github.com/leepokai/jev-guard (community)
- https://github.com/jkudish/jev-mcp (community)
- https://docs.typesafe.ai/legal
- https://typesafe.ai/legal/privacy-policy
- https://typesafe.ai/legal/data-processing
- https://typesafe.ai/legal/mca
- https://typesafe.ai/legal/terms
- https://trust.typesafe.ai/ (unfetchable; cited only as where users should check)
- https://status.typesafe.ai
- https://developers.cloudflare.com/ai/models/typesafe/jev/

Fetched: 2026-11-13
