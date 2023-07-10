from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
optopn = Options()
optopn.page_load_strategy = 'norm'|| 'eger' or None
driver = webdriver.Chrome(options=optopn)
