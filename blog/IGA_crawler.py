
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys



# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path='C:\\Program Files\\Anaconda3\\selenium\\chromedriver.exe', chrome_options=option)

# go to website of interest
browser.get("https://www.iga.net/en/online_grocery/browse/in-flyer")

print('finish')

list_products_1 = []
for i in range(35):
    my_url = browser.current_url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div",{"class":"js-equalized-sub-item push-half--bottom"})
    titles = page_soup.findAll("span",{"class":"price text--strong"})

    for i in range(len(containers)):# t in titles:
        list_products_1.append(' '.join(containers[i].text.replace('\r\n','').replace('\n','').split())+': '+titles[i].text.strip())

    clicked_page = browser.find_element_by_class_name("icon--arrow-skinny-right").click()
date = page_soup.find("div",{"class":"island__container map-colors-bases-white"})
print(date.text.strip())
print(list_products_1)
print(len(list_products_1))


