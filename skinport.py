import requests

def getSkinportPrice(itemname):
    r = requests.get("https://api.skinport.com/v1/items", params={
        "app_id": 730,
        "currency": "USD",
        "tradable": 1
    }).json()
    outputRequest = [x for x in r if x['market_hash_name'] == itemname]
    for i in outputRequest:
        return i['min_price']



