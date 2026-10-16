# Amazon Nova 2 Sonic (`us.amazon.nova-2-sonic-v1:0`)

Status: active in the inspected Amazon Nova 2 model list. Release date: unknown in the inspected source. Canonical ID shown here is the US inference profile; `global.amazon.nova-2-sonic-v1:0` is also documented. These profile forms route to the same family model and are not separate identities.

## Modality and use

Nova 2 Sonic is a speech/text model for voice-enabled applications. AWS lists speech and text as input and output modalities. It supports real-time bidirectional streaming conversations and is positioned for low-latency voice agents, assistants and customer service experiences. It is not a general text-only chat model: its distinctive strength is handling speech in an interactive loop and returning speech with associated text/transcription.

The Nova 2 product guide describes a family-wide context ceiling up to 1M tokens and output up to 65,536 tokens, but does not state Sonic-specific audio context or duration limits in the inspected core inference page. Do not apply the family maxima blindly to an audio session. Check the current Sonic guide for audio duration, accepted codecs/sample rates, turn/session bounds and supported languages before designing around them.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Price and availability

Sonic inference pricing is token-based according to the Nova 2 overview, but the inspected page does not provide an exact current per-token rate. Audio input/output billing may differ by modality. Consult the current Bedrock price table for the exact region/profile and input/output types rather than applying Nova 2 Lite's rate or a text-only estimate.

Availability is through Amazon Bedrock, with US and global inference-profile forms in the current model ID listing. Confirm region eligibility, account access, quotas and profile choice for the target application. The documentation inspected here does not establish self-hosted weights or a separate public license; treat Sonic as a proprietary Bedrock service.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html (inspected 2026-10-16)

## Selection guidance

Use Sonic when the product must perceive speech and produce speech with short conversational turns. It is a better model-family fit than Nova 2 Lite for a streaming voice assistant. Lite is the current catalog choice for multimodal text/document/video understanding and text output. If the application needs only transcription, separate speech recognition may be a simpler architecture; Sonic's multimodal dialogue behavior should be evaluated against a speech-to-text plus text model pipeline.

For voice interactions, evaluate interruption handling, latency per turn, transcription quality, prosody, noise conditions, language coverage and total audio duration. No single context-window number answers these questions. Keep human confirmation and explicit application controls for consequential actions proposed during speech interaction.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Limits and lifecycle checks

The source describes low-latency bidirectional voice, but exact turn-duration limits, detailed language coverage, model-specific context and current pricing were not available in the inspected docs. Treat these as unknown pending a check of the current model guide. Do not transfer the five-document file rules for Nova 2 Lite's document flow to Sonic audio sessions.

AWS documents inference profiles in its model-ID table. A `us.` or `global.` profile is a routing choice, not a dated version. No release or retirement date is recorded in this catalog. Recheck the model list, supported regions and audio-specific limits before launch.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Adoption evidence

AWS documents a voice-agent use case and an Amazon Nova Sonic workshop, but did not disclose model-level traffic, deployment or download counts in the inspected material. The catalog leaves adoption unknown; workshop availability is an ecosystem resource, not measured model use.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html (inspected 2026-10-16)

## Sources

- https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html

Fetched: 2026-10-16
