from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(path)
driver.get(web)
driver.title
# get browser title 
broweser_title=driver.title
print(broweser_title)

# write implicity wait here
driver.implicitly_wait(9)

# find an element
ele = driver.find_element(By.CLASS_NAME,"")

# send and click
ele.send_keys("").click()

# request element info
ele.text

# end the browser
driver.quit()


# option default 
option = Options()
option.page_load_strategy= "norm"
option.page_load_strategy="eger"
option.page_load_strategy ="none"
driver = webdriver.Chrome(options=option)

# proxy setting
from selenium import webdriver

proxy ="<host:port>"
webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":proxy,
    "ftpproxu":proxy,
    "sslProxy":proxy,
    "proxyType":"MANUAL",
}

with webdriver.Firefox() as driver:
    driver.get("htt")

# explicit wait
WebDriverWait(driver,10).until(document_initialzed)


# wait for some element
ele = WebDriverWait(driver,3).until(EC.presence_of_element_located(By.CLASS_NAME,"p"))
assert ele == "some"


# find upload
driver.find_element(By.ID,"").send_keys(.jpg)
if driver.page_source.find("File uplod"):
    print("successfull")
else:
    print("not")    

# element is visible
is_email = driver.find_element(By.ID,"").is_displayed()

is_email = driver.find_element(By.CLASS_NAME,"").is_enabled()

is_email = driver.find_element(By.CLASS_NAME,"").is_selected()


# brouser info

driver.getTile()

driver.getCurrentUrl    

driver.get("")

# browser pressing back button
driver.back()

# browser pressing forword button
driver.forward()

# refresh the current page
driver.refresh()

# alert massage handle
alert=WebDriverWait(driver,10).until(EC.alert_is_present())
aleart_text= alert.text
alert.accept()

# alert massage cancel
alert=WebDriverWait(driver,10).until(EC.alert_is_present())
alert.dismiss()

# alert prompt 
alert = WebDriverWait(driver,10).until(EC.alert_is_present())
driver.switch_to.alert

alert.send_keys("input")
alert.accept()

# promt 
alert= WebDriverWait(driver,10).until(EC.alert_is_present())
driver.switch_to.alert
alert.send_keys("k")
alert.accept()

# add cookie
driver.add_cookie("name":"key","value":"value")
driver.get_cookie("key")
driver.get_cookies()


# delete cookie
driver.delete_cookie('value')
driver.delete_all_cookies('value')

# iframes
#store iframe web element

iframe =driver.find_element(By.CSS_SELECTOR,"#modal>iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.TAG_NAME,"").click()

# by id
driver.switch_to.frame('buttonframe')
driver.find_element(By.TAG_NAME,"button").click()

# using index
iframe = driver.find_element(By.TAG_NAME,'iframe')[1]
driver.switch_to.frame(iframe)

# leaving frame
driver.switch_to.default_content()

# window handle
driver.current_window_handle


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select

with webdriver.Firefox() as driver:
    # open url
    driver.get("h")

    # setup wait for later
    wait = WebDriverWait(driver,10)

    # store the id of the original window
    original_window =driver.current_window_handle

    # check we don't have other windows open already
    assert len(driver.window_handles)==1

    driver.find_element(By.LINK_TEXT,"new window").click()

    driver.find_element(By.LINK_TEXT,"new window").click()

    wait.until(EC.number_of_windows_to_be(2))

    # loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle!= original_window:
            driver.switch_to.window(window_handle)
            break:

    wait.until(EC.title_is("selen"))        



    # open a new tab and switches to new tab
    driver.switch_to.new_window('tab')
    driver.switch_to.new_window('window')
    driver.close()
    #switchback to the old tab
    driver.switch_to.window(original_window)

    # screenshot
    driver.save_screenshot('.')

    # action
    ActionChains(driver)\
        .move_to_element(clickable)\
        .click_and_hold()\
        .pause(1)\
        .double_click(clickable)\
        .pause(2)\
        .perform()
    