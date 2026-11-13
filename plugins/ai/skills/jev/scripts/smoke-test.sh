#!/usr/bin/env bash
# smoke-test.sh: send one tiny three-primitive jev request and print the raw response.
# Read-only diagnostic: it changes nothing, but it DOES spend tokens.
#
# REQUIRES AN API KEY AND SPENDS A FEW HUNDRED INPUT TOKENS (about $0.00002 at $0.042/M).
#
#   direct:      TYPESAFE_API_KEY=...                                        ./smoke-test.sh direct
#   cloudflare:  CLOUDFLARE_ACCOUNT_ID=... CLOUDFLARE_API_TOKEN=...          ./smoke-test.sh cloudflare
#   other model: JEV_MODEL=jev-latest ./smoke-test.sh direct   |   JEV_MODEL=typesafe/jev ./smoke-test.sh cloudflare
#
# Defaults (as of 2026-11-13): direct -> jev-1.14.0; cloudflare -> typesafe/jev-1.14.0
#   (Cloudflare's bare typesafe/jev id is still Jev 1.13).
#
# Why: it separates "my credentials/transport are wrong" from "my questions are wrong".
#   direct      POST https://api.typesafe.ai/v1/systemone   (model inside the body)
#   cloudflare  POST .../accounts/$ID/ai/run                (model + input as body siblings, NOT in the path)
# Reading the result:
#   401 or 403 on direct = key problem. A missing key returns 403 (typesafe-ai/skills#8, open), not the documented 401.
#   400 max_tokens_exceeded = state too large; 422 = payload shape; 429/529 = rate limit / overload.
#   Check the "model" field in the response: it names the version that actually answered.
#   Cloudflare needs a token with Workers AI Read + Edit.
# Sources: https://docs.typesafe.ai/api/system-one.md ; https://docs.typesafe.ai/api/errors.md ;
#          https://developers.cloudflare.com/ai/models/typesafe/jev-1.14.0/
set -euo pipefail

mode="${1:-direct}"
payload='{
  "state": "Help! My payouts have been failing for 3 days.",
  "questions": {
    "is_urgent":   {"type": "noul",   "instructions": "Does this convey urgency?"},
    "department":  {"type": "choice", "instructions": "Which team should handle this?",
                    "criteria": {"billing": "Payments, invoicing, refunds", "technical": "Bugs, outages, integrations", "sales": "Pricing, upgrades, new accounts"}},
    "frustration": {"type": "score",  "instructions": "How frustrated is the customer?",
                    "criteria": ["Calm", "Frustrated", "Very angry"]}
  }
}'

case "$mode" in
  direct)
    : "${TYPESAFE_API_KEY:?set TYPESAFE_API_KEY (create at https://console.typesafe.ai/keys)}"
    model="${JEV_MODEL:-jev-1.14.0}"
    # Merge "model" into the flat body without requiring jq.
    body="{\"model\": \"${model}\", ${payload#\{}"
    curl -sS -w '\nHTTP %{http_code}\n' -X POST https://api.typesafe.ai/v1/systemone \
      -H "Authorization: Bearer ${TYPESAFE_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "$body"
    ;;
  cloudflare)
    : "${CLOUDFLARE_ACCOUNT_ID:?set CLOUDFLARE_ACCOUNT_ID}"
    : "${CLOUDFLARE_API_TOKEN:?set CLOUDFLARE_API_TOKEN (Workers AI Read + Edit)}"
    model="${JEV_MODEL:-typesafe/jev-1.14.0}"
    body="{\"model\": \"${model}\", \"input\": ${payload}}"
    curl -sS -w '\nHTTP %{http_code}\n' \
      "https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run" \
      -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
      -H "Content-Type: application/json" \
      -d "$body"
    ;;
  *)
    echo "usage: $0 direct|cloudflare   (optional JEV_MODEL=<id>)" >&2; exit 2 ;;
esac
