import sys
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

if len(sys.argv) < 2:
    print("❌ Usage: python3 test_selenium.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# 🔹 Path to geckodriver (absolute path)
# Windows: r"C:\Users\deepak\Downloads\geckodriver.exe"
# Linux: "/usr/local/bin/geckodriver"
GECKO_PATH = os.path.abspath("geckodriver")

service = FirefoxService(executable_path=GECKO_PATH)
driver = webdriver.Firefox(service=service)

driver.get(url)

assert "Apache" in driver.title, "❌ Apache page title mismatch!"

print("✅ Apache page loaded successfully on Firefox!")
driver.quit()
