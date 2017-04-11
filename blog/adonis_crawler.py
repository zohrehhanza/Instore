
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
#Urls  = ["https://www1.pharmaprix.ca/en/flyer", "http://groupeadonis.ca/CMS/index.php/en/les-surgeles-2", "https://www.iga.net/en/online_grocery/browse/Grocery/in-flyer"]
#String url = driver.getCurrentUrl()
browser.get("http://groupeadonis.ca/en/")
clicked_area = browser.find_element_by_id("regionSendQC").click()
page_flyers = browser.find_element_by_xpath("//*[@id='ul-root']/li[4]/a").click()
print('finish')
#browser.maximize_window() #For maximizing window
#browser.implicitly_wait(20)
#clicked_flyer = browser.find_element_by_xpath("/html/body/div[11]/div[1]/div/div[6]/div[1]/a[1]").click()
#clicked_flyer = browser.find_element_by_xpath("/html/body/div[11]/div[1]/div/div[6]/div[1]/a[1]").click()
list_products = []
for i in range(9):
    clicked_page = browser.find_element_by_class_name("circ-nav-next").click()
    my_url = browser.current_url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div",{"class":"ribbon"})
    titles = page_soup.findAll("h2")
#print(len(containers))
#print(containers[0].text)
    for i in range(len(containers)):# t in titles:
        list_products.append(containers[i].text.strip()+':'+titles[i].text.strip())

date = page_soup.find("h1")
print(date.text.strip())
print(list_products)
print(len(list_products))
        # print(containers[i].text.strip()+':'+titles[i].text.strip())

#for title in titles:
 #   print(title.text)

    #print(title.text)
#for  j in range(15):
#    key_flyer = browser.find_element_by_tag_name("h2")
 #   value_flyer = browser.find_element_by_class_name("item-txt")
  #  print(str(key_flyer) +','+ str(value_flyer))
#= browser.find_element_by_tag_name("img").click()
#keys_element = browser.find_elements_by_class_name("name")
#keys = [x.text for x in specific_flyer]  # same concept as for-loop/list-comprehension above
#print('keys')
#print(keys, '\n')

# get all of the financial values themselves
#values_element = browser.find_elements_by_class_name("ribbon")
#values = [x.text for x in values_element]  # same concept as for-loop/list-comprehension above
#print('values')
#print(values, '\n')


#pair each title with its corresponding value using zip function and print each pair
#for key, value in zip(keys, values):
 #   print(key + ': ' + value)

