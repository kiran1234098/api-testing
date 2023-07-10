from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

with webdriver.Firefox() as driver:
    # open url
    driver.get("")
    #
    wait =WebDriverWait(driver,10)

    origanal_window = driver.current_window_handle

    assert len(driver.window_handles) ==1

    driver.find_element(By.LINK_TEXT,"new window ").clink()

    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != origanal_window:
            driver.switch_to.window(window_handle)
            break


    wait.until(EC.title_is("seleniumHQ browser Automation"))

    # create new winndow (or) new tab and swich
    driver.switch_to.new_window('tab')

    driver.switch_to.new_window('window') 


    # close the tab or window
    driver.close()

    driver.switch_to.window(origanal_window)

    driver.maximize_window()
    driver.minimize_window()
    driver.fullscreen_window()
        
    

