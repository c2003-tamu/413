from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import random, uuid, time

"""
sample bank app, has users and transactions

users can send transactions between themselves and other users, just sending money to/from account for simplicity

for simplicity, users and txns will be stored in memory rather than in a db

"""

app = Flask(__name__)

users = {
	0:{"name" : "Cade Royal", "balance": random.randint(1000,2000), "password": generate_password_hash("password"), "valid_cookie": None, "last_auth": None},
	1:{"name" : "LeBron James", "balance": random.randint(10000, 20000), "password": generate_password_hash("password"), "valid_cookie": None, "last_auth": None}
}

transactions = []

# Define nonces - a set of uuid's that can only be used once
used_nonces = set()

"""
ROUTE - /authenticate
METHOD(S) - POST
QUERY PARAMS - none
"""
@app.route('/authenticate', methods=['POST'])
def auth():
	data = request.json
	userid = int(data.get('userid', None))
	password = data.get('password', None)
	nonce = data.get('nonce', None)
	if userid == None or password == None or nonce == None:
		return jsonify({"error": "Invalid request"}), 400
	try:
		if check_password_hash(users[userid]["password"], password) and nonce not in used_nonces:
			valid_cookie = str(uuid.uuid4())
			users[userid]["valid_cookie"] = valid_cookie
			users[userid]["last_auth"] = time.time()
			used_nonces.add(nonce)
			return jsonify({"message": "SUCCESS", "cookie": valid_cookie})
		else:
			return jsonify({"error": "Invalid userid or password"}), 403
	except Exception as e:
		return jsonify({"error": "Invalid userid or password"}), 403
		

"""
ROUTE - /transactions
METHOD(S) - GET
QUERY PARAMS - none
"""
@app.route('/transactions', methods=['GET'])
def gettransactions():
	return jsonify({"transactions": transactions})


"""
ROUTE - /balance
METHOD(S) - GET
QUERY PARAMS - userId
"""
@app.route('/balance', methods=['GET'])
def balance():
	userId = int(request.args.get('userId'))
	return jsonify({"name": users[userId]["name"], "balance": users[userId]["balance"]})

"""
ROUTE - /unsafetransaction
METHOD(S) - POST
QUERY PARAMS - none
"""
@app.route('/unsafetransaction', methods=['POST'])
def unsafetransaction():
	data = request.json
	fromId = int(data.get('fromId', None))
	toId = int(data.get('toId', None))
	amount = int(data.get('amount', None))

	users[fromId]["balance"] -= amount
	users[toId]["balance"] += amount
	
	transactions.append({
		"fromId": fromId,
		"toId": toId,
		"amount": amount
	})

	return jsonify({"message": "SUCCESS", "from": users[fromId]["name"], "to": users[toId]["name"]})


# Define the appropriate time window for txns, in this case 5 mins
time_window = 5 * 60

"""
ROUTE - /safetransaction
METHOD(S) - POST
QUERY PARAMS - fromId, toId, amount
"""
@app.route('/safetransaction', methods=['POST'])
def safetransaction():
	data = request.json
	fromId = int(data.get('fromId', None))
	toId = int(data.get('toId', None))
	amount = int(data.get('amount', None))
	timestamp = data.get('timestamp', None)	
	nonce = data.get('nonce', None)	
	cookie = data.get('cookie', None)

	if fromId not in users or toId not in users:
		return jsonify({"error": "Invalid sender or receiver"}), 400
	
	current_time = time.time()
	if abs(current_time - timestamp) > time_window:
		return jsonify({"error": "timestamp invalid or expired"}), 400

	if abs(current_time - users[fromId]["last_auth"]) > time_window:
		return jsonify({"error": "auth invalid or expired"}), 400

	if nonce in used_nonces:
		return jsonify({"error": "Nonce already used"}), 400
	
	if users[fromId]["valid_cookie"] != cookie:
		return jsonify({"error": "auth invalid or expired"}), 400
	
	used_nonces.add(nonce)

	users[fromId]["balance"] -= amount
	users[toId]["balance"] += amount
	
	transactions.append({
		"fromId": fromId,
		"toId": toId,
		"amount": amount,
		"timestamp": timestamp,
		"nonce": nonce	
	})
	return jsonify({"message": "SUCCESS", "from": users[fromId]["name"], "to": users[toId]["name"]})


if __name__ == '__main__':
	app.run()
