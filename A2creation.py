from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.noon.com")

search = driver.find_element(By.ID,"searchBar")
search.send_keys("underwear")
search.send_keys(Keys.RETURN)

try:
    mains = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.CLASS_NAME, "sc-cb3f65f3-7"))
        EC.presence_of_element_located((By.CLASS_NAME, "WwCBf"))
    )
    # titles = main.find_element(By.CLASS_NAME,"sc-f8165ac8-15")
    # for main in mains:
    print(mains.text)
    # print(titles.text)
finally:
    driver.quit()
