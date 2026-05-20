import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_homepage(driver):
    driver.set_page_load_timeout(30)  # wait up to 30s for page load
    driver.get("https://webdriveruniversity.com/")
    time.sleep(5)  # then pause 5s

    assert "WebDriverUniversity.com" in driver.title
