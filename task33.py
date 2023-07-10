from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time 

web =
path=
driver = webdriver(web)
driver.get()

textbox = driver.find_element(By.CLASS_NAME,"").is_displayed()
assert textbox == True

inpu_box = driver.find_element(By.E)
