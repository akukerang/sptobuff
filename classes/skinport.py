import requests

def getSkinportPrice(itemname,s_csrf,s__cf_bm):
    if 'AK-47' in itemname or 'M4A4' in itemname or 'M4A1-S' in itemname or 'FAMAS' in itemname or 'Galil AR' in itemname or 'AWP' in itemname or 'G3SG1' in itemname or 'AUG' in itemname or 'Scar-20' in itemname or 'SG 553' in itemname or 'SSG 08' in itemname:
        weapontype = 'Rifle'
    elif 'R8 Revolver' in itemname or 'Dual Berettas' in itemname or 'Desert Eagle' in itemname or 'Glock-18' in itemname or 'P2000' in itemname or 'USP-S' in itemname or 'P250' in itemname or 'CZ75-Auto' in itemname or 'Tec-9' in itemname or 'Five-Seven' in itemname:
        weapontype = 'Pistol'
    elif 'MP7' in itemname or 'MP9' in itemname or 'PP-Bizon' in itemname or 'P90' in itemname or 'UMP-45' in itemname or 'MAC-10' in itemname or 'MP5-SD' in itemname:
        weapontype = 'SMG'
    elif 'Mag-7' in itemname or 'Sawed-Off' in itemname or 'Nova' in itemname or 'XM1014' in itemname or 'Negev' in itemname or 'M249' in itemname:
        weapontype = 'Heavy'
    elif 'Gloves' in itemname or 'Hand Wraps' in itemname:
        weapontype = 'Gloves'
    else:
        weapontype = 'Knife'
    types = itemname.split(" | ")[0]
    skin = itemname.split(" | ")[1].split(" (")[0]
    condition = itemname.split(" (")[1][:-1]
    if condition ==  "Factory New":
        exteriorid = 2
    elif condition == "Minimal Wear":
        exteriorid = 4
    elif condition == "Field-Tested":
        exteriorid = 3
    elif condition == "Well-Worn":
        exteriorid = 5
    elif condition == "Battle-Scarred":
        exteriorid = 1
    else:
        print("Condition Error")
        print(condition)
    cookies = {
    '__cf_bm': s__cf_bm,
    '_csrf': s_csrf,
    
}
    if "StatTrak" in itemname:
        types = types.split("StatTrak™ ")[1]
        st = 1
    elif "★" in itemname:
      types = types.replace("★ ","")
      st = 0
    else:
      st = 0
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://skinport.com/market?cat=Pistol&type=USP-S&item=Target+Acquired',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
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

