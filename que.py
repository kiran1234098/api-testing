from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a WebDriver instance
driver = webdriver.Chrome('chromedriver')

# Open the Magento Software Testing Board website
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='button-group']//span[@class='hidden-xs hidden-sm hidden-md']").click()

driver.find_element(By.CLASS_NAME, "btn.btn-inverse.btn-block.btn-lg.dropdown-toggle").click()

# Wait for the table to be visible
table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table.table-striped")))

# Print the text of each element in the table
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    print(row.text)

# Quit the WebDriver
driver.quit()
