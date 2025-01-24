#/bin/bash

# Base URL of the web application
BASE_URL="http://127.0.0.1:5000"
USER0_COOKIE=""

# Generate a unique nonce
generate_nonce() {
  uuidgen
}

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

auth() {
  USERID=$1
  PASSWORD=$2
  NONCE=$(generate_nonce) 
  echo "Authentication for user $USERID" 
  RESPONSE=$(curl -s -X POST "${BASE_URL}/authenticate" \
    -H "Content-Type: application/json" \
    -d "{
      \"userid\": \"${USERID}\",
      \"password\": \"${PASSWORD}\",
      \"nonce\": \"${NONCE}\"
    }")
  echo "Response: $RESPONSE"

  # Extract the cookie from the response
  COOKIE=$(echo "$RESPONSE" | jq -r '.cookie')
  
  # Check if the cookie extraction was successful
  if [ "$COOKIE" != "null" ]; then
    echo "Authentication successful for user $USERID. Cookie: $COOKIE"
    
    # Store the cookie in a global variable (adjust based on user)
    if [ "$USERID" == "0" ]; then
      USER0_COOKIE=$COOKIE
    fi
  else
    echo "Authentication failed for user $USERID"
  fi
}

# Transfer money between users
safe_txn() {
  SENDER=$1
  RECEIVER=$2
  AMOUNT=$3
  TIMESTAMP=$(date +%s)  # Current timestamp in seconds
  NONCE=$(generate_nonce)  # Generate a unique nonce

  echo "Transferring $AMOUNT from $SENDER to $RECEIVER"
  RESPONSE=$(curl -s -X POST "${BASE_URL}/safetransaction" \
    -H "Content-Type: application/json" \
    -d "{
      \"fromId\": \"${SENDER}\",
      \"toId\": \"${RECEIVER}\",
      \"amount\": ${AMOUNT},
      \"timestamp\": ${TIMESTAMP},
      \"nonce\": \"${NONCE}\",
      \"cookie\": \"${USER0_COOKIE}\"
    }")
  echo "Response: $RESPONSE"
}

fetch_balance 0
fetch_balance 1

auth 0 "password"
safe_txn 0 1 100

fetch_balance 0
fetch_balance 1

fetch_transactions
