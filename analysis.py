from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.maximize_window()

# Navigate to the URL
url = "https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/"
driver.get(url)

# Wait for the page to load (You can adjust the waiting time if needed)
driver.implicitly_wait(10)

# Extract the article text
article_title = driver.find_element(By.CLASS_NAME, "entry-title").text
article_content = driver.find_element(By.XPATH, '//div[@class="td-post-content tagdiv-type"]').text

# Print the extracted data
print("Article Title:", article_title)
print("Article Content:", article_content)

# Close the browser
driver.quit()
