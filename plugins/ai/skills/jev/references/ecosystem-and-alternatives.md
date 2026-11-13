# Ecosystem: integrations, community tools and the company

Read this when a user asks which framework already wraps jev, whether a community tool is trustworthy, or who makes jev. **Competing decision models (Gemini Decisions, OpenAI Decisions, Kev, Ollama and others) moved to `decision-model-alternatives.md`. Purchase routes and gateways are in `purchase-routes.md`.**

## Identity

> Source: https://typesafe.ai
> Source: https://typesafe.ai/team
> Source: https://typesafe.ai/blog/dont-call-it-a-decision-model (vendor blog)

- jev is TypeSafe AI's first "System One model": hosted, proprietary (no published weights), returning typed answers with calibrated probabilities. It is not an LLM, a coding-agent model, a CLI or a framework.
- TypeSafe avoids the term "decision model": "Jev makes judgments, code makes decisions."
- Leadership: Diogo Almeida (CEO), Sasha Sheng (COO), Erik Gafni (CTO); in-person San Francisco office.
- Training method name: "Reinforcement Learning for Calibrated Decisions" (RLCD), per the launch post.
- **Not Lightbend.** TypeSafe AI is unrelated to Lightbend's former "Typesafe" (Scala/Akka). Treat Scala/Akka knowledge as inapplicable.

## Company news since launch

> Source: https://typesafe.ai/blog/series-ai (vendor blog)
> Source: https://www.channelinsider.com/ai/news-typesafe-ai-870-million-funding-jev-model/ (press)
> Source: https://www.implicator.ai/typesafe-ai-raises-870-million-for-jev-as-openai-amazon-and-cloudflare-ship-rivals/ (press)

- **Series A, reported $870M at a $7.5B valuation** (blog body dated 2026-10-09; the post uses a placeholder and the figures come from its footnote and press). Led by Andreessen Horowitz with Sequoia, existing investor DCVC and angels; Martin Casado joins the board.
- Vendor claim, unverified: a third of the Fortune 500 use jev (press notes the lead investor said 25%). Press reports a claim of profitability after expenses; revenue undisclosed.
- jev was still described as "early access" in posts through 2026-10-14. Access status is unresolved: the quickstart no longer mentions a waitlist, VentureBeat reported the waitlist dropped with $5 free credit, and a community post said signups were paused on 2026-09-22.
- Named customer (company-reported): Jack & Jill, 88% candidate-screening cost cut.

## Integrations (fetched 2026-11-13)

> Source: https://docs.langchain.com/oss/python/integrations/providers/typesafe.md
> Source: https://docs.langchain.com/oss/javascript/integrations/providers/typesafe.md
> Source: https://pydantic.dev/docs/ai/models/typesafe.md
> Source: https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
> Source: https://mastra.ai/reference/classifier/classifier.md
> Source: https://github.com/typesafe-ai/n8n-nodes-typesafe-ai
> Source: https://docs.sentry.io/platforms/javascript/guides/eve/configuration/integrations/typesafe/
> Source: https://composio.dev/toolkits/jev.md
> Source: https://tanstack.com/ai/latest/docs/adapters/typesafe.md

| Integration | Package / entry point | Notes |
|---|---|---|
| LangChain Python | `langchain-typesafe>=0.1.0`, `TypeSafeClassifier`; types from `langchain_core.decisions` | Python ≥ 3.11. In 0.1, pass `state` **and** `questions` to `invoke`. `usage` is a dict and may be `None`. Middleware (`ModelRouterMiddleware`, `AutoModeMiddleware`) is beta, needs `langchain>=1.5.0`, and is imported from `langchain.agents.middleware` with `classifier=TypeSafeClassifier()`; `langchain_typesafe.experimental.middleware` is deprecated. |
| LangChain JS | `@langchain/typesafe>=0.1.0`, `@langchain/core>=1.4.0` | `timeout` 30000 ms, `maxRetries` 2. Middleware from `langchain` (≥ 1.6.5); `@langchain/typesafe/middleware` exports are deprecated, removal planned for 0.2.0. |
| Pydantic AI | `pydantic-ai-slim[typesafe]`, `TypeSafeModel` / `typesafe:jev-latest` | Output-type fields become questions; `FallbackModel` hands unsure routes to an LLM; `temperature`/`top_p` ignored. Examples still pin `jev-1.13.0`, and the page says jev "reads text only" (stale since images shipped). |
| Vercel AI SDK | `ai` + `@ai-sdk/typesafe-ai`; `experimental_decide` with `typeSafeAi.decisionModel(id)` | Env `TYPESAFE_AI_API_KEY` (not `TYPESAFE_API_KEY`). `boolean` maps to Noul. Confidence under `providerMetadata.typesafe.confidence`. Never use `experimental_evaluate` / `evaluationModel` (deprecated). |
| Mastra (new) | `Classifier` from `@mastra/core/classifier` with `typeSafeAi.decisionModel('jev-latest')` | `classifier.decide({ state })`; a "refusal" answer type exists, so check `type` before reading numbers; tracing exposes state unless `hideInput`/`hideOutput`. |
| TanStack AI | `@tanstack/ai-typesafe` (`typesafeDecider`), `@tanstack/ai-vercel-gateway` (`vercelGatewayDecider`) | Server-only; `decide()` does not stream; `meta` is a reserved question key. Its docs list `jev-latest` and `jev-1.13.0` only. |
| n8n (official repo, new) | `@typesafe-ai/n8n-nodes-typesafe-ai` | MIT, "Tested with n8n 2.40"; Evaluate and Route operations; default timeout 5000 ms. |
| Sentry (new) | `Sentry.typesafeIntegration()` | Adds a `gen_ai.decide` span per `systemOne()` call and records inputs/outputs by default; set `recordInputs: false`, `recordOutputs: false` for sensitive data. Needs Sentry JS ≥ 11.7.0 and `@typesafe-ai/sdk` `>=0.5.0 <1`. |
| Composio (new) | toolkit `jev`: `JEV_LIST_MODELS`, `JEV_EVALUATE_STATE` | Uses your own Jev key; SDK or MCP session; each call is usage-priced. |
| eve (Vercel) | `auto()` from `eve/tools/approval` | Tool-call approval; see `limitations-and-security.md` and `examples.md`. |

