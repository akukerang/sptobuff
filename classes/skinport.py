import requests
class skinport():
    def __init__(self):
        params = {
            "app_id": 730,
            "currency": "USD",
        }
        r = requests.get('https://api.skinport.com/v1/items' , params=params)
        self.data = r.json()
    def getSkinportPrice(self, itemname):
        selected =  [x for x in self.data if x['market_hash_name'] == itemname]
        return selected[0]['min_price']
