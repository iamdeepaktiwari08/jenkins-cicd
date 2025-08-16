import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# -------------------------------
# Configuration
# -------------------------------
URL = "http://192.168.77.133:8085"   # Apache container URL
EXPECTED_TEXT = "Hello from Apache Docker"  # must match index.html text

# -------------------------------
# Wait until Apache is reachable
# -------------------------------
for i in range(10):
    try:
        r = requests.get(URL, timeout=2)
        if r.status_code == 200:
            print(f"Apache is up at {URL}")
            break
    except Exception:
        print("Waiting for Apache to start...")
    time.sleep(2)
else:
    raise Exception(f"Apache not reachable at {URL}")

# -------------------------------
# Selenium Setup (Headless)
# -------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")         # run without GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")        # path to chromedriver (adjust if needed)
driver = webdriver.Chrome(service=service, options=chrome_options)

# -------------------------------
# Open the page and check content
# -------------------------------
driver.get(URL)
time.sleep(2)  # allow page to load fully

page_source = driver.page_source
print("Page content loaded")

assert EXPECTED_TEXT in page_source, f"Expected text not found in page. Got:\n{page_source}"

print("✅ Selenium Test Passed!")
driver.quit()
