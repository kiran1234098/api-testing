from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://www.linkedin.com/")
time.sleep(10)

try:
    element = driver.find_element(By.ID, "username") or driver.find_element(By.NAME, "session_key")
except NoSuchElementException:
    # If element with ID "username" is not found, locate the element by name "session_key"
    element = driver.find_element(By.NAME, "session_key") or driver.find_element(By.NAME, "session_key")
element.send_keys("cs1754.iiitbhopal@gmail.com")
time.sleep(10)
some=driver.find_element(By.ID,"session_password")
some.send_keys("Hbiboras123@")
some.send_keys(Keys.ENTER)
time.sleep(10)




