#/bin/bash

# Base URL of the web application
BASE_URL="http://127.0.0.1:5000"

# Fetch all transactions
fetch_transactions() {
  echo "Fetching all transactions"
  curl -s "${BASE_URL}/transactions" | jq
}

# Fetch balance for a user
fetch_balance() {
  USER=$1
  echo "Fetching balance for user: $USER"
  curl -s "${BASE_URL}/balance?userId=${USER}" | jq
}

# example of unsafe txn
unsafe_txn() {
  SENDER=$1
  RECEIVER=$2
  AMOUNT=$3
  TIMESTAMP=$(date +%s)  # Current timestamp in seconds

  echo "Unsafely transferring $AMOUNT from $SENDER to $RECEIVER"
  RESPONSE=$(curl -s -X POST "${BASE_URL}/unsafetransaction" \
    -H "Content-Type: application/json" \
    -d "{
      \"fromId\": \"${SENDER}\",
      \"toId\": \"${RECEIVER}\",
      \"amount\": ${AMOUNT}
    }")
  echo "Response: $RESPONSE"
}

fetch_balance 0
fetch_balance 1

unsafe_txn 0 1 100

fetch_balance 0
fetch_balance 1

fetch_transactions
