import logging
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

logging.basicConfig(level=logging.INFO,filename='log.txt',filemode="w")
logger=logging.getLogger()

driver = webdriver.Chrome()

try:
    #Open 
    driver.get()

    ele = driver.find_element()
    action = ActionChains(driver)
    action.move_to_element(ele).perform()

    #copy
    action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
    time.sleep(1)
    action.key_down(Keys.CONTROL).send_keys("v").key_up(keys.CONTROL)
    time.sleep(1)
    input_data = driver.find_element(By.ID,"")
    assert copied_data == expectd ,f"validation failed"

    
        