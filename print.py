from time import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
def test_pause(driver):
    driver.get()

    start = time()


    clickable = driver.find_element(By.ID,"clickable")
    ActionChains(driver)\
    .move_to_element(clickable)\
    .pause(1)\
    .click_and_hold()\
    .pause(1)\
    .send_keys("abc")\
    .perform()

    duration = time() - start
    assert duration > 2
    assert duration < 3

def test_release_all(driver):
    driver.get()
    clickable = driver.find_element(By.ID,"clickable")
    ActionChains(driver)\
    .click_and_hold(clickable)\
    .key_down(Keys.ShIFT)\    
    .key_down("a")\
    .perform()

    ActionBuilder(driver).clear_actions()

    ActionChains(driver).key_down