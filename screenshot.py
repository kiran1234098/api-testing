from selenium import webdriver
import os

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")
# Return and base64 encoded string into image

driver.save_screenshot(r'C:\Users\kiran\OneDrive\Desktop\app\import.png')

#take element screeen shot
ele =driver.find_element(By.CSS_SELECLTOR,'h1')

ele.screenshot('./image.png')

# Execute Script
header = driver.find_element(By.CSS_SELECTOR,'h1')
driver.execute_script('return argument [0].innerText',header)



from selenium.webdriver.common.print_page_options import PrintOptions
print_oti

driver.quit()
