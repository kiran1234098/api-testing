from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from time import time
import time
import sys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By


def test_pauses(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    start = time()

    clickable = driver.find_element(By.ID, "clickable")
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


def test_releases_all(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .key_down(Keys.SHIFT)\
        .key_down("a")\
        .perform()

    ActionBuilder(driver).clear_actions()

    ActionChains(driver).key_down('a').perform()

    assert clickable.get_attribute('value')[0] == "A"
    assert clickable.get_attribute('value')[1] == "a"
    time.sleep(10)

def test_copy_and_paste(driver):
    #driver = firefox_driver
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')
    cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    #time.sleep(10)
    ActionChains(driver)\
        .send_keys("Selenium!")\
        .send_keys(Keys.ARROW_LEFT)\
        .key_down(Keys.SHIFT)\
        .send_keys(Keys.ARROW_UP)\
        .key_up(Keys.SHIFT)\
        .key_down(cmd_ctrl)\
        .send_keys("xvv")\
        .key_up(cmd_ctrl)\
        .perform()
    time.sleep(10)
    actual_value = driver.find_element(By.ID, "textInput").get_attribute('value')
    print("Actual Value:", actual_value)
    assert actual_value == "SeleniumSelenium!"


def test_click_and_hold(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .perform()

    time.sleep(10)
    assert driver.find_element(By.ID, "click-status").text == "focused"

def test_right_click(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .context_click(clickable)\
        .perform()

    time.sleep(10)
    assert driver.find_element(By.ID, "click-status").text == "context-clicked"   

def test_back_click_ab(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')
    driver.find_element(By.ID, "click").click()
    assert driver.title == "We Arrive Here"
    time.sleep(10)
    action = ActionBuilder(driver)
    action.pointer_action.pointer_down(MouseButton.BACK)
    time.sleep(5)
    action.pointer_action.pointer_up(MouseButton.BACK)
    time.sleep(5)
    action.perform()

    assert driver.title == "BasicMouseInterfaceTest"

def test_drag_and_drop_by_offset(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')
    time.sleep(5)

    draggable = driver.find_element(By.ID, "draggable")
    start = draggable.location
    finish = driver.find_element(By.ID, "droppable").location
    time.sleep(5)
    ActionChains(driver)\
        .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y'])\
        .perform()
    time.sleep(10)
    assert driver.find_element(By.ID, "drop-status").text == "dropped"

def test_drag_and_drop_onto_element(driver):
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')
    time.sleep(5)
    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    time.sleep(5)
    ActionChains(driver)\
        .drag_and_drop(draggable, droppable)\
        .perform()
    time.sleep(5)
    assert driver.find_element(By.ID, "drop-status").text == "dropped"

path = 'chromedriver'
driver = webdriver.Chrome(path)
#test_copy_and_paste(driver)
#test_click_and_hold(driver)
#test_pauses(driver)
#test_releases_all(driver)
#test_right_click(driver)
#test_back_click_ab(driver)
#test_drag_and_drop_by_offset(driver)
test_drag_and_drop_onto_element(driver)