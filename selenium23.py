from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_componests():
    driver = webdriver.Chrome()
    
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title =driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=by.Name,value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR,value="botton")

    text_box.send_keys("selenium")
    submit_button.click()

    massage =driver.find_element(by=By.ID,value="massage")
    value =massage.text

    assert value =="Received!"

    driver.quit()