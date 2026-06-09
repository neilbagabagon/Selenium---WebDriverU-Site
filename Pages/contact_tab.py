import time
from selenium.webdriver.common.by import By
from window_utils import WindowUtils


class ContactTab:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    def input_details(self):
        def fill_inputs(driver):
            self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Neil")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Bagabagon")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys(
                "bagabagon111000@gmail.com")
            self.driver.find_element(By.XPATH, "//textarea[@placeholder='Comments']").send_keys(
                "lorem ipsum dolor sit amet")

        button = self.driver.find_element(By.XPATH, "//a[@id='contact-us']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_wait(self.driver)

        fill_inputs(self.driver)
        self.driver.find_element(By.XPATH, "//input[@value='RESET']").click()
        time.sleep(1)

        fill_inputs(self.driver)
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Back to Homepage')]").click()
        time.sleep(1)
        self.driver.switch_to.window(main_window)

    def input_empty(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='contact-us']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_wait(self.driver)

        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Try Again')]").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()
        time.sleep(1)

        self.driver.switch_to.window(main_window)
