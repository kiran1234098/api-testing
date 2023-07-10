from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a WebDriver instance
driver = webdriver.Chrome()

# Open the Magento Software Testing Board website
driver.get("https://magento.softwaretestingboard.com/")

# Wait for the product listing page to load
WebDriverWait(driver, 10).until(EC.title_contains("Home page"))

# Navigate to the product listing page
driver.find_element(By.LINK_TEXT, "Sale").click()

# Select a specific product to view its details
driver.find_element(By.LINK_TEXT, "Product Name").click()

# Validate that the product details page is displayed correctly
WebDriverWait(driver, 10).until(EC.title_contains("Product Details"))

# Note down the product's name, price, and other relevant information
product_name = driver.find_element(By.CSS_SELECTOR, "h1.product-name").text
product_price = driver.find_element(By.CSS_SELECTOR, "span.price").text

# Click the "Add to Cart" button
driver.find_element(By.CSS_SELECTOR, "button.tocart").click()

# Verify that the product is successfully added to the cart
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.minicart-wrapper span.counter-number"), "1"))

# Navigate to the cart page
driver.find_element(By.CSS_SELECTOR, "a.action.showcart").click()

# Validate that the product appears in the cart with the correct details
cart_product_name = driver.find_element(By.CSS_SELECTOR, "a.product-item-link").text
cart_product_price = driver.find_element(By.CSS_SELECTOR, "span.price").text

assert product_name == cart_product_name
assert product_price == cart_product_price

# Verify the total price and quantity of items in the cart
cart_total_price = driver.find_element(By.CSS_SELECTOR, "span.price-including-tax").text
cart_quantity = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty").get_attribute("value")

# Print the results
print("Product Name:", product_name)
print("Product Price:", product_price)
print("Cart Product Name:", cart_product_name)
print("Cart Product Price:", cart_product_price)
print("Cart Total Price:", cart_total_price)
print("Cart Quantity:", cart_quantity)

# Optionally, proceed to the checkout process and validate the order placement steps

# Close the browser
driver.quit()
