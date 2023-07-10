from selenium import webdriver

def run_test_cases(driver,browser_name):
    #open the browser
    driver.get("")

    #perform actions and assertions
    # for example:
    # driver.find_element(By.ID,"").send_keys("")
    # driver.find_element(By.ID,"").send_keys("")
    # driver.find_element(By.ID,"").click()
    # asssert "Expected result "==driver.find_element(By.ID,"").text
    print("borowser",browser_name)
# Set the paths to the wbdriver executable for chrome and firefox
# 
chrome_driver_path = "path/to/chromedriver"
firefox_driver_path = "path/to/geckodriver" 

# create ChromeDriver instanse
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)
run_test_cases(chrome_driver,"chrome")

# Create firefoxDriver instance
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path)
run_test_cases(firefox_driver,"Firefox")

chrome_driver.quit()
firefox_driver.quit()