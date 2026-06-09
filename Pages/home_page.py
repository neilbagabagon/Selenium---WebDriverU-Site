import time
from selenium.webdriver.common.by import By
from window_utils import WindowUtils


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")
        assert "WebDriverUniversity.com" in self.driver.title

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        scroll_position = self.driver.execute_script("return window.pageYOffset;")
        time.sleep(2)
        assert scroll_position > 0
        time.sleep(2)
        print("Scroll Position:", scroll_position)
        print(bool(scroll_position))

    def click_logo(self):
        logo_button = self.driver.find_element(By.ID, "nav-title")
        logo_button.click()
        assert "WebDriverUniversity.com" in self.driver.title

    def click_course(self):
        course_buttons = self.driver.find_elements(By.CLASS_NAME, "course-btn")
        main_window = WindowUtils.get_main_window(self.driver)

        for each_course_btn in course_buttons:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", each_course_btn)
            self.driver.execute_script("arguments[0].click();", each_course_btn)
            time.sleep(2)
            expected_url = each_course_btn.get_attribute("href")

            WindowUtils.switch_to_new_window(self.driver)
            opened_url = self.driver.current_url
            assert "udemy.com" in opened_url, f"Expected url: {expected_url}, Actual url: {opened_url}"
            time.sleep(2)
            self.driver.close()
            WindowUtils.switch_back(self.driver, main_window)

            print("\nEXPECTED URL:", expected_url)
            print("ACTUAL URL:", opened_url)
            print(bool(expected_url == opened_url))

    def click_contact_us(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='contact-us']")

    def click_login(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='login-portal']")

    def click_button_click(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='button-clicks']")

    def click_to_do(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='to-do-list']")

    def click_object_model(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='page-object-model']")

    def click_card_link(self):
        WindowUtils.click_and_verify(self.driver, "//a[@href='Accordion/index.html']")

    def click_drop_check_radio(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='dropdown-checkboxes-radiobuttons']")

    def click_ajax_loader(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='ajax-loader']")

    def click_actions(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='actions']")

    def click_scroll_around(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='scrolling-around']")

    def click_popup_alerts(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='popup-alerts']")

    def click_iframe(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='iframe']")

    def click_hidden_elements(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='hidden-elements']")

    def click_data_table(self):
        WindowUtils.click_and_verify(self.driver, "(//a[@id='data-table'])[1]")

    def click_autocomplete_textfield(self):
        WindowUtils.click_and_verify(self.driver, "(//a[@id='data-table'])[2]")

    def click_file_upload(self):
        WindowUtils.click_and_verify(self.driver, "(//a[@id='data-table'])[3]")

    def click_date_picker(self):
        WindowUtils.click_and_verify(self.driver, "(//a[@id='data-table'])[4]")

    def click_ai_playground(self):
        WindowUtils.click_and_verify(self.driver, "//a[@id='ai-playground']")
