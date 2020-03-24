import os
import requests
import fuckit # error steamroller
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# need to install selenium AND WEBDRIVER (I have chromewebdriver)


def website_list_loop(website_list, product):

    for website in website_list:
        search_site(website, product)


def search_site(website="https://www.safeway.com/", product="jeans"):
    ''' opens website with selenium's find elem '''

    url = str(website)
    searchfor = str(product)
   

    user_path = os.path.expanduser('~')
    # only on mac, if windows -> change the path to C:\\ 
    browser = webdriver.Chrome(user_path + '/Downloads/chromedriver')

    browser.get(url)

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





    # fuckit ignores errors and moves on with the code. 
    # try else would have taken me too long but are effectively the same as fuckit module

    with fuckit:
        browser.find_element_by_name('search')
        searchbox = browser.find_element_by_name('search')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

    with fuckit:
        searchbox = browser.find_element_by_name('search-input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    
    with fuckit:
        searchbox = browser.find_element_by_name('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    
    with fuckit:
        searchbox = browser.find_element_by_name('search-box')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

    with fuckit:
        searchbox = browser.find_element_by_name('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

    with fuckit:
        searchbox = browser.find_element_by_name('search-bar')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    
    with fuckit:

        searchbox = browser.find_element_by_name('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

    with fuckit:

        searchbox = browser.find_element_by_name('keyword')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    
    with fuckit:

        searchbox = browser.find_element_by_name('key-word')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_name('key-words')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_name('keywords')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_name('keywordSearch')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER) 
    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchInputField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchInput')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchInput')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_name('globalSearchField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

    with fuckit:

        searchbox = browser.find_element_by_id('search')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_id('search-input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_id('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_id('searchbar')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_id('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_id('globalSearchInputField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER) 
    with fuckit:

        searchbox = browser.find_element_by_id('globalSearch')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_id('globalSearchInput')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER) 
    with fuckit:

        searchbox = browser.find_element_by_id('globalSearchField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)


    with fuckit:

        searchbox = browser.find_element_by_tag('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchform = browser.find_element_by_tag_name('form')
        searchbox = searchform.find_element_by_tag_name('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)

    with fuckit:

        searchbox = browser.find_element_by_class_name('globalSearchInputField')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_class_name('keyword')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_class_name('keywords')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_class_name('search')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_class_name('searchbox')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_class_name('searchbar')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)
    with fuckit:

        searchbox = browser.find_element_by_class_name('input')
        searchbox.send_keys(searchfor)
        searchbox.send_keys(Keys.ENTER)







    # else:
    #     print('Could not locate website search')
    #     return None

search_site()
