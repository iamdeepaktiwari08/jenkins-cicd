from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import sys

# Get URL from command-line arg
url = sys.argv[1]

# Firefox driver path
service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service)

# Open Apache page
driver.get(url)

# Debug info
print("🔹 Page title is:", driver.title)

# Assertion according to your actual title
assert "Jai Shri Ram Jai Hanuman" in driver.title, \
       f"❌ Page title mismatch! Found: {driver.title}"

print("✅ Selenium test passed! Apache page title verified.")

driver.quit()
