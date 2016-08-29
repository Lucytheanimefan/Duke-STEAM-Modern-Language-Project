'''
Created on Mar 17, 2016
Script to get the reaction count of posts
@author: lucy
'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver, query):
    driver.get("https://www.facebook.com/nytimes/?fref=ts")
    try:
        box = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("edit-keys"))
        button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("edit-submit"))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found")
 
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "college")
    time.sleep(5)
    #driver.quit()