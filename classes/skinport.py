import requests

def getSkinportPrice(itemname):
    if 'AK-47' in itemname or 'M4A4' in itemname or 'M4A1-S' in itemname or 'FAMAS' in itemname or 'Galil AR' in itemname or 'AWP' in itemname or 'G3SG1' in itemname or 'AUG' in itemname or 'Scar-20' in itemname or 'SG 553' in itemname or 'SSG 08' in itemname:
        weapontype = 'Rifle'
    elif 'R8 Revolver' in itemname or 'Dual Berettas' in itemname or 'Desert Eagle' in itemname or 'Glock-18' in itemname or 'P2000' in itemname or 'USP-S' in itemname or 'P250' in itemname or 'CZ75-Auto' in itemname or 'Tec-9' in itemname or 'Five-Seven' in itemname:
        weapontype = 'Pistol'
    elif 'MP7' in itemname or 'MP9' in itemname or 'PP-Bizon' in itemname or 'P90' in itemname or 'UMP-45' in itemname or 'MAC-10' in itemname or 'MP5-SD' in itemname:
        weapontype = 'SMG'
    else:
        weapontype = 'Heavy'
    types = itemname.split(" | ")[0]
    skin = itemname.split(" | ")[1].split(" (")[0]
    condition = itemname.split(" (")[1][:-1]
    if condition ==  "Factory New":
        exteriorid = 2
    elif condition == "Minimal Wear":
        exteriorid = 4
    elif condition == "Field tested":
        exteriorid = 3
    elif condition == "Well-Worn":
        exteriorid = 5
    elif condition == "Battle-Scarred":
        exteriorid = 1
    else:
        print("Condition Error")
    cookies = {
        '__cf_bm': 'cawY=',
        'i18n': 'en',
        '_csrf': 'asc',
    }
    if "StatTrak" in itemname:
        types = types.replace("StatTrak™ ","")
        st = 1
    else:
        st = 0
    headers = {
        'authority': 'skinport.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://skinport.com/market',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    
    params = {
        'cat': f'{weapontype}',
        'item': f'{skin}',
        'sort': 'price',
        'order': 'asc',
        'type': f'{types}',
        'exterior': f'{exteriorid}',
        'stattrak': f'{st}'
    }

    response = requests.get('https://skinport.com/api/browse/730', params=params, cookies=cookies, headers=headers)
    r = response.json()

    return float(r['items'][0]['salePrice']/100)
