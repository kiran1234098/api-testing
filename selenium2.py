from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload");
driver.implicitly_wait(30)
driver.find_element(By.ID, "file-upload").send_keys("C:\\Users\\kiran\\OneDrive\\Pictures\\Screenshotss\\s.png")


#driver.find_element(By.ID,"file-submit").submit()
'''if(driver.page_source.find("File Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()'''

  