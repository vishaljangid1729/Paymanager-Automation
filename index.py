from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert





driver = webdriver.Chrome()

driver.get("http://164.100.153.22/paymanager/")

username = driver.find_element_by_id("MyCaptcha_Email")
# username.clear()
username.send_keys("07045237")
password = driver.find_element_by_id("MyCaptcha_Passwd")
password.send_keys("Tharwan@3")



intput_captcha = input("Type the given captcha: ")


captcha = driver.find_element_by_id("MyCaptcha_TxtCpatcha")
captcha.send_keys(intput_captcha)


login_button = driver.find_element_by_id("MyCaptcha_btnddologin")

login_button.click()

# check box tick

check_box = driver.find_element_by_id("chk")
check_box.click()

take_me_web_button = driver.find_element_by_id("Btn")
take_me_web_button.click()

# inside web

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Bill Processing"))




