from selenium import webdriver
import pyautogui
import time
import os
from selenium.webdriver.common.by import By

path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
upload_input = driver.find_element(By.ID,"file-upload")
upload_input.click()

time.sleep(5)

file_path = r"C:\Users\kiran\OneDrive\Pictures\Screenshots\s.png"
time.sleep(10)
pyautogui.typewrite(file_path)
pyautogui.press('enter')

