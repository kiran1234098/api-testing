from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

website = 'https://www.linkedin.com/'
path = 'chromedriver'

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get(website) 
print(driver.title)# get title of the page
print(driver.current_url) # url of  the page
# Wait until the page is fully loaded
# Wait until the email input field is visible and enabled
wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email or phone")))
wait.until(EC.element_to_be_clickable((By.ID, "username")))
# Find the element using XPath
# Find the element using XPath
element = driver.find_element(By.XPATH, "//*[@id='session_key']")
element.send_keys("cs1754.iiitbhopal@gmail.com")
driver.close()