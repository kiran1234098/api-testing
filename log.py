import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set up logging
logging.basicConfig(level= logging.INFO,filename='selenim.log',filemode='w')
logger=logging.getLogger()
# create chromedriver instanse
option =Options()
driver=webdriver.Chrome(options=option)

driver.get("")

logger.info("logiing")

username_input=driver.find_element(By.ID)
username_pass = driver.find_element(By.ID,'')
button_log = driver.find_element(By.ID,)

username_input.send_keys("")
username_pass.send_keys('')
button_log.click()

logger.info("varify")

welcome_massage =driver.find_element(By.ID)
assert welcome_massage.text == 'welcome kiran'
driver.quit()