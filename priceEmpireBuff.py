from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

s = Service(r'chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(service=s, options=options)


def getBuffPrice(itemname):
    URL = "https://pricempire.com/search?q=" + str(itemname)
    driver.get(URL)
    time.sleep(2.5)
    listings = driver.page_source
    soup = BeautifulSoup(listings, "html5lib")
    # Gets the item link
    item = soup.find(title=str(itemname))
    itemhref = item.get('href')
    URL2 = "https://pricempire.com" + itemhref
    # Goes to item page and gets price
    driver.get(URL2)
    time.sleep(2.5)
    itempage = driver.page_source
    soup2 = BeautifulSoup(itempage, "html5lib")
    buffListing = soup2.find('a', href=re.compile("buff163"))
    buffPrice = buffListing.find('div', class_="price color-price").getText()
    buffPrice = buffPrice.replace('$', '')
    buffPrice = buffPrice.replace('\n', '')
    return float(buffPrice)

