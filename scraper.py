import os
import re
import requests
import fuckit # error steamroller
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# need to install selenium AND WEBDRIVER (I have chromewebdriver)


def website_list_loop(website_list, product):

    for website in website_list:
        print('get searched, son', website)
        search_site(website, product)
    return 'loopty'

def search_site(website, product="mens slim jeans"):
    ''' opens website with selenium's find elem '''

    url = str(website)
    searchfor = str(product)
   
    # getting the iphone content version (hopefully less content)
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}

    options=Options()
    options.page_load_strategy = 'eager' # waits only til html is loaded and parsed, no stylesheets, images etc


    username = os.path.expanduser('~')
     # only on mac, if windows -> change the path to C:\\ 
    download_path = username + '/Downloads/chromedriver'
    browser = webdriver.Chrome(download_path, options=options)

    browser.get(url)
    # browser.set_page_load_timeout(10)

    product_price = {}

    # this is super inefficient and annoying to copypasta if you know of a better way Let me know!
    # If there is a search box on the site - I am assuming it is the first input element or form element.. not perfect but makes sense, right? 
    # attempt at every possible way a website may have named its search box !! 
    # try:
    #     browser.find_element_by_name('search')
    #     searchbox = browser.find_element_by_name('search')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    # except selenium.common.exceptions.NoSuchElementException: 
    #     pass

    # elif browser.find_element_by_name('search-input'):
    #     searchbox = browser.find_element_by_name('search-input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_name('searchbox'): 
    #     searchbox = browser.find_element_by_name('searchbox')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_name('search-box'): 
    #     searchbox = browser.find_element_by_name('search-box')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('searchbar'):
    #     searchbox = browser.find_element_by_name('searchbox')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_name('search-bar'): 
    #     searchbox = browser.find_element_by_name('search-bar')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('input'): 
    #     searchbox = browser.find_element_by_name('input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('keyword'): 
    #     searchbox = browser.find_element_by_name('keyword')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_name('key-word'): 
    #     searchbox = browser.find_element_by_name('key-word')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_name('key-words'): 
    #     searchbox = browser.find_element_by_name('key-words')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_name('keywords'): 
    #     searchbox = browser.find_element_by_name('keywords')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('keywordSearch'):
    #     searchbox = browser.find_element_by_name('keywordSearch')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER) 

    # elif browser.find_element_by_name('globalSearchInputField'): 
    #     searchbox = browser.find_element_by_name('globalSearchInputField')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('globalSearch'): 
    #     searchbox = browser.find_element_by_name('globalSearchInput')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('globalSearchInput'): 
    #     searchbox = browser.find_element_by_name('globalSearchInput')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_name('globalSearchField'): 
    #     searchbox = browser.find_element_by_name('globalSearchField')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)


    # elif browser.find_element_by_id('search'):
    #     searchbox = browser.find_element_by_id('search')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_id('search-input'):
    #     searchbox = browser.find_element_by_id('search-input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_id('searchbox'):
    #     searchbox = browser.find_element_by_id('searchbox')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_id('searchbar'):
    #     searchbox = browser.find_element_by_id('searchbar')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_id('input'):
    #     searchbox = browser.find_element_by_id('input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_id('globalSearchInputField'):
    #     searchbox = browser.find_element_by_id('globalSearchInputField')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER) 

    # elif browser.find_element_by_id('globalSearch'): 
    #     searchbox = browser.find_element_by_id('globalSearch')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_id('globalSearchInput'):
    #     searchbox = browser.find_element_by_id('globalSearchInput')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER) 

    # elif browser.find_element_by_id('globalSearchField'): 
    #     searchbox = browser.find_element_by_id('globalSearchField')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)



    # elif browser.find_element_by_tag_name('input'):
    #     searchbox = browser.find_element_by_tag('input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_tag_name('form'):
    #     searchform = browser.find_element_by_tag_name('form')
    #     searchbox = searchform.find_element_by_tag_name('input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)


    # elif browser.find_element_by_class_name('globalSearchInputField'): 
    #     searchbox = browser.find_element_by_class_name('globalSearchInputField')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_class_name('keyword'):
    #     searchbox = browser.find_element_by_class_name('keyword')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_class_name('keywords'):
    #     searchbox = browser.find_element_by_class_name('keywords')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_class_name('search'):
    #     searchbox = browser.find_element_by_class_name('search')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_class_name('searchbox'):
    #     searchbox = browser.find_element_by_class_name('searchbox')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_class_name('searchbar'):
    #     searchbox = browser.find_element_by_class_name('searchbar')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_class_name('input'):
    #     searchbox = browser.find_element_by_class_name('input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)


    
    # elif browser.find_element_by_css_selector('p.search'):
    #     searchbox = browser.find_element_by_css_selector('p.search')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_css_selector('p.searchbox'):
    #     searchbox = browser.find_element_by_css_selector('p.searchbox')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_css_selector('p.searchbar'):
    #     searchbox = browser.find_element_by_css_selector('p.searchbar')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_css_selector('p.input'):
    #     searchbox = browser.find_element_by_css_selector('p.input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)
    
    # elif browser.find_element_by_css_selector('p.search-input'):
    #     searchbox = browser.find_element_by_css_selector('p.search-input')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)

    # elif browser.find_element_by_css_selector('p.keywords'):
    #     searchbox = browser.find_element_by_css_selector('p.keyword')
    #     searchbox.send_keys(searchfor)
    #     searchbox.send_keys(Keys.ENTER)





    # FUCKIT ignores errors and moves on with the code. 
    # try else would have taken me too long but are effectively the same as fuckit module

    with fuckit:

        # TIMING TO AVOID BOT DENIAL ?? time.sleep(2)
        browser.find_element_by_name('search')
        searchbox = browser.find_element_by_name('search')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

        # options2 = webdriver.ChromeOptions()
        # options2.add_argument('--ignore-certificate-errors')
        # options2.add_argument("--test-type")
        # options2.binary_location = "/usr/bin/chromium"
        # browser.save_screenshot('screenshot.png', chrome_options = options2)

        # do i need to reassign the new url? guess not
        print('current url', browser.current_url)

        # tag = browser.find_elements_by_tag_name('p')
        # tag2 = browser.find_elements_by_tag_name('a')

        # tag3 = browser.find_elements_by_class_name('prod_price')
        # tag4 = browser.find_elements_by_tag_name('span')

        # browser.find_elements_by_class_name('productPrice')
        # browser.find_elements_by_class_name('product-Price')
        # browser.find_elements_by_class_name('productprice')
        # browser.find_elements_by_class_name('Price')
        # price = browser.find_elements_by_class_name('price')
        # price2 = browser.find_elements_by_id('price')

        # browser.find_elements_by_class_name('prod_price')
        # browser.find_elements_by_class_name('prod_Price')

        # for item in price:
        #     print(item.text)

        # for item in tag4:
        #     print(item.text)

        # SOUP scrape
        page_response = requests.get(browser.current_url, headers=headers)
        page_content = bs(page_response.content, "html.parser")
        print(page_content.prettify)
        ul_lists = page_content.find_all('div')
        # print(ul_lists)


        # REGEX TRIAL 
        # pattern = re.compile(r'[0-9][0-9][1-9]\.[0-9][0-9]?')
        # match = pattern.findall(str(page_content))

        # i=0
        # for m in match:
        #     if i < 10:
        #         print(m)
        #         i += 1
        
        # floats = re.findall("\d+\.\d+", str(page_content))
        # for num in floats:
        #     print(num)
        #     print(num.text)

        # If-statement after search() tests if it succeeded
        # if match:
        #     print('found', match.group()) ## 'found word:cat'
        # else:
        #     print('did not find')



        # browser.find_elements_by_name('price')
        # browser.find_elements_by_name('product')
        # browser.find_elements_by_name('product-price')
        # browser.find_elements_by_name('productprice')

        # browser.find_elements_by_class_name('price')
        # browser.find_elements_by_class_name('product')
        # browser.find_elements_by_class_name('product-price')
        # browser.find_elements_by_class_name('productprice')
        
        # browser.find_elements_by_id('price')
        # browser.find_elements_by_id('product')
        # browser.find_elements_by_id('product-price')
        # browser.find_elements_by_id('productprice')

        browser.quit()
        


    with fuckit:
        searchbox = browser.find_element_by_name('search-input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)
        

    
    with fuckit:
        searchbox = browser.find_element_by_name('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    
    with fuckit:
        searchbox = browser.find_element_by_name('search-box')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)


    with fuckit:
        searchbox = browser.find_element_by_name('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:
        searchbox = browser.find_element_by_name('search-bar')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)
   
    with fuckit:

        searchbox = browser.find_element_by_name('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('keyword')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)
    
    with fuckit:

        searchbox = browser.find_element_by_name('key-word')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('key-words')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('keywords')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('keywordSearch')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER) 
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchInputField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchInput')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchInput')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)


    with fuckit:

        searchbox = browser.find_element_by_id('search')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('search-input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('searchbar')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('globalSearchInputField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER) 
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('globalSearch')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('globalSearchInput')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER) 
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_id('globalSearchField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)



    with fuckit:

        searchbox = browser.find_element_by_tag('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchform = browser.find_element_by_tag_name('form')
        searchbox = searchform.find_element_by_tag_name('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)


    with fuckit:

        searchbox = browser.find_element_by_class_name('globalSearchInputField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_class_name('keyword')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_class_name('keywords')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_class_name('search')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_class_name('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_class_name('searchbar')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    with fuckit:

        searchbox = browser.find_element_by_class_name('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
        print(browser.current_url)

    browser.quit()
    return 'website'






    # else:
    #     print('Could not locate website search')
    #     return None

