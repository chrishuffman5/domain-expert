---
name: glm
description: "GLM model selection across current Z.ai text reasoning and multimodal Flash variants. Use for model-level capability, weight terms, lifecycle and task fit. Do NOT use for AI API/SDK mechanics, harnesses, evaluation infrastructure, inference routing or other model families."
license: MIT
---

# Glm model selection

## Scope and decision boundary

This skill covers GLM model identities, capability, lifecycle, adoption, weight terms and task selection. It does not provide implementation or evaluation workflows.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Model routing table

| Model | Choose it for | Key constraint | Reference |
|---|---|---|---|
| `GLM-5.3` | Text-only difficult coding and long-horizon agent reasoning | Reasoning always on; weight license unconfirmed | [version](references/versions/glm-5-3.md) |
| `GLM-5.3-Flash` | Visual/document coding and multimodal inputs | 320B total; local serving remains demanding | [version](references/versions/glm-5-3-flash.md) |

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Choose by input type

If screenshots, video or files are inputs, direct model selection toward GLM-5.3-Flash. The captured GLM-5.3 guide describes text input. Do not infer modality from the common GLM brand.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Text reasoning and coding

GLM-5.3 is positioned for complex coding and long-horizon agent tasks. Its reasoning is always enabled, with low, high and max effort levels. Avoid it when disabling reasoning is a requirement; a request attempting to turn reasoning off may fail.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Flash fit

GLM-5.3-Flash is documented for text, image, video and file input, tool use and visual coding. FlashX is a faster serving option, not a distinct weight identity. Test the serving tier on the actual workload.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Context and output

The catalog records 1M context and 128K maximum output for each selected model. Confirm host-specific limits and whether output includes reasoning tokens before planning long jobs.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## License boundary

Flash’s official model card identifies MIT terms for its weights. The weight license for GLM-5.3 remains unknown. The repository’s code license does not establish the license for model weights. Hosted access terms are separate from local weight rights.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Serving constraints

Flash is described as 320B total and 18B activated parameters. Sparse activation does not remove the memory demands of loading full weights. Hosted API or FlashX may be more practical where local capacity is limited.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Benchmark and adoption evidence

Z.ai’s claimed improvement over GLM-5.2 on its Code Bench is provider-authored, not independent. OpenRouter public routing usage for Flash is scoped to that router; it excludes direct and private traffic and is not global use or quality.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Name and version hygiene

Use the model name GLM-5.3 or GLM-5.3-Flash. Do not treat FlashX as a new model. Where a cloud marketplace exposes a dated ID, preserve it and verify status against that marketplace.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Selection workflow

Choose text-only versus multimodal first. Then establish local-weight rights and hardware requirements. Evaluate GLM-5.3 at a supported effort level for text/code; evaluate Flash for visual/video/document work or MIT-licensed local deployment.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Migration caveats

Always-on reasoning is part of the GLM-5.3 behavior. Verify effort support on the selected host. Marketplace snapshots may differ in endpoint, billing and capabilities from Z.ai direct API.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Freshness

Captured facts are dated 2026-10-16. Reopen Z.ai guides, release notes and the exact model card before quoting current IDs, prices, limits, licenses or lifecycle.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

## Sources

- https://docs.z.ai/guides/llm/glm-5.3
- https://docs.z.ai/guides/overview/overview
- https://github.com/zai-org/GLM-5
- https://help.aliyun.com/en/model-studio/model-pricing
- https://docs.z.ai/guides/vlm/glm-5.3-flash
- https://huggingface.co/zai-org/GLM-5.3-Flash
- https://docs.z.ai/release-notes/new-released
- https://openrouter.ai/rankings?benchmark=intelligence

Fetched: 2026-10-16
## Decision checks before selecting a tier

- Route screenshot, video or document-image work to Flash unless a different current source proves base GLM-5.3 supports it.
- For text-only complex code, test GLM-5.3 at low effort before using high or max effort.
- If reasoning must be disabled, do not recommend GLM-5.3 as the only candidate.
- For local multimodal hosting, check Flash weight size and actual serving hardware first.
- Use FlashX only when a faster hosted tier fits; keep it attached to the Flash model identity.
- Check whether the target service exposes the same context and output values as Z.ai direct docs.
- Use the model-specific license for Flash weights; do not transfer those terms to GLM-5.3.
- For hosted access, review service terms even when downloadable weights also exist.
- Confirm whether the required file or video modality is supported by the selected route.
- Compare provider coding claims with task-specific independent evaluation results.
- Check the marketplace snapshot date if an intermediary serves the model.
- Confirm current release notes before migrating from an older GLM version.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

> Source: https://help.aliyun.com/en/model-studio/model-pricing

## Claims to keep bounded

- Provider-reported code benchmark improvement is not a cross-provider result.
- An OpenRouter rank is restricted to public traffic routed through OpenRouter.
- FlashX speed does not establish improved accuracy or a new set of weights.
- An 18B active count does not state the total memory footprint for local hosting.
- MIT on Flash weights does not establish the GLM-5.3 license.
- API access does not imply commercial redistribution rights for weights.
- One provider’s context documentation may not describe a marketplace deployment.
- Multimodal input support does not mean the model generates images or video.
- Always-on reasoning may affect latency and token consumption.
- Unknown terms should stay unknown until the model card or license is inspected.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

> Source: https://help.aliyun.com/en/model-studio/model-pricing

## Review checklist for a recommendation

- Identify text-only versus multimodal inputs before naming a GLM tier.
- List supported reasoning efforts and note always-on reasoning for 5.3.
- Keep FlashX described as a serving option.
- Record which service and region expose the chosen model.
- Check weight-license text before any local or commercial recommendation.
- Explain the full model-size implication for Flash local hosting.
- Attribute benchmark claims to Z.ai and usage claims to OpenRouter.
- Use current release notes to validate lifecycle.

> Source: https://docs.z.ai/guides/llm/glm-5.3

> Source: https://docs.z.ai/guides/overview/overview

> Source: https://github.com/zai-org/GLM-5

> Source: https://help.aliyun.com/en/model-studio/model-pricing

