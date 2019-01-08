import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def login():
    driver.get("https://www.twitter.com/login")
    time.sleep(3)
    login_field = driver.find_element_by_class_name("js-username-field")
    login_field.clear()
    login_field.send_keys("*Your Username*")
    password_elem = driver.find_element_by_class_name("js-password-field")
    password_elem.clear()
    password_elem.send_keys("*Your Password*")
    password_elem.submit()
    time.sleep(1)


def Search_Hashtags():
    driver.get("https://twitter.com/search-advanced")
    time.sleep(2)
    search_field = driver.find_element_by_name("tag")
    search_field.send_keys(hashtags)
    time.sleep(2)
    search_field.submit()
    time.sleep(1)

def Like_Photo():
    pic_hrefs = []
    for i in range(1, 20):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                if '.com/p/' in elem.get_attribute('href')]
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
        except Exception:
            continue


hashtags = ["#anonymous", " #adventure", " #funny", " #follow",
            " #friends", " #cyber", " #cybersecurity", " #followme",
            " #like", " #likephoto", " #tweet", " #world", " #news" ]

login()
Search_Hashtags()
Like_Photo()
