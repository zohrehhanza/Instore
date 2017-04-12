
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
import pymongo

uri = 'mongodb://instore2:123abc@ds159050.mlab.com:59050/in-store'
client = pymongo.MongoClient(uri)
db = client.get_default_database()
products = db['products']
store_n='IGA'

# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\selenium\\chromedriver.exe', chrome_options=option)

# go to website of interest
#browser.get("https://www.iga.net/en/online_grocery/browse/in-flyer")
browser.get("https://www.iga.net/en/online_grocery/browse/in-flyer?page=27&pageSize=60")

#print('finish')
ii=0
Prices = []
Description=[]
for i in range(15):
    my_url = browser.current_url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "js-equalized-sub-item push-half--bottom"})
    price = page_soup.findAll("span", {"class": "price text--strong"})

    for j in range(len(containers)):  # t in titles:
    #Description.append(' '.join(containers[i].text.replace('\r\n', '').replace('\n', '').split()))
    #Prices.append(price[i].text.strip())

         products.insert({"store" : store_n,  "price" : price[j].text.strip() , 'description' : (' '.join(containers[j].text.replace('\r\n', '').replace('\n', '').split()))})
         ii=ii+1
    clicked_page = browser.find_element_by_class_name("icon--arrow-skinny-right").click()
#db.products.createIndex({"store": "text", "description": "text"})
#print(j)
#date = page_soup.find("div",{"class":"island__container map-colors-bases-white"})
#print(Description)