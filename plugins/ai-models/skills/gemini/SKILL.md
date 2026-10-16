---
name: gemini
description: "Select Google Gemini model endpoints by task, modality, latency, reasoning depth, context, and cost. Covers Gemini 4 Argon, 3.8 Flash, 3.5 Flash-Lite, 3.8 Live, and 3.5 Transcribe. Do NOT use for API/SDK implementation, agent harnesses, provider routing, or evaluation infrastructure; use `ai`. Do NOT use for Claude or other provider families. Do NOT use for Gemma open weights; use `gemma`."
license: MIT
---

# Gemini model selection

This skill covers Google's hosted Gemini model identities and selection tradeoffs. It distinguishes general reasoning models from low-cost processing and specialist audio endpoints. It does not document API call mechanics.

The selected catalog contains five Gemini identities: Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.5 Flash-Lite, Gemini 3.8 Live, and Gemini 3.5 Transcribe. It does not include every Google model. Gemma is an open-weight family with a separate selection skill; Gemini and Gemma are not interchangeable deployment choices.

## Do NOT use
> Source: https://ai.google.dev/gemini-api/docs/models.md


- Do NOT use this skill for Gemini API or Vertex AI request syntax, SDKs, authentication, retries, streaming code, or response schemas; use the `ai` plugin.
- Do NOT use it to build agent harnesses, tool loops, computer-use integrations, MCP servers, or conversation-state infrastructure; use the `ai` plugin.
- Do NOT use it for provider gateways, model routing, cloud deployment, regional endpoint setup, failover, or batch job implementation; use the `ai` plugin.
- Do NOT use it to build training, fine-tuning, benchmark, red-team, or evaluation infrastructure; use the `ai` plugin.
- Do NOT use it to select Anthropic Claude or any non-Google model family; route to that provider's family skill.
- Do NOT use it for Google Gemma open-weight downloads, local inference, tuning, or license interpretation; use the `gemma` skill.
- Do NOT use it for Gemini API features that are not model selection, such as Search grounding or URL-context mechanics; use `ai` for feature integration.

## Route by task shape
> Source: https://ai.google.dev/gemini-api/docs/models.md


| Workload | First candidate | Compare against | Selection reason |
|---|---|---|---|
| Hard general reasoning, complex coding, math/science | Gemini 4 Argon | Gemini 3.8 Flash | Argon has the largest shared context and long decode; Flash may meet quality needs at lower cost. |
| General multimodal knowledge or agentic work | Gemini 3.8 Flash | Gemini 4 Argon | Stable Flash is the general speed/cost option; move up only when task checks justify it. |
| High-volume translation or simple structured processing | Gemini 3.5 Flash-Lite | Gemini 3.8 Flash | Lite is provider-positioned for cost-efficient high-volume tasks; check error rates on your own data. |
| Real-time streaming voice conversation | Gemini 3.8 Live | None in this selection | It is a specialist low-latency Live endpoint with audio input/output. |
| File-based transcription with speaker and timing annotations | Gemini 3.5 Transcribe | Gemini 3.8 Flash | Transcribe is the specialist endpoint; Flash is a broader multimodal alternative only if task checks support it. |
| High-precision or expensive decisions | Argon or Flash after evaluation | Other provider families | Select on representative evidence; model family alone does not establish accuracy. |

Treat “stable” as a provider lifecycle label, not a guarantee of quality for a particular workload. The catalog contains no comparable public usage metric for most selected Google endpoints; stability and documentation are availability evidence, not adoption measurements.

## Selection workflow
> Source: https://ai.google.dev/gemini-api/docs/models.md


1. Name the required input and output modalities: text, image, video, audio, PDF, or live audio stream.
2. Determine whether the task needs general generation, long reasoning, live interaction, transcription, or a high-volume inexpensive pass.
3. Check the exact endpoint and current lifecycle status in its reference file and official model catalog.
4. Estimate context use, including supplied media, tool results, conversation history, thinking budget, and expected answer.
5. Identify the applicable price tier and modality-specific charges before comparing costs.
6. Evaluate quality, latency, and cost on examples from the intended workload.
7. Record the exact model ID and date of the status/pricing check.
8. Recheck provider deprecation notices before changing a production ID.

A short prompt can still require difficult reasoning, and a long prompt can be routine extraction. Use task complexity and input size together; do not route by token count alone.

Make the first comparison with a stable, lower-cost model when the error cost is modest. Add a stronger candidate when the baseline misses hard examples. For high-impact tasks, plan human review or deterministic validation; model capability and Google tooling do not guarantee correctness.

Measure the complete task cost, not input tokens alone. Include output and thinking tokens where billed, audio/video tokens, grounding or tool charges where applicable, cache storage, batch discount, and retries. Do not compare modalities using a single text token rate.

The list below is a decision aid. It does not set a universal rank or recommend one endpoint for every application.

## General reasoning and multimodal work
> Source: https://ai.google.dev/gemini-api/docs/models.md


### Gemini 4 Argon
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon


Use Gemini 4 Argon for the hardest general reasoning, long decode, complex software engineering, math/science, and multi-step agent work represented in the catalog. Its official model card lists text, image, video, audio, and PDF input; tool capabilities include function calling, code execution, file search, search grounding, and URL context.

The model has a shared 1,048,576-token input/output context. Synchronous output is capped at 65,536 tokens; long decode can reach 1,048,576. Thinking levels are low, medium, and high. Since input, thinking, and output share the budget, a large source document can leave less room for answer generation.

As of this catalog snapshot, pricing is introductory through Nov. 30, 2026: $2 per million input tokens and $10 per million output tokens; published prices rise to $4/$20 on Dec. 1. It is paid-only. Implicit cache hits are discounted; explicit caching is unsupported. Recheck the date boundary before making a budget or migration plan.

Longer thinking can improve hard-problem results at the cost of time and output tokens. Argon requests can take several minutes on demanding prompts. Use background processing or sufficient timeouts as an integration choice; implementation belongs to `ai`.

The model supports computer use only as Preview in the inspected model card. Do not treat that as mature or universally enabled. Check account, region, model endpoint, and lifecycle page before relying on a capability.

### Gemini 3.8 Flash
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash


Use Gemini 3.8 Flash for current stable general work, including long-horizon software engineering, autonomous agents, and multimodal tasks where a Flash cost/speed profile is attractive. Its catalog record lists up to 1,048,576 input tokens and 65,536 output tokens, with text, image, video, audio, and PDF input.

Compare Flash with Argon when task difficulty is uncertain. If Flash meets the quality threshold on challenging examples, it may be the more economical general choice. If it fails, inspect whether the failure requires deeper reasoning, more context, a better prompt, or a different specialist modality before escalating every request.

The catalog lists standard paid tier pricing of $0.50 per million input and $3 per million output; provider pricing conditions vary by tier and modality. Check current pricing rather than treating the snapshot as timeless.

### Gemini 3.5 Flash-Lite
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash


Choose Flash-Lite for high-volume agentic tasks, translation, and simple data processing when price and throughput matter. The catalog lists $0.30 per million input and $2.50 per million output, plus a cache rate; current modality and tier terms are in its reference.

Flash-Lite is not the default for difficult reasoning simply because it is cheaper. Evaluate the error rate and review burden on representative, borderline, multilingual, and malformed examples. Compare against 3.8 Flash when quality loss creates downstream costs.

A two-stage selection pattern can use a low-cost pass for routine cases and escalate uncertain cases, but the confidence signal and routing policy must be validated in application logic. No model’s self-reported confidence should be treated as calibrated without evidence.

## Audio and speech tasks
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live


### Gemini 3.8 Live
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live


Choose Gemini 3.8 Live for real-time voice-agent experiences with low latency and streaming audio input/output. Google positions it as the default Live API model for most conversational voice experiences without reasoning-induced delay. Its catalog record lists 131,072 input and 65,536 output tokens.

Live is a specialist interface, not simply a general text model that happens to accept audio. Select it when turn-taking, streaming interaction, and audio output are central. Do not choose it for offline transcription merely because it accepts audio; use the transcription endpoint when diarization, timestamps, and custom vocabulary matter.

The catalog does not provide a verified single pricing rate for live audio. Use current modality-specific pricing and confirm audio token accounting, streaming conditions, and any tool charges. Do not estimate from text-only input/output prices.

Use the extended-thinking Live sibling only where a requirement justifies higher background reasoning and it is available; it is not one of the selected catalog IDs in this skill. Do not substitute it without checking its own status, limits, and price.

### Gemini 3.5 Transcribe
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe


Choose Gemini 3.5 Transcribe for speech-to-text when automatic language detection, speaker diarization, word timestamps, or custom vocabulary biasing are needed. The inspected provider page describes support for more than 85 languages and code-switching.

Check whether the workload is audio-file transcription or bidirectional live transcription. The catalog records the file transcription identity; a separate live ID may exist and is not interchangeable without checking its current endpoint behavior.

The catalog does not record one verified universal price. Consult the audio section of the current Gemini pricing page, including batch conditions. Compare transcription quality on accents, code-switching, noise, speaker overlap, specialized vocabulary, and timestamps that downstream systems consume.

Do not infer transcription accuracy from language-count claims. A language being supported does not establish equal performance across dialects, recording conditions, or domain vocabulary.

## Modality, context, and cost controls
> Source: https://ai.google.dev/gemini-api/docs/models.md


Use the model-specific reference to distinguish supported modalities from endpoint behavior. A catalog capability does not mean every API method accepts the same input packaging or produces the same response shape.

Gemini 4 Argon’s context is shared across input and output. Keep reserve for reasoning and response generation. For Flash, the catalog separates input and output limits; check current docs for modality-specific tokenization and request limits.

Audio and video tokenization can differ from text. Estimate representative media length, resolution, sample rate, and output form. Include any generated media output because it can dominate cost even when the text prompt is short.

Pricing can vary by free/paid tier, standard/priority/batch inference, cached tokens, long input, modality, and date. The catalog records conditions known on the research date; the official pricing source is the authority for a current spend estimate.

Gemini 4 Argon has implicit caching, while explicit caching is unsupported. Do not carry caching assumptions from older Gemini models into Argon. For all models, verify whether cache charges and discounts cover the actual data pattern.

Google's model catalog includes stable and preview endpoints. Preview status means greater change risk; do not deploy a preview ID as if it were a stable alias. The selected models here are stable as of the catalog snapshot, but status can change.

## Versions, aliases, and lifecycle
> Source: https://ai.google.dev/gemini-api/docs/deprecations


Use the exact identifiers in the routing table and linked references. The catalog records stable API names such as `gemini-4-argon` and `gemini-3.8-live`; it does not record a separate pinned version or alias for these entries.

Do not invent a version suffix, date-stamped ID, or replacement based on a model’s displayed family name. Consult Google's official model list and version patterns for the endpoint currently offered.

Google’s deprecations page distinguishes a deprecation announcement from shutdown and reports earliest possible shutdown dates. Those dates are not guaranteed exact shutdown dates. Check release notes and current deprecations before selecting an ID for a long-lived deployment.

Do not confuse Gemini with Gemma. Gemini is a provider-hosted model line; Gemma is a separately documented open-weight line with different distribution, usage terms, and deployment responsibilities. Route local-weight questions to `gemma`.

Do not count model endpoint variants as independent families. Live, Transcribe, and general Flash belong to the Google Gemini family but solve distinct task shapes; route within the family by modality and output contract.

## Evaluation and operational judgment
> Source: https://ai.google.dev/gemini-api/docs/models.md


This skill supports model selection, not evaluation infrastructure. For each candidate, define success criteria such as exactness, coverage, factual grounding, transcription word error, speaker attribution, latency, cost, and human correction burden.

Use examples sampled from the real workload, including tail cases. Keep evaluation data private and authorized. Compare model versions only after ensuring the request shape and tool context are equivalent.

For complex reasoning, inspect whether improvements persist when prompts contain irrelevant context or ambiguous instructions. Include cases where a correct result is to state uncertainty or ask a follow-up.

For transcription, evaluate both text content and metadata: speaker labels, timestamps, language transitions, and domain words. A clean transcript with incorrect timing may still fail the application.

For live voice, measure turn latency and stability across longer interactions, not just one-shot response quality. Check interruption handling and the application’s fallback behavior as part of system evaluation; building those mechanisms is outside this skill.

For high-volume Lite routing, compare total cost including errors and review. The price delta is useful only if the lower-cost endpoint meets your accepted quality bar.

Re-run comparisons after a material model version, price, endpoint, prompt, or modality change. Save the exact model ID and date so a later result can be reproduced.

## Practical workload checks
> Source: https://ai.google.dev/gemini-api/docs/models.md


### Document analysis
> Source: https://ai.google.dev/gemini-api/docs/models.md


For a long PDF, confirm that the endpoint accepts the document form and that the total input fits once instructions, prior turns, and expected output are included. Argon's shared budget means a large input reduces space available to thinking and response tokens.

When a task requires citations from supplied documents, evaluate whether the answer identifies the relevant passages, not just whether it sounds plausible. Grounding features and model selection are related but distinct; configuring a retrieval or URL tool belongs to `ai`.

### Video understanding and generation
> Source: https://ai.google.dev/gemini-api/docs/models.md


Gemini 3.8 Flash accepts video input and can support agentic video understanding according to the catalog. Estimate media length and resolution, and test whether temporal events are accurately represented. Do not infer video generation capability from video input support.

Gemini Omni Flash is not selected in the final catalog. For video creation, consult the model catalog and pricing directly rather than routing the request to a text-generation model based on its multimodal input support.

### Translation and extraction
> Source: https://ai.google.dev/gemini-api/docs/models.md


Flash-Lite is a candidate for translation and simple data processing at high volume. Evaluate language pairs separately; broad multilingual support does not imply equal quality across them.

For extraction, define required fields and acceptable missing-value behavior. Compare false positives and omissions, then account for downstream schema validation and manual correction.

### Streaming voice
> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live


For live voice interactions, optimize the selection decision for turn latency and conversational continuity as well as semantic quality. The Live endpoint has audio output and a smaller context budget than general Flash in the catalog.

Evaluate representative accents, background noise, interruptions, multi-turn references, and function-call moments. These checks inform model choice; implementing voice transport and turn management belongs to `ai`.

### Transcription
> Source: https://ai.google.dev/gemini-api/docs/models.md


Check the audio conditions that matter to the workload: multiple speakers, overlap, code-switching, domain terminology, and timestamp granularity.

If the result will trigger downstream actions, validate speaker attribution and entity spelling separately. A readable transcript can still be unsafe for diarized or timestamp-sensitive use.

## Safe selection examples
> Source: https://ai.google.dev/gemini-api/docs/models.md


- A challenging multi-document code analysis with time for longer reasoning can begin with Argon; compare Flash on the same hard examples before deciding whether the premium is needed.
- A straightforward language conversion at high volume can begin with Flash-Lite; compare its corrections and review cost against Flash.
- A spoken dialogue agent with low-latency audio output should use Live as the specialist model-selection starting point.
- A batch of recordings that needs speaker labels and word timing should use Transcribe as the starting point.
- A request for a locally hosted Google model belongs to Gemma, not this hosted Gemini family skill.
- A request for Google model API code belongs to the `ai` integration plugin, not this selection guide.

## Routing table
> Source: https://ai.google.dev/gemini-api/docs/models.md


| Catalog model | Reference | Use when |
|---|---|---|
| Gemini 4 Argon (`gemini-4-argon`) | [version details](references/versions/gemini-4-argon.md) | Hard reasoning, long decode, complex coding, multimodal multi-step work. |
| Gemini 3.8 Flash (`gemini-3.8-flash`) | [version details](references/versions/gemini-3-8-flash.md) | Stable general multimodal, coding, and agentic tasks. |
| Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) | [version details](references/versions/gemini-3-5-flash-lite.md) | High-volume translation and simple data processing with cost sensitivity. |
| Gemini 3.8 Live (`gemini-3.8-live`) | [version details](references/versions/gemini-3-8-live.md) | Low-latency real-time voice interaction. |
| Gemini 3.5 Transcribe (`gemini-3.5-transcribe`) | [version details](references/versions/gemini-3-5-transcribe.md) | File transcription with diarization, timestamps, and vocabulary biasing. |

## Cross-family boundaries
> Source: https://ai.google.dev/gemini-api/docs/models.md


Choose the `claude` skill for Anthropic model identities and Claude-specific reasoning, cost, and version tradeoffs. Choose `gemma` for open-weight Google models and local deployment choices.

Choose `ai` for Gemini API or Vertex AI mechanics, SDKs, tool calls, model routing, system design, deployment, and evaluation infrastructure. This skill can identify what to check, but it does not specify an API implementation.

For general comparisons spanning several providers, use the ai-models specialist or the family skills for each candidate. Do not rank providers from unlike adoption proxies or isolated benchmark results.

## Sources

The selected model references carry canonical catalog facts, limitations, adoption evidence, source URLs, and retrieval date. They are the starting point for changing a model choice.

- [Gemini 4 Argon](references/versions/gemini-4-argon.md)
- [Gemini 3.8 Flash](references/versions/gemini-3-8-flash.md)
- [Gemini 3.5 Flash-Lite](references/versions/gemini-3-5-flash-lite.md)
- [Gemini 3.8 Live](references/versions/gemini-3-8-live.md)
- [Gemini 3.5 Transcribe](references/versions/gemini-3-5-transcribe.md)
- [Gemini model catalog](https://ai.google.dev/gemini-api/docs/models.md)
- [Gemini lifecycle](https://ai.google.dev/gemini-api/docs/deprecations)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing.md)

Fetched: 2026-10-16