No official LlamaIndex, DSPy, CrewAI, Haystack or Zapier integration was found from a fetchable source.

## TypeSafe's own repos and agent skill

> Source: https://github.com/typesafe-ai
> Source: https://docs.typesafe.ai/agent-skill.md

- Org repos: `typesafe-sdk-python`, `typesafe-sdk-js`, `skills` (~2.9k stars), `n8n-nodes-typesafe-ai`, `typesafe-public-examples` (cookbook and demo code), `WorkflowEvals` (evals.typesafe.ai), `system-one-adapter-python` (LLM-backed drop-in, last updated 2026-09-22), plus a vllm fork with no stated purpose.
- Official agent skill: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai` (invoke `/typesafe:typesafe-ai`); other agents `npx skills add typesafe-ai/skills --skill typesafe-ai` (`-g` global). Update with `claude plugin marketplace update typesafe-ai` + `claude plugin update typesafe@typesafe-ai`, or `npx skills update`. Use one install method. Open issues on that repo include over-triggering on TypeScript requests (#2).

## Community tools (community tier; never present as TypeSafe-endorsed)

> Source: https://github.com/jkudish/jev-mcp (community)
> Source: https://github.com/leepokai/jev-guard (community)
> Source: https://github.com/topics/typesafe-jev (community)
> Source: https://github.com/Anil-matcha/awesome-jev-by-typesafe (community)

- **jev-mcp** (`@jkudish/jev-mcp`, ~578 stars, Node ≥ 22): grew from one tool to 12 (`jev_verify`, `jev_screen`, `jev_noul`, `jev_find`, `jev_rerank`, `jev_classify`, `jev_decide`, `jev_compare`, `jev_extract`, `jev_audit`, `jev_review`, `jev_gate`). Providers: TypeSafe direct, OpenRouter, Cloudflare, Vercel. `jev_screen` is advisory only; HTTP mode needs `JEV_MCP_AUTH_TOKEN` unless loopback. Author calls it early software. For building MCP servers generally, use `mcp`.
- **jev-guard** (~153 stars): tool-call hook for Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor and others. **Fails open by default** when jev is unreachable (`JEV_GUARD_FAIL_CLOSED` flips it); "a guardrail, not a sandbox".
- The GitHub topic `typesafe-jev` lists 125 repos (community SDKs for Swift and Go, Postgres/DuckDB extensions, visualizers). The awesome list names many more guards and agents; none was individually verified.

These tools treat jev as an **advisory signal**, never as the enforcement point.

## Sources
- https://typesafe.ai
- https://typesafe.ai/team
- https://typesafe.ai/blog/dont-call-it-a-decision-model (vendor blog)
- https://typesafe.ai/blog/series-ai (vendor blog)
- https://typesafe.ai/blog/introducing-system-one-models-and-jev (vendor blog)
- https://www.channelinsider.com/ai/news-typesafe-ai-870-million-funding-jev-model/ (press)
- https://www.implicator.ai/typesafe-ai-raises-870-million-for-jev-as-openai-amazon-and-cloudflare-ship-rivals/ (press)
- https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict (press)
- https://flaviocopes.com/jev/ (community)
- https://docs.typesafe.ai/introduction/quickstart.md
- https://docs.langchain.com/oss/python/integrations/providers/typesafe.md
- https://docs.langchain.com/oss/javascript/integrations/providers/typesafe.md
- https://pydantic.dev/docs/ai/models/typesafe.md
- https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai
- https://mastra.ai/reference/classifier/classifier.md
- https://tanstack.com/ai/latest/docs/adapters/typesafe.md
- https://github.com/typesafe-ai/n8n-nodes-typesafe-ai
- https://docs.sentry.io/platforms/javascript/guides/eve/configuration/integrations/typesafe/
- https://composio.dev/toolkits/jev.md
- https://github.com/typesafe-ai
- https://github.com/typesafe-ai/skills
- https://docs.typesafe.ai/agent-skill.md
- https://github.com/jkudish/jev-mcp (community)
- https://github.com/leepokai/jev-guard (community)
- https://github.com/topics/typesafe-jev (community)
- https://github.com/Anil-matcha/awesome-jev-by-typesafe (community)

Fetched: 2026-11-13
