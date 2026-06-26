import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from window_utils import WindowUtils


class AccordionTextEffect:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    def window_handler(self):
        button = self.driver.find_element(By.XPATH, "//a[@href='Accordion/index.html']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

    def toggle_panels(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        # IMPLICIT WAIT
        manual_testing = self.driver.find_element(By.XPATH, "//button[@id='manual-testing-accordion']")
        self.driver.implicitly_wait(2)
        manual_testing.click()
        manual_testing.click()

        # EXPLICIT WAIT
        cucumber_bdd = WebDriverWait(self.driver, 2).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@id='cucumber-accordion']")))
        cucumber_bdd.click()
        cucumber_bdd.click()

        # FLUENT WAIT
        automation_test = WebDriverWait(self.driver, 5, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
        test_button = automation_test.until(lambda d: d.find_element(By.XPATH, "//button[@id='automation-accordion']"))
        test_button.click()
        test_button.click()

        # HARD CODED WAIT/DELAY
        keep_click = self.driver.find_element(By.XPATH, "//button[@id='click-accordion']")
        time.sleep(10)
        keep_click.click()
        time.sleep(1)
        keep_click.click()

        # accordion_list = ["//button[@id='manual-testing-accordion']",
        #                   "//button[@id='cucumber-accordion']",
        #                   "//button[@id='automation-accordion']",
        #                   "//button[@id='click-accordion']"]
        # for each_accordion in accordion_list:
        #     element = self.driver.find_element(By.XPATH, each_accordion)
        #     for _ in range(2):
        #         if each_accordion != "//button[@id='click-accordion']":
        #             time.sleep(1)
        #             element.click()
        #         else:
        #             time.sleep(5)
        #             element.click()

        time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(main_window)
