# Command A Vision (`command-a-vision-07-2025`)

Status: active. Canonical API ID: `command-a-vision-07-2025`. Cohere's model overview identifies the release in July 2025; the day is unknown in the inspected source. No alias mapping was listed. This is a vision-understanding model, not an image generator.

## Modalities and limits

Command A Vision accepts text and images and returns text. Cohere documents up to 20 images per request, 128,000 tokens of context and up to 8,000 output tokens. It targets document analysis, charts, diagrams, table understanding, OCR and document question answering; its documented official language set is English, Portuguese, Italian, French, German and Spanish.

Two important limits are explicit: the model does not support tool use, and it accepts images but cannot generate them. Do not route tool calls to this model based only on the fact that it shares a Chat API interface with other Command models. A common endpoint does not mean a common capability set.

> Source: https://docs.cohere.com/docs/command-a-vision ; https://docs.cohere.com/docs/models (inspected 2026-10-16)

## Access, pricing and license

The model page says API keys can use the model free until rate limits are reached, and production use requires contacting Cohere sales. No public production rate is shown in the inspected material. Treat commercial pricing and availability as unknown until the provider confirms them for the account.

The inspected source describes a hosted Cohere model and does not establish a downloadable checkpoint or open license. Catalog license is therefore proprietary hosted API/model deployment. Do not inherit the Apache 2.0 license associated with a separate Command A+ W4A4 checkpoint.

> Source: https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Selection guidance

Choose A Vision when visual evidence is central and the model only needs to describe, extract or answer questions about that evidence. It is a better fit than Command A Reasoning for charts/tables/OCR, and a better fit than an image-generating model when output should be a text explanation. Choose A+ instead if the model needs both image input and agentic tool use. For workflows requiring tool use, pass the image findings to a separate controlled agent or use a different model; this model itself cannot invoke tools.

Evaluate with representative image quality and layout conditions: scanned and born-digital documents, rotated pages, charts with legends, dense tables, mixed languages, and multiple images. Measure extraction accuracy and refusal/error cases rather than judging a prose explanation alone. Respect the provider's image count and token limits.

> Source: https://docs.cohere.com/docs/command-a-vision ; https://docs.cohere.com/docs/command-a-plus (inspected 2026-10-16)

## Adoption and lifecycle

Cohere did not publish model-level usage or download data in the inspected Vision page. Adoption is unknown, not zero. The model ID contains a month-style suffix, but the official family table is the source of its status and month; do not infer an exact release day. Recheck the active model list, language list, image count, tool support and commercial access before migration.

> Source: https://docs.cohere.com/docs/models ; https://docs.cohere.com/docs/command-a-vision (inspected 2026-10-16)

## Sources

- https://docs.cohere.com/docs/command-a-vision
- https://docs.cohere.com/docs/models

Fetched: 2026-10-16
