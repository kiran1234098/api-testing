from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options =Options()
options.page_load_strategy='normal'
driver = webdriver.Chrome(options=options)
driver=webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()

options.page_load_strategy='eager'
options.page_load_strategy='none'


driver.navigate('file:///race_condition.html')
el = driver.find_element(By.TAG_NAME,'p')
assert el.text == "Hello from Javasript"

from selenium.webdriver.support.wait import WebDriverWait

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver.navigate("file:")
WebDriverWait(driver,timeout=10).until(document_initialised)
el = driver.find_element(by.TAG_NAME,"p")
assert el.text == "Hello from JavaScript!"

