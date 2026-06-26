import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from window_utils import WindowUtils
from selenium.webdriver.support import expected_conditions as EC

class LoginTab:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    def window_handler(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='login-portal']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

    def login_portal(self):
        def input_succeed():
            self.driver.find_element(By.XPATH, "//input[@id='text']").send_keys("webdriver")
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("webdriver123")

        def input_failed():
            self.driver.find_element(By.XPATH, "//input[@id='text']").send_keys("izkitzo")
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("izkitzo123")

        self.window_handler()

        input_failed()
        self.driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        assert alert.text == "validation failed"
        print("\n", alert.text)
        time.sleep(1)
        alert.accept()
        time.sleep(1)

        input_succeed()
        self.driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        assert alert.text == "validation succeeded"
        print("\n", alert.text)
        time.sleep(1)
        alert.accept()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[@id='home-link']").click()
        time.sleep(1)