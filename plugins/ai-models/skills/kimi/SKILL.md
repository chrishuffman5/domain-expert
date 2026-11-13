---
name: kimi
description: "Kimi model selection across Moonshot’s current flagship and coding-specialist hosted endpoint. Use for identity, lifecycle, terms, modality, context and task fit. Do NOT use for AI API/SDK mechanics, harnesses, evaluation infrastructure, inference routing, or other families."
license: MIT
---

# Kimi model selection

## Scope and decision boundary

This family skill explains Kimi model-level fit, lifecycle, weight terms and selection. It does not teach API calls or operations.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Model routing table

| Model | Choose it for | Key constraint | Reference |
|---|---|---|---|
| `kimi-k3` | Multimodal flagship reasoning, long context and general coding | 2.8T total weights; custom scale-related terms | [version](references/versions/kimi-k3.md) |
| `kimi-k2.7-code` | Programming-agent and code-specialist tasks | Context/rates not captured; recheck official detail | [version](references/versions/kimi-k2-7-code.md) |

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Flagship fit

K3 is the broadest current model in this selected family: text, image and video understanding, reasoning, knowledge work and long-horizon coding. It has 1M context and both hosted and downloadable forms.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Coding specialist fit

Choose K2.7 Code for programming-agent work where a specialized endpoint suits the task. Its high-speed option is a serving tier, not separate weights. Do not infer K2.7 context or price from K3; both are unknown in this catalog snapshot.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Lifecycle hygiene

Moonshot’s current listing marks prior API names and families such as K2.5, `moonshot-v1`, K2, `kimi-latest` and `kimi-thinking-preview` discontinued. Avoid them for new use. Recheck the live model list because lifecycle has shifted repeatedly.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Modality and context

K3 supports image and video understanding with 1M context. The coding specialist is listed for code and programming-agent tasks; do not assume it has K3’s modality or context.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Pricing conditions

K3 pricing distinguishes cached input, uncached input and output per million tokens. Check the current page for cache rules and updated prices. K2.7 Code rate was not captured, so do not price it by analogy.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Weight license

K3 uses a Moonshot-specific license with conditions affecting very large Model-as-a-Service and large-scale products. It is not MIT or unconditionally open source. Review current text before redistribution or commercial hosting.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Local feasibility

K3 has 2.8T total and 104B active parameters. Activation count does not mean the full checkpoint fits ordinary hardware. Check model and serving requirements before choosing local deployment; hosted access may be more feasible.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Adoption evidence

Hugging Face likes/discussions for K3 are engagement proxies, not downloads or production use. K2.7 has official catalog availability but no comparable measured usage signal in the captured evidence.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Selection workflow

Ask whether the task needs broad multimodal reasoning or mostly code. Determine hosted versus local requirements; review K3 weight terms and hardware; confirm current ID and lifecycle; then evaluate with realistic prompt, image/video, code and tool traces.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Migration cautions

Do not substitute a retired Kimi alias for a current ID. Verify the exact service and any high-speed tier’s behavior after a change. Measure quality and cost against the task rather than assuming model names imply continuity.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Freshness

Snapshot date is 2026-10-16. Recheck Moonshot model and pricing pages before quoting context, rates, availability or retirement status.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

## Sources

- https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart
- https://platform.moonshot.ai/docs/models
- https://platform.moonshot.ai/docs/pricing/chat
- https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE
- https://forum.moonshot.ai/t/kimi-k3-is-here-our-most-capable-model/480
- https://huggingface.co/moonshotai/Kimi-K3
- https://forum.moonshot.ai/c/announcement/5

Fetched: 2026-10-16
## Decision checks before selecting a tier

- Use K3 when broad multimodal reasoning and long context are central.
- Use K2.7 Code when programming-agent tasks dominate the workload.
- Do not transfer K3’s context or price to K2.7 Code.
- Check the live Moonshot model list for retired aliases before writing a deployment plan.
- Confirm whether K2.7 Code high-speed is enabled for the user’s plan.
- Review the K3 custom license before model redistribution or third-party serving.
- Assess K3 hardware based on total checkpoint size, not only active parameters.
- Prefer hosted K3 when local hardware and model terms are unresolved.
- Test image and video inputs separately; do not infer identical support in K2.7.
- Check cache conditions for K3 before estimating token cost.
- Use the current pricing page for exact code-specialist rates.
- Keep model availability distinct from observed user adoption.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

> Source: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE

## Claims to keep bounded

- K3 repository likes and discussions show engagement, not downloads or active users.
- K2.7 model-list presence shows support, not how widely the endpoint is used.
- K3’s weight terms are custom and scale-dependent; do not shorten this to “open source.”
- An activated parameter count does not tell you how much memory the full checkpoint needs.
- A 1M context ceiling does not guarantee reliable retrieval across all positions.
- High-speed serving may alter latency and billing without changing model identity.
- Current API support is subject to the provider’s published lifecycle.
- Benchmark results should not replace coding-agent task tests.
- Do not claim K2.7 context if the cited model-specific page does not state it.
- Explain the source date beside prices and lifecycle statements.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

> Source: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE

## Review checklist for a recommendation

- Name `kimi-k3` or `kimi-k2.7-code` exactly.
- Note retired aliases if the user currently relies on one.
- Separate hosted availability from downloadable weights.
- Summarize custom K3 restrictions before commercial deployment.
- Check the chosen context and pricing page separately for each endpoint.
- Confirm target modality and code task coverage.
- Assess local hardware against full model requirements.
- Describe measured adoption only with its platform scope.

> Source: https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart

> Source: https://platform.moonshot.ai/docs/models

> Source: https://platform.moonshot.ai/docs/pricing/chat

> Source: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE

