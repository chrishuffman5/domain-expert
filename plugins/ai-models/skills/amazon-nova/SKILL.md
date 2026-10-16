---
name: amazon-nova
license: MIT
description: "Select active Amazon Nova model identities for Bedrock text, multimodal document/video or voice workloads. WHEN: Nova 2 Lite vs Nova 2 Sonic, context, supported inputs, region-profile or cost constraints. Do NOT use for Cohere Command or other model families, Bedrock/API/SDK mechanics, inference routing, agent harnesses, training, or eval infrastructure; use the relevant family skill or existing `ai` plugin."
---

# Amazon Nova model selection

This family skill compares the selected Amazon Nova model identities and their workload fit. Model identity, model capabilities and model-level limits belong here. Amazon Bedrock request construction, IAM, quota increases, endpoint routing and SDK mechanics belong to the existing `ai` plugin's inference/API coverage.

## Routing

| Need | Read |
|---|---|
| Multimodal text generation, document/video understanding, configured reasoning | [`Amazon Nova 2 Lite`](references/versions/us-amazon-nova-2-lite-v1-0.md) |
| Streaming speech/text voice interaction | [`Amazon Nova 2 Sonic`](references/versions/us-amazon-nova-2-sonic-v1-0.md) |
| Bedrock model APIs, IAM, inference profiles, endpoint operations and SDKs | Existing `ai` plugin's `inference-providers` and API guidance |
| Compare Nova with Google, OpenAI, Cohere, xAI or open weights | `ai-models-specialist`, then read the other selected family references |

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html (inspected 2026-10-16)

## Selected identities and model map

| Model | Exact documented ID | Role | Status | Reference |
|---|---|---|---|---|
| Amazon Nova 2 Lite | `us.amazon.nova-2-lite-v1:0` | General multimodal text-output model | Active; release 2025-12-02 | [version reference](references/versions/us-amazon-nova-2-lite-v1-0.md) |
| Amazon Nova 2 Sonic | `us.amazon.nova-2-sonic-v1:0` | Speech/text input and output for live voice | Active; release date unknown | [version reference](references/versions/us-amazon-nova-2-sonic-v1-0.md) |

AWS also documents `global.amazon.nova-2-lite-v1:0` and `global.amazon.nova-2-sonic-v1:0`. The prefixes identify inference profiles/region routing. They are deployment forms of these same selected identities, not additional model candidates. Verify current profile names and supported regions before use.

This catalog subset does not include the older Nova Premier/Pro/Lite/Micro line, Nova image/video generation, or Nova multimodal embeddings. Those are distinct model identities or modalities, not aliases for Nova 2 Lite or Sonic. Do not silently substitute one for another.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html (inspected 2026-10-16)

## Choose the model by modality

- Choose **Nova 2 Lite** for text, images, video and document input with text output; it is positioned for high-volume, cost/latency-sensitive processing.
- Choose **Nova 2 Sonic** for real-time bidirectional speech/text interaction, such as voice assistants or customer-service agents.
- Do not choose Sonic for a batch of PDFs merely because it is in the same Nova family. Its focus is speech interaction.
- Do not choose Lite when the core requirement is a low-latency speech-to-speech loop; use Sonic and evaluate turn-taking.
- If the task is vector retrieval/similarity, select an embedding model rather than either generative candidate. Nova Multimodal Embeddings is not part of this shortlist.

The modality distinction is more important than a generic “Lite versus Sonic” tier ladder. They are specialized model identities with different input/output shapes. The family guide's maximal context/output figures do not establish audio-session or per-file limits for Sonic.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Nova 2 Lite: documented fit and constraints

Nova 2 Lite accepts text, image, video and document input and returns text. AWS describes configurable extended reasoning, built-in web grounding and code interpreter capabilities. Use it for mixed-modality document assistance, image/video analysis, multimodal agent tasks and high-volume workflows. Validate that the specific feature is supported through the exact Bedrock route and region.

The Nova 2 overview says up to 1M context and up to 65,536 output tokens across the family. These are stated family maxima. They should not be turned into a guarantee for every media type, profile or request shape. Keep estimates conservative and test large prompts with actual input formats.

Document support has concrete constraints. The official guide permits up to five documents per request. Each text document can be at most 4.5 MB. Combined media document size can be up to 25 MB for direct upload or 2 GB through Amazon S3. Documents containing CMYK color profiles or SVG images inside PDFs are unsupported. A file can therefore be below the byte limit and still be rejected because its internal encoding is unsupported.

