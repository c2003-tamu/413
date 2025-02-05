import requests, time, uuid


server_url = "http://server:5000"
proxies = {
    "http": "http://mitm:8080",
    "https": "http://mitm:8080",
}

try:
  subreq = server_url+"/authenticate"
  print("requesting " + subreq)
  body = {"userid":0, "password":"password", "nonce":str(uuid.uuid4())}
  response = requests.post(subreq, json = body, proxies=proxies, verify=False)
  print("Response from Server:", response.text)
  response_json = response.json()
  
  cookie = response_json["cookie"]
  txn_body = {"fromId":0, "toId":1, "amount":100, "timestamp":time.time(), "nonce":str(uuid.uuid4()), "cookie":cookie}
  txn_req = server_url +"/safetransaction"
  txn_response = requests.post(txn_req, json=txn_body, proxies=proxies, verify=False)
  print("txn response: "+ txn_response.text)

except Exception as e:
  print("could not req "+ str(e))
