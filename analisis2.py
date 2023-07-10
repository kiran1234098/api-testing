from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.maximize_window()

# Navigate to the URL
url = "https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/"
driver.get(url)

# Wait for the page to load (You can adjust the waiting time if needed)
driver.implicitly_wait(10)

# Extract the article text
article_title = driver.find_element(By.CLASS_NAME, "entry-title").text
article_content_element = driver.find_element(By.XPATH, '//div[@class="td-post-content tagdiv-type"]')
article_content_lines = article_content_element.text.split('\n')

# Remove the last line from the content
article_content_lines = article_content_lines[:-1]
# Remove any image tags from the content
article_content_lines = [line for line in article_content_lines if not line.startswith('[Image:')]

# Join the remaining lines back into a single string
article_content = '\n'.join(article_content_lines)



# Print the extracted data
print("Article Title:", article_title)
print("Article Content:", article_content)

# Close the browser
driver.quit()
