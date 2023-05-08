import requests
import json

class Skinport:
    def __init__(self):
        self.data = self.initRequest()
    def initRequest(self):
        response = requests.get("https://api.skinport.com/v1/items?app_id=730&currency=USD&tradable=0")
        print('runs')
        return json.loads(response.content)
    def getSkinportPrice(self, itemname):
        output_dict = [x for x in self.data if x['market_hash_name'] == itemname]
        return output_dict[0]["min_price"]