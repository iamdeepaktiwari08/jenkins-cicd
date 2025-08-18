
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import sys, time

url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8085"

options = Options()
options.add_argument("--headless")  # run without GUI (important for Jenkins)

service = Service("/usr/local/bin/geckodriver")  # path to geckodriver
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get(url)
    time.sleep(2)  # wait for page load

    page_title = driver.title
    print(f"✅ Page Title: {page_title}")

    if "Apache" in page_title or "Index" in page_title:
        print("✅ Apache page is loading correctly")
        sys.exit(0)  # success
    else:
        print("❌ Apache page title not correct")
        sys.exit(1)  # fail

finally:
    driver.quit()