Nova requests may take up to 60 minutes according to the core inference guide. Account for long-running jobs when selecting client runtime behavior or application architecture; for detailed API timeout configuration, use the existing `ai` plugin's operational material.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Nova 2 Sonic: documented fit and unknowns

Nova 2 Sonic supports speech and text input/output and real-time bidirectional streaming. It is positioned for voice-enabled assistants and low-latency conversational interactions. Use it when speech understanding and speech generation must participate in an interactive loop.

The inspected Nova 2 overview says the family supports up to 1M context and 65,536 output tokens but does not publish Sonic-specific audio duration, session, codec, sample-rate or context limits on the core model list. Record those values as unknown until checked on a current Sonic-specific page. Do not reuse Nova 2 Lite's document limits for Sonic.

For evaluation, compare turn-taking and interruption behavior, latency across turns, recognition under noise, language coverage, transcription quality and speech naturalness. Audio tasks require measures beyond text completion quality. If only speech transcription is required, evaluate whether a dedicated speech-to-text route is simpler than a conversational speech model.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Pricing and availability

Nova 2 inference is token-priced, but the inspected model pages defer exact current rates to the Amazon Bedrock price table. Nova 2 Lite and Nova 2 Sonic prices may differ and audio-related charges may use modality-specific units. Do not copy the rate of the older Nova Lite or estimate Sonic from text-token pricing.

Both models have US and global profile IDs in the inspected API guide. A profile changes routing/region behavior; it is not a distinct checkpoint. Check the current region table, account eligibility and service quotas for the planned deployment. A model can be documented in the family guide while remaining unavailable in a specific region/account.

The inspected documentation describes Amazon-hosted access via Bedrock and does not publish downloadable weights or an open license for either model. Treat both as proprietary hosted services. For legal/privacy terms, consult the current Amazon service and contractual documentation.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Adoption, lifecycle and evidence limits

AWS describes high-volume processing and voice-agent use cases but did not publish comparable per-model usage totals in the inspected sources. The catalog records adoption as unknown. Stated use cases, Bedrock availability and workshop listings are not model-level usage evidence.

Nova 2 Lite's release date is recorded from AWS's dated model-card launch entry. Nova 2 Sonic's release date remains unknown in the inspected source. Do not infer a date from the model ID, documentation update date or family launch. No retirement dates are recorded here; recheck current model documentation and Bedrock's lifecycle notices before planning a migration.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Selection checklist

1. Is the input speech, or text/image/video/document content?
2. Must the model emit audio, or is text output sufficient?
3. Does the request fit the published context and media/document constraints?
4. Is a capability such as reasoning, web grounding or code interpreter required and available for the route?
5. Which Bedrock region/profile is available to the account, and what are its current rates and quotas?
6. Are long-running request times and modality-specific costs acceptable?
7. Have realistic document/audio examples been evaluated, including unsupported formats and failure cases?

If the question shifts to IAM, Converse/Invoke request construction, SDK code, cross-region routing, quota requests or provisioning, use the `ai` plugin's inference-provider/API coverage. This skill is for selecting model identity and task fit, not configuring Bedrock.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html (inspected 2026-10-16)

## Workload worksheets

Use the worksheet to determine which model family is relevant before comparing price:

| Question | Nova 2 Lite answer | Nova 2 Sonic answer |
|---|---|---|
| Primary input | Text, image, video, documents | Speech and text |
| Primary output | Text | Speech and text |
| Main task shape | Document/media analysis or high-volume multimodal generation | Live speech turn-taking |
| Family context claim | Up to 1M tokens | Up to 1M family-wide; audio limit unknown |
| Current exact rate | Unknown in inspected model guide | Unknown in inspected model guide |
| Profile IDs inspected | `us.` and `global.` | `us.` and `global.` |
| Best first test | Document QA, video summary, multimodal retrieval | Real noisy conversations with interruptions |

If the user has not provided a modality, ask which input and output are required. “Multimodal” is too broad to choose between these members.

For a document pipeline, inventory formats before model selection. Record whether each item is a text document, media-rich PDF, spreadsheet or image. Group only files the documented request can accept. Keep a preprocessing path for unsupported PDF encodings, oversized text files and excess document count. Do not automatically downsample a chart or rewrite a document without checking whether the transformation removes meaningful details.

