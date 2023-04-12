import requests
def CNYtoUSD():
        URL = "https://www.freeforexapi.com/api/live?pairs=USDCNY"
        r=requests.get(URL).json()
        return float(1/r["rates"]["USDCNY"]["rate"])
class Buff:       
    rate = CNYtoUSD()
    def __init__(self, header):
        self.header = {
            "Cookie": str(header)
        }
    def getBuffPrice(self, itemname):
        URL = "https://buff.163.com/api/market/goods"
        params = {
            "game" : "csgo",
            "page_num" : "1",
            "search" : str(itemname)
        }
        r = requests.get(URL, params=params, headers=self.header).json()
        priceCNY = r["data"]["items"][0]["sell_min_price"]
        priceUSD = float(priceCNY)  * self.rate
        return round(priceUSD, 2)
