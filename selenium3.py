from selenium import wbdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

website = 'https://www.linkedin.com/'
path = 'chromedriver'

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get(website)

wbsite= "https:"
path ='chromedriver'

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get(website)

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("your_userName")
password.send_keys("your_password")
possword.send_keys(Keys.ENTER) # Presss Enter to submit the form

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)";)

download_button = driver.find_element_by_xpath("//a[@class ='download']")
download_button.click(
     
)

import time
import os 
file_path ="/path/to/downloaded/file" 

if os.path.exists(file_path):
    os.startfile(file_path)
    
