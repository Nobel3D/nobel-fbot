from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

fb_email = "YOUR_EMAIL"
fb_pass = "YOUR_PASS"
fb_message = "YOUR_MESSAGE"
fb_post = "YOUR_POST"
 
def fb_login():
    browser.get("https://www.facebook.com")
    time.sleep(5)
    email = browser.find_element_by_id("email")
    email.send_keys(fb_email)
    pwd = browser.find_element_by_id("pass")
    pwd.send_keys(fb_pass)
    login = browser.find_element_by_id("loginbutton")
    login.click()
    time.sleep(5)

def fb_page():
    browser.get(fb_post)
    
    
def fb_comment():
    browser.find_element_by_class_name("_5rpu")
    textbox.send_keys(fb_message)
    textbox.send_keys(Keys.ENTER)
    textbox.clear()
    
browser = webdriver.Firefox()
fb_login()
fb_page()
fb_comment()
