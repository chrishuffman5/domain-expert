# TabPFN-3.5

## Identity and status

The official Prior Labs repository describes TabPFN-3.5 as the current default. It states the default package uses TabPFN-3.5 and that the single multitask checkpoint from 3.5 serves both classification and regression. TabPFN-3.5-Fast is a separate smaller/faster variant, not an alias for this catalog identity.

> Source: https://github.com/PriorLabs/tabpfn

## Task and scale

TabPFN-3.5 is a pretrained predictor for supervised tabular classification and regression. The official repository lists up to 1,000,000 rows and 20,000 features for TabPFN-3.5 and TabPFN-3.5-Fast, while recommending checkpoint-specific limits. These figures are guardrails; practical runtime and memory depend on hardware and workload. The repository recommends GPU use and batching test rows.

> Source: https://github.com/PriorLabs/tabpfn
> Source: https://priorlabs.ai/technical-reports

## Release and license

Prior Labs' technical reports page lists the TabPFN-3.5 report on September 15, 2026. The repository separates code from weights: code is Apache-2.0, but TabPFN-3.5 weights are under a non-commercial license. Prior Labs describes a commercial enterprise license for commercial production. Review the current license for the exact checkpoint and route before use.

> Source: https://priorlabs.ai/technical-reports
> Source: https://github.com/PriorLabs/tabpfn

## Availability and cost

The official repository provides a Python package with local checkpoints downloaded on first use, an official client for cloud inference, and enterprise/private high-throughput offerings. No fixed public per-token rate was established from inspected pages; API or enterprise price is unknown/contract-specific. Local compute and operational costs are separate from any hosted service terms.

> Source: https://github.com/PriorLabs/tabpfn
> Source: https://priorlabs.ai/pricing

## Adoption evidence and limits

Prior Labs' homepage displayed 8K GitHub stars and 4M downloads on 2026-10-16. The page did not define a counter period, unique users, active inference volume, or per-version coverage. These vendor-displayed values are distribution and interest proxies only; they do not measure active deployment or model quality.

> Source: https://priorlabs.ai/

## Sources

- https://priorlabs.ai/
- https://priorlabs.ai/technical-reports
- https://priorlabs.ai/tabpfn-3-5
- https://priorlabs.ai/pricing
- https://github.com/PriorLabs/tabpfn
- https://huggingface.co/Prior-Labs/TabPFN-v2-clf

Fetched: 2026-10-16
