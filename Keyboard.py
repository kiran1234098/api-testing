import logging 
import time 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook

logging.basicConfig(level=logging.INFO,filename="sheet",filemode="w")
logger = logging.getLogger()

driver = webdriver.Chrome(path)
Workbook =Workbook()
sheet=Workbook.active
try:
    driver.get(web)

    # perform Keybord actions
    action = ActionChains(driver)
    action.send_keys("hellow")
    action.key_down("Shift").send_keys("s").key_up("Shift")
    action.perform()

    time.sleep(2)

    ele = driver.find_element(By.ID,"")
    soe = ele.text

sheet['a']=soe
Workbook.save("data.xlsx")

logger.info("data added to excel")

except Exception as e:
logger.exception("An",str(e))

finally:
driver.quit()