import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

if len(sys.argv) < 2:
    print("❌ Usage: python3 test_apache_page.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Headless mode for Jenkins
options = Options()
options.add_argument("--headless")

service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)

assert "Apache" in driver.title, "❌ Apache page title mismatch!"

print("✅ Apache page loaded successfully on Firefox (Jenkins headless)!")
driver.quit()
