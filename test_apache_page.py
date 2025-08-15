from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Firefox browser (GeckoDriver must be installed)
driver = webdriver.Firefox()

# Go to your Apache server page
driver.get("http://localhost:84")  # Change port if different

# Check if the page title contains expected text
assert "Apache" in driver.title, "Apache page title mismatch!"

print("✅ Apache page loaded successfully!")

driver.quit()
