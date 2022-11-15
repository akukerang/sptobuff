# sptobuff
Compares Skinport Prices to Buff.163

### How to use
1. Run flask server from main.py
    - If you want to get an updated list of skins, run [itemList.py](classes/getItemList.py)
    - This might need to be run multiple times due to request rates, so change start values based off where the errors left off.
2. Go to http://127.0.0.1:5000/
3. Enter a skin name in the textfield
4. Press submit
    - The first run is the slowest, since Selenium needs to start up
    - But every run after should be faster
<br/>
*For the most up to date prices, going to the websites is still the best way.*
<br/>
<br/>
<br/>

![input](/images/spToBuffInput.png)

![results](/images/spToBuffResults.png)

![peko](https://c.tenor.com/yCXF2YPIXtwAAAAC/pekora-animeh.gif)
