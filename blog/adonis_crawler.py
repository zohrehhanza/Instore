from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
######################################Connection with MongoDB#########################
import pymongo

uri = 'mongodb://instore2:123abc@ds159050.mlab.com:59050/in-store'
client = pymongo.MongoClient(uri)
db = client.get_default_database()
products = db['products']
store_n = 'Adonis'
store_loc = ['H7T 1R3','H4R OC9','H3H 1M9','H3C 2G6']
# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\selenium\\chromedriver.exe', chrome_options=option)

browser.get("http://groupeadonis.ca/en/")
clicked_area = browser.find_element_by_id("regionSendQC").click()
page_flyers = browser.find_element_by_xpath("//*[@id='ul-root']/li[4]/a").click()
print('finish')

list_products = []
for i in range(8):
    clicked_page = browser.find_element_by_class_name("circ-nav-next").click()
    my_url = browser.current_url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "ribbon"})
    titles = page_soup.findAll("h2")

    for i in range(len(containers)):  # t in titles:
        for j3 in store_loc:
        # list_products.append("store: Adonis"+",price:"+containers[i].text.strip()+',discription:'+titles[i].text.strip()+'+')
              products.insert({"store": store_n, "price": containers[i].text.strip(), 'description': titles[i].text.strip(),'location': j3})
              #jj = jj + 1
date = page_soup.find("h1")
# print(date.text.strip())
# print(list_products)
# print(len(list_products))
