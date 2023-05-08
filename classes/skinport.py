import requests
import json
def getSkinportPrice(itemname):
    url = "https://api.skinport.com/v1/items?app_id=730&currency=USD&tradable=0"
    response = requests.get(url)
    data = json.loads(response.content)
    output_dict = [x for x in data if x['market_hash_name'] == itemname]
    return output_dict[0]["min_price"]