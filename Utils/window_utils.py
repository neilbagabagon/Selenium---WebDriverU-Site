import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class WindowUtils:
    @staticmethod
    def get_main_window(driver):
        return driver.current_window_handle

    @staticmethod
    def switch_to_new_window(driver, timeout=5):
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])
        return driver.current_window_handle

    @staticmethod
    def switch_back(driver, main_window):
        return driver.switch_to.window(main_window)

    @staticmethod
    def click_and_verify(driver, element_id, link_url, expected_domain="webdriveruniversity.com", ):
        try:
            if element_id:
                button = driver.find_element(By.ID, element_id)
            else:
                raise NoSuchElementException
        except NoSuchElementException:
            if link_url:
                button = driver.find_element(By.XPATH, link_url)
            else:
                raise NoSuchElementException

        main_window = driver.current_window_handle
        expected_url = button.get_attribute("href")
        time.sleep(2)

        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        driver.execute_script("arguments[0].click();", button)

        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        opened_url = driver.current_url
        assert expected_domain in opened_url, f"Expected domain '{expected_domain}' not found in {opened_url}"
        time.sleep(2)
        driver.close()
        driver.switch_to.window(main_window)

        print(f"\nEXPECTED URL: {expected_url}")
        print(f"ACTUAL URL: {opened_url}")
        print(bool(expected_url == opened_url))

###### SAMPLE code if not a @staticmethod #####

# login_button = self.driver.find_element(By.ID, "login-portal")
# main_window = WindowUtils.get_main_window(self.driver)
# expected_url = login_button.get_attribute("href")
# time.sleep(2)
#
# self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
# self.driver.execute_script("arguments[0].click();", login_button)
#
# WindowUtils.switch_to_new_window(self.driver)
# opened_url = self.driver.current_url
# assert "webdriveruniversity.com" in f"Expected url: {expected_url}, Actual url: {opened_url}"
#
# self.driver.close()
# WindowUtils.switch_back(self.driver, main_window)
#
# print("\nEXPECTED URL:", expected_url)
# print("ACTUAL URL:", opened_url)
# print(bool(expected_url == opened_url))
