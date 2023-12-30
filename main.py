from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Cookie clicker game link
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Select language (English)
time.sleep(3) #delay program for 3 seconds so it can select language
driver.find_element(by=By.ID, value="langSelect-EN").click()
time.sleep(3)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/a[1]").click()

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="bigCookie")

timeout = time.time() + 4
upgrade_time = time.time() + 10
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click ()

    # check every 11.2 sekonds to buy products
    if time.time () > timeout:
        add_ons_list = driver.find_elements(by=By.CSS_SELECTOR, value="#products .unlocked.enabled")
        add_ons_list[-1].click()
        timeout = time.time () + 11.2
    # check every 18 sekonds to buy upgrades
    if time.time() > upgrade_time:
        upgrade = driver.find_element(by=By.ID, value="upgrade0")
        upgrade.click()
        upgrade_time = time.time() + 18

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time () > five_min:
        cookie_sec = driver.find_element (By.ID, "cookiesPerSecond").text
        print (f"cookies {cookie_sec}")
        break
