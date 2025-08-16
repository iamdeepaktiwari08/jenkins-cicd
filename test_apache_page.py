from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

# Replace with your container’s IP:PORT
driver.get("http://192.168.77.133:8085")

assert "Apache" in driver.page_source, "❌ Apache page content mismatch!"
print("✅ Apache page loaded successfully!")

driver.quit()