For a voice application, identify whether it needs transcription only, audio-to-audio conversation, or text-plus-audio output. Measure per-turn latency and interruption handling, not just total response time. Define what the system should do when a user speaks over the model or the model cannot hear a segment.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Common selection mistakes

- Treating 1M context as a guarantee that all long-context inputs are affordable or useful.
- Assuming the same input formats and limits apply to speech and documents.
- Using the `global.` prefix as a distinct model version or treating it as a legal data-residency guarantee without checking the AWS region policy.
- Copying a Nova 1 price or limit into Nova 2 because the family names are similar.
- Pricing a live voice product with text-only rates when modality-specific audio charges may apply.
- Sending CMYK/SVG-containing PDFs directly and interpreting input failure as low model capability.
- Treating a published Bedrock availability row as proof of account entitlement in the selected region.
- Selecting Lite because of its name without verifying actual total cost and task quality.
- Using the maximum output budget by default and creating long, costly, difficult-to-review responses.
- Designing an unbounded request path despite the documented possibility of long Nova request runtimes.

When any of these issues is decisive, pause the recommendation until the relevant format, route or price is confirmed. For API details, send the integration portion to the existing `ai` plugin.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html (inspected 2026-10-16)

## Pilot design by modality

A useful Nova 2 Lite pilot should include ordinary and difficult documents, representative image/video clips and the actual output format the product needs. Separate exact extraction from summary quality. Include unsupported file types as negative tests to confirm the pipeline rejects or preprocesses them safely. Track:

- Correctness of extracted facts against an annotated source.
- Whether charts, tables and diagrams survive the input path.
- Sensitivity to long contexts and irrelevant attachments.
- Output length and cost on the account's current rate card.
- Timeout and retry behavior for very long requests.
- Failures caused by unsupported encodings and file sizes.

A Sonic pilot should include:

- Speech in the exact target languages and accents.
- Noise, crosstalk, silence and barge-in cases.
- Cases where the user corrects the model mid-turn.
- Confirmation of critical entities such as names, dates, amounts and account identifiers.
- Speech/text alignment and recovery from a dropped audio session.
- Current per-modality cost and concurrency limits in the chosen region.

These are evaluation questions, not claims that the model supports any particular language, audio duration or concurrency value. Verify each feature in the current Sonic documentation.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html (inspected 2026-10-16)

## Deployment constraint prompts

The model family itself does not answer infrastructure questions. Gather these constraints to decide whether a candidate survives:

- Is Bedrock mandatory, or can the application call another provider?
- Which AWS region must receive or process the request?
- Can a global inference profile be used under the user's residency policy?
- Must responses be real-time, or may large inputs take a long time?
- Is the application designed for documents, video, or streaming voice?
- What request sizes and payload formats appear in production?
- Does the user have access to on-demand or provisioned capacity?
- Are tool/grounding features allowed by the selected environment's policy?
- What failures need retry, alternate route or human fallback?

If the user is unsure, recommend a small sample evaluation that uses representative inputs and the actual AWS route. Do not assume a region choice, account quota or Bedrock entitlement from the model documentation alone.

This list is for model suitability. Hand off account, network, IAM, throughput, failover and API call details to the existing `ai` plugin.

For global profile use, ask whether the user's policy permits cross-region processing and have them check the current AWS documentation for participating regions. A profile name alone is not a data residency statement.

For cost comparisons, include preprocessing and storage alongside inference. A workload that needs OCR, transcription or media conversion may have material costs outside model tokens.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html (inspected 2026-10-16)

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html (inspected 2026-10-16)

## Compare cost on equivalent work

Compare the two models using the same task and output target. A voice workload should include audio input and generated speech; a document workload should include the same files and requested answer length. A text-only token estimate does not establish voice cost, and a document prompt should not be priced using audio assumptions.

Track input preparation separately from model inference. OCR, transcription, media conversion, storage and retrieval can change total cost even when the model's token rate is unchanged. Record current charges from the exact Bedrock route and split input, output and any modality-specific units.

If one candidate cannot accept the required modality or latency pattern, exclude it before comparing nominal rates. Ask AWS for the price and quota details that the inspected model pages leave unspecified.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html (inspected 2026-10-16)

## Sources

- https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html

Fetched: 2026-10-16
