# launches FireFox browser and navigates to Peleton Login page
# Sample automation script to test logging in with valid and invalid tests
# Then navigating to 'Shop'-> Option->Add to cart page

import os
import webbrowser
from StdSuites import seconds


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get("https://www.onepeloton.com/login")

#writing tests for incorrect login, then valid login for username and password
# 1st test - invalid email, valid password
# 2nd test - invalid email and invalid password

#Test 1 invalid username
elem = browser.find_element_by_name("usernameOrEmail")
elem.clear()
elem.send_keys("qa@gmail.com")

elem = browser.find_element_by_name("password")
elem.clear()
elem.send_keys("ILoveToRide")
elem.send_keys(Keys.RETURN)

#Test 2 invalid password
elem = browser.find_element_by_name("usernameOrEmail")
elem.clear()
elem.send_keys("pelotonqa@gmail.com")

elem = browser.find_element_by_name("password")
elem.clear()
elem.send_keys("11111")
elem.send_keys(Keys.RETURN)

#Test with valid username and password
elem = browser.find_element_by_name("usernameOrEmail")
elem.clear()
elem.send_keys("pelotonqa@gmail.com")

elem = browser.find_element_by_name("password")
elem.clear()
elem.send_keys("ILoveToRide")
elem.send_keys(Keys.RETURN)


browser.implicitly_wait(2)

#login is completed and app is at user's account page
#Click 'Shop' menu item
elem.find_element_by_xpath("//a[@href='/shop']").click()

#Select option to put in cart...

#elem.find_element_by_xpath("//a[@href='/shop/bike/configure']").click()
#elem.findElement(By.linkText("Order yours")).click()
#elem.find_element_by_xpath("//*[contains(@href,'/shop/bike/configure')]").click()

browser.get("https://www.onepeloton.com/shop/bike/configure")

#elem.find_element_by_link_text("Add to Cart").click()
#elem.find_element_by_class_name("sc-fjhmcy hNLgig").click()

elem.find_element_by_xpath("//button[text()='Add to Cart']").click()

