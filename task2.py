from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web="https://tutorialsninja.com/demo/"
path='chromedriver'
driver =webdriver.Chrome(path)
driver.get(web)

item = driver.find_element(By.LINK_TEXT,"MacBook")
item.click()

isbody = driver.find_element(By.TAG_NAME,"body")
assert isbody == True

product_name =driver.find_element(By.XPATH,"//div[@class='col-sm-4']/h1/text()")
get_product_name = product_name.text
product_price  =driver.find_element(By.XPATH,"//ul[@class='list-unstyled']/li/h2")
get_product_price = driver.product_price.text

#product_detail =driver.find_element(By.ID,"")
#get_product_detail = product_detail.text

driver.find_element(By.ID,"button-cart").click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

#alert_text =alert.text
#assert alert_text == "Seccess: You have added MacBook to your shopping cart!"
time.sleep(10)
driver.back()

driver.find_element(By.CLASS_NAME,"btn btn-inverse btn-block btn-lg dropdown-toggle").click()

#total_cost = driver.find_element(By.ID,"")
#assert total_cost == product_cost  *2

