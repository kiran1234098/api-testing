from selenium import webdriver
driver.implicity_wait(10)
driver.get("https://the-internet.herokuapp.com/upload")

driver.find_element(By.ID,"file-upload").send_keys("selenium-snapshot.jpg")

driver.find_element(By.ID,"file-submit").submit()
if(driver.page_source.find("file Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyau
driver =webdriver.Chrome()

driver.get()