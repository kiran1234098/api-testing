from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

driver = webdriver.Chrome(web)
driver.get(web)

driver.find_element(By.CLASS_NAME,"j").send_keys("")
driver.find_element(By.ID,"").send_keys("")

# select an option from a dropdown
dropdown = select(driver.find_element(By.ID,""))
dropdown.select_by_visible_text("")

#select radio button
driver.find_element(By.CLASS_NAME,"").click()

# Print the form details

form_details = {
    "name": driver.find_element(By.ID,"").get_attribute("value"),
    "email":driver.find_element(By.ID,"email").get_attribute("value")
    "Country":dropdown.first_select_option.text}

for field ,value in form_details.items():
    print(f"")
driver.quit()
