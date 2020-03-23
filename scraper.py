import os
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# need to install selenium AND WEBDRIVER (I have chromewebdriver)



def open_site(website, product):
    ''' opens website with selenium's find elem '''

    url = str(website)
    searchfor = str(product)

    user_path = os.path.expand('~')
    # only on mac, if windows -> change the path to C:\\ 
    browser = webdriver.Chrome(user_path + '/Downloads/chromedriver')

    browser.get(url)

    searchbox = browser.find_element_by_name('search')

    searchbox.send_keys(searchfor)
    searchbox.send_keys(Keys.ENTER)
    