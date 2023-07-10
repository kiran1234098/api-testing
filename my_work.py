from selenium import webdriver
import mysql.connector
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
web =""
path ="chromedriver"

# Create a WebDriver instance
driver = webdriver.Chrome()

# Open website
driver.get("")

# Wait for the product listing page to load
#WebDriverWait(driver, 10).until(EC.title_contains("Home page"))
