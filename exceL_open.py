from selenium import webdriver
from openpyxl import load_workbook

driver = webdriver.Chrome()

excel_file_path = "path_.xlsx"
workbook = load_workbook(excel_file.path)

sheet= workbook['sheet1']

cell_value = sheet['A1'].value

print(cell_value)

