from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "EMAIL ADDRESS USED TO LOG INTO FACEBOOK"
FB_PASSWORD = "PASSWORD USED TO LOG INTO FACEBOOK"

#To prevent chrome from shutting down
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH,value='/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
fb_login.click()

tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(2)
email_field = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
email_field.send_keys(FB_EMAIL)

password_field = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password_field.send_keys(FB_PASSWORD)

fb_login_button = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
fb_login_button.click()

input("Press enter after completing captcha")

driver.switch_to.window(tinder_window)
print(driver.title)

sleep(5)
allow_location = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]/div[2]/div[2]")
allow_location.click()

sleep(5)
no_notifs = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]/div[2]/div[2]")
no_notifs.click()

sleep(5)
cookies = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div")
cookies.click()

for n in range(100):
    sleep(2)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/div/main/div/div/div/div/div[4]/div/div[4]/button/span/span[1]')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            sleep(2)
