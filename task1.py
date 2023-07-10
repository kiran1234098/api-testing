from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


web ="https://stackoverflow.com/"
path=
driver = webdriver.Chrome(path)
driver.get(web)

wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located(By.TAG_NAME,"body"))

log_button =driver.find_element(By.ID,"").click()
time.sleep(4)
inpu_ele =driver.find_element(By.ID,"")
inpu_ele.send_keys("kiranzapate@gmail.com")
assert inpu_ele.text == "Email"

inpu_pass = driver.find_element(By.CLASS_NAME,"")
inpu_pass.send_keys("kiran098")

time.sleep(4)

boolean isAsk = driver.find_element(By.Name,"Asl")
assert isAsk == True

ask_botton = driver.find_element(By.ID,"")
ask_botton.click()

time.sleep(5)

title_page = driver.find_element(By.ID,"")
title_page.send_keys("")

driver.find_element(By.ID,"").click()

discrip=driver.find_element(By.ID,"")
discrip.send_keys("")

driver.find_element(By.CLASS_NAME,"").click()

que1=driver.find_element(By.CLASS_NAME,"")
que1.send_keys()

driver.find_element(By.CLASS_NAME,"").click()

Tag=driver.find_element(By.CLASS_NAME,'')
Tag.send_keys("")

driver.find_element(By.CLASS_NAME,"").click()

driver.find_element(By.CLASS_NAME,"").click()

