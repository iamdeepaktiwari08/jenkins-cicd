from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import sys

url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8085"

# Firefox options (Headless mode)
options = Options()
options.add_argument("--headless")   # 👈 server/jenkins me GUI ke bina chalega

service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
print("Page Title:", driver.title)

assert "Jai Shri Ram Jai Hanuman" in driver.title, "❌ Title mismatch!"

print("✅ Test Passed: Correct title found!")

driver.quit()
