from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

time.sleep(2)
login_button_1 = driver.find_element(by=By.CLASS_NAME, value='lxn9zzn')
login_button_1.click()

time.sleep(2)
more_options_button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
login_button_1.click()

time.sleep(2)
facebook_button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
facebook_button.click()