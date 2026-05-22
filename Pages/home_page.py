import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get(self.url)
        assert "WebDriverUniversity.com" in self.driver.title

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        scroll_position = self.driver.execute_script("return window.pageYOffset;")
        assert scroll_position > 0

    def click_logo(self):
        logo_button = self.driver.find_element(By.ID, "nav-title")
        logo_button.click()
        assert "WebDriverUniversity.com" in self.driver.title

    def click_courses(self):
        course_buttons = self.driver.find_elements(By.CLASS_NAME, "course-btn")
        main_window = self.driver.current_window_handle

        for course_button in course_buttons:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "course-btn")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", course_button)
            self.driver.execute_script("arguments[0].click();", course_button)

            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            opened_url = self.driver.current_url
            assert "udemy.com" in opened_url

            self.driver.close()
            self.driver.switch_to.window(main_window)

