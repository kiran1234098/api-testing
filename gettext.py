import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from docx import document

from selenium.webdriver.common.action_chains import ActionChains

logging.basicConfig(level=logging.INFO,filename="acrion.txt",filemode="w")
logger =logging.getLogger()

driver = webdriver.chrome(web)
doc =document()

try:
    driver.get("htts:")
    clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID,""))
    driver.save_screenshot("screenshot_befor.png")
    doc.add_picturee("Screenshot.png")
    doc.add_paragraph("")

    logger.info("varifiy")
    find