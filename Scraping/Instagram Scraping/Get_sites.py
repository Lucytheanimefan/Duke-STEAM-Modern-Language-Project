'''
Created on Mar 17, 2016
Get many Instagram urls
@author: lucy
'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import bs4
'''
CLIENT_ID='4364f2b6963b4592916a5e7b705eeb65'
client_secret='dc8f51dcfcfc4a89b466707d1ee5b275'
access_token='3039584474.4364f2b.086a1a1ce4564d218067ef62f5d69553'

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="dango_ramen", access_token=access_token,count = 10)
for media in recent_media:
    print media.caption.text
'''
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver):
    driver.get("https://www.instagram.com/nytimes/")
    try:
        button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name("_fuu7c _345gm coreSpriteSpeechBubbleSmall"))
        #button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("edit-submit"))
        #box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found")
    
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    #driver.quit()