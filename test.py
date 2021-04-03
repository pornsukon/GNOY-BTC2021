import requests
import json

# late limit 403 can not to request get
# module = "account"
# action = "tokentx"
address = "0xEcA19B1a87442b0c25801B809bf567A6ca87B1da"
# startblock = "0"
# endblock = "999999999"
# sort = "asc"
# apikey = "YourApiKeyToken"
# response = requests.get("https://api-ropsten.etherscan.io/api?module=" + module + "&action=" + action + "&address=" + address + "&startblock="+ startblock +"&endblock="+ endblock +"&sort="+ sort +"&apikey=" + apikey)
# res = response.json()  

def getResult(address):
    f = open(address + '.json',)
    data = json.load(f)
    result = []
    for res in data['result']:
        value = int(res["value"])*(10**-18)
        res_one = {
            "hash" : res["hash"],
            "from" : res["from"],
            "to" : res["to"],
            "value" : value
        }
        if res_one["from"] == "0x0000000000000000000000000000000000000000":
            continue
        elif res_one["to"] != address:
            result.append(res_one)
            # res_get = getResult(res_one["to"])
        elif res_one["from"] != address:
            result.append(res_one)
            # res_get = getResult(res_one["from"])
    f.close()
    return result

f = open(address + '.json',)
data = json.load(f)
result = []
a = 0
for res in data['result']:
    if a == 3: # just have 3 file for get data
        break
    value = int(res["value"])*(10**-18)
    res_one = {
        "hash" : res["hash"],
        "from" : res["from"],
        "to" : res["to"],
        "value" : value
    }
    if res_one["from"] == "0x0000000000000000000000000000000000000000":
        continue
    elif res_one["to"] != address:
        result.append(res_one)
        res_get = getResult(res_one["to"])
        result = result + res_get
        a += 1
    elif res_one["from"] != address:
        result.append(res_one)
        res_get = getResult(res_one["from"])
        result = result + res_get
        a += 1
  
f.close()
print(result)

