# Amazon Nova 2 Lite (`us.amazon.nova-2-lite-v1:0`)

Status: active. AWS's model card dates Nova 2 Lite to 2025-12-02. The catalog ID is the US inference-profile form; `global.amazon.nova-2-lite-v1:0` is also documented. These are profiles/routes for the same model identity, not distinct model versions.

## Capabilities and limits

Nova 2 Lite accepts text, images, video and documents and returns text. AWS describes it as optimized for cost-effective, high-volume processing. It can support extended reasoning when configured; AWS also documents web grounding and code interpreter as built-in tools in the Nova 2 product overview. Treat those as Bedrock product/model capabilities and verify availability for the exact API path and region you will use.

The Nova 2 guide states up to 1M tokens of context and up to 65,536 generated tokens for Nova 2. These are family-wide stated maxima, not a guarantee that every modality, document input or region supports the full limits identically. Check the latest model-specific limits and configured request settings before relying on maximum-size prompts.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Price and deployment

Inference is billed on input and output tokens; exact current Nova 2 Lite rates are not published on the inspected model guide. Amazon directs users to the current Amazon Bedrock pricing page. Price can depend on model, region and inference mode, so use the live rate card for a workload estimate. On-demand inference is the default pay-per-use path described in the Nova guide. The model page documents US and global inference profiles, but a profile ID is not a separate weight set.

No public downloadable Nova 2 Lite weights or end-user license were identified in the inspected documentation. Treat this as a proprietary Amazon Bedrock-hosted model. For regional or compliance constraints, inspect the current supported-region table and Bedrock service terms.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Multimodal input guidance

Use Nova 2 Lite for text-plus-media questions, document assistance, image/video analysis, and high-volume multimodal tasks. Document support accepts common text, office, spreadsheet and image formats through documented Converse flows. The guide caps a request at five documents. Text-based documents must be at most 4.5 MB each; combined media documents are limited to 25 MB for direct upload and 2 GB when read from S3. Media-bearing PDFs/DOCX follow different size treatment from text-only documents, so verify which path your input uses.

AWS explicitly documents unsupported CMYK color profiles and SVG images inside PDFs. A document may fit the byte limit and still fail because of encoding. For visual charts and tables, use image/document input rather than extracting only plain text when the visual structure contains relevant meaning.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html (inspected 2026-10-16)

## Reasoning and tools

Reasoning is configurable; do not assume extended reasoning is always active. Use it for multi-step tasks only when its expected quality gain justifies extra latency and output. Web grounding can bring current information, while a code interpreter can execute Python; verify the exact region/API availability and cost of any tool behavior before deployment. Tool outputs are inputs to the model and do not substitute for validating results in application code.

The core inference guide says Nova requests may take up to 60 minutes. Client read timeout configuration therefore needs to account for long-running requests, particularly when processing large documents or using extended reasoning. Streaming is available through documented Bedrock inference paths, but streaming does not eliminate overall completion time or change token billing.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html (inspected 2026-10-16)

## Selection and limits

Choose Nova 2 Lite when a managed Bedrock model, multimodal understanding and cost/latency-oriented high-volume processing are relevant. It is the general-purpose model in this selected Nova subset. Choose Nova 2 Sonic when the application needs live speech-to-speech interaction; Sonic is not a text-only Lite alternative. If the actual need is semantic similarity or cross-modal retrieval, choose an embeddings model, not this text-generating model; that embedding model is not in the current 60-model catalog subset.

Do not infer price advantage from the word “Lite.” The name describes family positioning; compare the current rate card and your own task cost. Do not assume every input modality can be mixed without size limits. Keep format, file-count, region and runtime constraints in the design.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html (inspected 2026-10-16)

## Adoption and lifecycle

AWS describes high-volume use cases but did not publish a comparable per-model usage figure in the inspected sources. The catalog records adoption as unknown. Active status and model documentation are availability evidence, not proof of popularity.

The official core inference page currently documents `us.amazon.nova-2-lite-v1:0` and `global.amazon.nova-2-lite-v1:0`. The profile name contains a route selector; do not use it as a date or release identifier. Nova 2 Lite release date in this catalog comes from AWS's dated model card launch entry. No retirement date is listed in the inspected source. Recheck model availability, profile names and Bedrock rates before deployment or migration.

> Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html ; https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html (inspected 2026-10-16)

## Sources

- https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html
- https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html

Fetched: 2026-10-16
