# sptobuff
Compares Skinport Prices to Buff.163
![program](/images/sptobuff.png) 

## How to use
1. Go to buff.163.com, and get your cookie value
    - Inspect element -> Network -> Domain: `Buff.163.com` -> File:  `/` -> Request Headers -> Cookie
    - Enter the cookie value into config.json
![network](/images/network.png) 
2. Run `sptobuff.exe`
3. Search a skin name and select from the list
4. Press Submit

## How to update the skin list
1. Install requirements
    - `pip install -r requirements.txt`
    - `Python 3.10.x`
2. Run `classes/getItemList.py`
3. After a while, the program will stop automatically due to rate limits.
    - Adjust the `start` variable to what the program outputed to start at when it ended.
    - This would start the search from where the program ended last

## Notes
1. Had request issues with `https://skinport.com/api/browse/730`, prices aren't as update to date as possible.
2. Skin list hasn't been updated, if you do so please send a PR.


![peko](https://c.tenor.com/yCXF2YPIXtwAAAAC/pekora-animeh.gif)
