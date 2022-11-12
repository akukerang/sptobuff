import requests

def getSkinportPrice(itemname):
    params = {
        "market_hash_name": str(itemname),
        "app_id": 730,
        "currency": "USD"
    }
    r = requests.get("https://api.skinport.com/v1/sales/history", params = params).json()
    return float(r[0]['last_30_days']['avg'])



