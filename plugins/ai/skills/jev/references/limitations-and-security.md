# Limitations, prompt injection, data handling and legal terms

Read this before you put jev in any path where a wrong answer costs something: gating agent tool calls, security screening, money movement, or anything that handles sensitive data. It also covers designing around the jev-1.13 weaknesses.

## Jev 1.13 "jaggedness": the vendor's known failure modes

> Source: https://docs.typesafe.ai/model-jaggedness/jev-1.13.md (last reviewed 2026-09-17)

| # | Weakness | Design response |
|---|---|---|
| 1 | Literal interpretation: it "answers the question you wrote, not the one you meant". Scoping words and negations are read literally. | Write exact instructions. Never rely on implied intent. |
| 2 | No arithmetic: counting and numeric handling are unreliable, and error grows with the count. | Compute in code, then ask about the *result*. |
| 3 | Dates are read as text, not ordered values. Mixed formats, relative dates, quarters and settlement windows all fail. | Parse and compare dates in code. |
| 4 | Indirection and multi-hop reasoning ("properties of properties", double negatives) lose accuracy. | Ask direct, single-step questions. |
| 5 | Context overload: irrelevant state distracts the model. | Filter state before sending. |
| 6 | Adversarial content can move the answer (injected instructions, misleading framing, text arguing for its own classification). | See the prompt-injection section below. |
| 7 | Instructions and criteria that contradict each other give unreliable answers. | Keep them aligned and avoid double negatives. |
| 8 | No structural invariants: P(X) + P(not X) is not guaranteed to be 1, and related answers are not guaranteed consistent. | Validate cross-question consistency in code. |
| 9 | Not trained to generate text; forcing text out of it is "very slow". | Use a Choice for bounded answers and an LLM for prose. |

Score has "weak numerical calibration" between levels. Use it to threshold or rank, and never interpolate a magnitude from it. Community source for the same point: https://flaviocopes.com/jev/.

The page publishes no numeric accuracy or failure rates. Re-check it when a new model version ships, because the page is per version.

## Prompt injection: jev is not a security boundary

> Source: https://docs.typesafe.ai/model-jaggedness/jev-1.13.md
> Source: https://pydantic.dev/docs/ai/models/typesafe/ (integration-partner docs)
> Source: https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)

- **The vendor acknowledges it**: adversarial content in `state` "can move the answer".
- **Reproduced exploit (press tier)**: an Octomind engineer asked jev whether to block `rm -rf ~/.ssh`.
  - The baseline block probability was 0.76.
  - After a fake tool-output field claiming pre-approval was injected into the state, it fell to **0.48**, and confidence fell from 0.64 to 0.22.
- **Option order is input.** Pydantic AI: "The order of a Literal's options or an Enum's members is part of what Jev sees, and reordering them can move the answer." Reordering an enum is a behaviour change, not a cosmetic one.
- **Disclosure before verdict.** Pydantic AI: "The arguments go to TypeSafe before the verdict comes back, so a call is disclosed to a third party even when it is then refused." Gating a tool call ships its arguments to TypeSafe whatever the verdict.
- **Retries do not converge.** jev "does not revise an answer the way a language model does". An output-validator retry loop tends to get the same answer back and burn the retry budget.
- **History confusion.** A tool call repeated in conversation history can be re-approved, because jev does not reliably recognise that it already ran.
- **Gate = grader collapse (press tier).** When jev both gates actions and grades agents, one injection can fool both layers.

Mitigations from the sources:
- LangChain's middleware **excludes tool output** from what jev sees when gating tool calls, "so content the agent fetched cannot authorize its own execution". It also pairs jev with human approval for consequential actions.
- Pydantic AI: "A guard built on Jev belongs alongside deterministic checks, not instead of them."
- VentureBeat's six pre-deployment questions (press tier):
  1. Do you log state, schema, option order, model version and confidence together?
  2. Does the service run under a dedicated workload identity?
  3. Have you tested different option orderings?
  4. Have you tested adversarial text injection?
  5. Is the model version pinned?
  6. Who is accountable when an automated decision fails?

For threat modelling and defence-in-depth design, use the `ai-security` skill. This file covers only the jev-specific facts.

## Data handling (direct TypeSafe API)

> Source: https://typesafe.ai/legal/privacy-policy
> Source: https://typesafe.ai/legal/data-processing
> Source: https://docs.typesafe.ai/legal

- **No training on input**: "We will not train or fine tune any artificial intelligence or machine learning models on Input." The MCA adds "without Customer's prior consent".
- Input counts as everything in `state`, question text and option labels.
- Retention is "as long as reasonably necessary". There is no fixed period.
- The DPA commits to breach notification **within 72 hours**. It uses EU SCCs (Modules 2 and 3) and the UK IDTA, and gives 15 days to object to a new subprocessor.
- The subprocessor list is at `https://trust.typesafe.ai/subprocessors`.
- **Zero data retention** is an enterprise option: ask `privacy@typesafe.ai`. It is not a self-serve toggle.
- Telemetry carve-out (MCA): "technical logs, hashes, summary statistics" may be processed indefinitely.

Cloudflare-routed requests follow Cloudflare's own no-training and no-persistence terms (see `cloudflare-workers-ai.md`). **No source says** whether TypeSafe's direct-API retention and training terms apply identically when a request arrives through Cloudflare.

**Trust Center (`https://trust.typesafe.ai/`)**: the page is JavaScript-rendered and could not be fetched. **Do not claim any certification (SOC 2, ISO 27001 or other).** The MCA names none. Send users to the Trust Center to check for themselves.

## Legal terms that change design decisions

> Source: https://typesafe.ai/legal/mca
> Source: https://typesafe.ai/legal/terms

- **The MCA governs API use.** The site Terms of Use cover browsing typesafe.ai only. Point users at the MCA.
- **No distillation**: you may not "train a model to imitate the output of the Services, or develop ... a similar or competing product". Never propose jev outputs as training data for another model.
- **Output rights**: TypeSafe assigns output rights to the customer. It keeps a broad processing license over input so it can run the service.
- **Liability cap**: the greater of the prior 12 months' fees or $50. The site ToU cap is $100.
- **No error-free warranty**, no uptime SLA, and support on "commercially reasonable efforts" only.
- **After termination**, there is no obligation to retain customer data. Export anything you need before you leave.
- **Feedback** submitted through the site becomes TypeSafe's, under a perpetual license. Leave sensitive specifics out of bug reports.

## Reliability

> Source: https://status.typesafe.ai

- The status page is informational only. **No SLA** exists.
- It lists two incidents, 2026-09-19/20 and 2026-09-20/21 (API downtime and console outage).
- Code defensively: set timeouts, back off on 429/529 (the SDK default), and circuit-break on repeated 5xx.

## Sources
- https://docs.typesafe.ai/model-jaggedness/jev-1.13.md
- https://pydantic.dev/docs/ai/models/typesafe/ (integration-partner docs)
- https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)
- https://www.langchain.com/blog/building-a-harness-with-jev (vendor blog)
- https://flaviocopes.com/jev/ (community)
- https://typesafe.ai/legal/privacy-policy
- https://typesafe.ai/legal/mca
- https://typesafe.ai/legal/terms
- https://typesafe.ai/legal/data-processing
- https://docs.typesafe.ai/legal
- https://trust.typesafe.ai/ (unfetchable; cited only as the place users should check)
- https://status.typesafe.ai

Fetched: 2026-09-23
