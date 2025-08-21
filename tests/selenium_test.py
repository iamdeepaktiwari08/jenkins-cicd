from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("http://localhost:8081")

assert "Hello from Jenkins CI/CD 🚀" in driver.page_source

print("✅ Selenium test passed!")

driver.quit()
