# sptobuff
Compares Skinport Prices to Buff.163
### How to use
1. Install requirements </br>
`
    pip install -r requirements.txt
`
2. Go to buff.163.com, and get your cookie value
    - Inspect element -> Network -> Domain: Buff.163.com -> Request Headers -> Cookies
    - Enter the cookie value into config.json
    <br/>

    
    ![network](/images/network.png) 
3. Go to skinport.com, and get your __cf_bm and _csrf value
    - Inspect element -> Network -> Domain: skinport.com -> Request Headers -> Cookies
    - Enter the __cf_bm and _csrf value into config.json
1. Run flask server from main.py
    - If you want to get an updated list of skins, run [itemList.py](classes/getItemList.py)
    - This might need to be run multiple times due to request rates, so change start values based off where the errors left off.
2. Go to http://127.0.0.1:5000/
3. Enter a skin name in the textfield
4. Press submit
<br/>
*For the most up to date prices, going to the websites is still the best way.*
<br/>
<br/>
<br/>

![input](/images/spToBuffInput.png)

![results](/images/spToBuffResults.png)

![peko](https://c.tenor.com/yCXF2YPIXtwAAAAC/pekora-animeh.gif)
