#!/usr/bin/env bash
# smoke-test.sh: send one tiny three-primitive jev request and print the raw response.
#
# REQUIRES AN API KEY AND SPENDS A FEW HUNDRED INPUT TOKENS (about $0.00002 at $0.042/M).
#
#   direct:      TYPESAFE_API_KEY=...                                        ./smoke-test.sh direct
#   cloudflare:  CLOUDFLARE_ACCOUNT_ID=... CLOUDFLARE_API_TOKEN=...          ./smoke-test.sh cloudflare
#
# Why: it separates "my credentials/transport are wrong" from "my questions are wrong".
#   direct      POST https://api.typesafe.ai/v1/systemone   (model inside the body)
#   cloudflare  POST .../accounts/$ID/ai/run                (model + input as body siblings, NOT in the path)
# Reading the result:
#   401 or 403 on direct = key problem. A missing key returns 403 (typesafe-ai/skills#8), not the documented 401.
#   422 = payload shape. Cloudflare needs a token with Workers AI Read + Edit.
# Sources: https://docs.typesafe.ai/api.md ; https://developers.cloudflare.com/ai/models/typesafe/jev/
set -euo pipefail

mode="${1:-direct}"
payload='{
  "state": "Help! My payouts have been failing for 3 days.",
  "questions": {
    "is_urgent":   {"type": "noul",   "instructions": "Does this convey urgency?"},
    "department":  {"type": "choice", "instructions": "Which team should handle this?",
                    "criteria": {"billing": "Payments, invoicing, refunds", "technical": "Bugs, outages, integrations", "other": null}},
    "frustration": {"type": "score",  "instructions": "How frustrated is the customer?",
                    "criteria": ["Calm", "Frustrated", "Very angry"]}
  }
}'

case "$mode" in
  direct)
    : "${TYPESAFE_API_KEY:?set TYPESAFE_API_KEY (create at https://console.typesafe.ai/keys)}"
    model="${TYPESAFE_DEFAULT_MODEL:-jev-latest}"
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
    body="{\"model\": \"typesafe/jev\", \"input\": ${payload}}"
    curl -sS -w '\nHTTP %{http_code}\n' \
      "https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run" \
      -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
      -H "Content-Type: application/json" \
      -d "$body"
    ;;
  *)
    echo "usage: $0 direct|cloudflare" >&2; exit 2 ;;
esac
