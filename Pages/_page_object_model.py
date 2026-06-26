import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v146.page import navigate

from window_utils import WindowUtils


class PageObjectModel:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    def window_handler(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='page-object-model']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

    def controls_and_navigation(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        for each_right_control in range(3):
            right_control = self.driver.find_element(By.XPATH, "//a[@class='right carousel-control']")
            action_right_click = ActionChains(self.driver)
            action_right_click.move_to_element(right_control).click().perform()
            time.sleep(1)

        for each_left_control in range(3):
            left_control = self.driver.find_element(By.XPATH, "//a[@class='left carousel-control']")
            action_left_click = ActionChains(self.driver)
            action_left_click.move_to_element(left_control).click().perform()
            time.sleep(1)

        radio_buttons = self.driver.find_elements(By.XPATH, "//ol[@class='carousel-indicators']/li")
        for each_radio_button in radio_buttons:
            each_radio_button.click()
            time.sleep(1)

        xpath = ["//button[normalize-space()='Find Out More']",
                  "//button[normalize-space()='Close']",
                  "//button[normalize-space()='×']",
                  "//div[@id='myModal']"]
        for each_xpath in xpath:
            action_click = ActionChains(self.driver)

            find_out_button = self.driver.find_element(By.XPATH, "//b[normalize-space()='Find Out More!']")
            action_click.move_to_element(find_out_button).click().perform()
            time.sleep(1)

            exit_button = self.driver.find_element(By.XPATH, each_xpath)
            action_click.move_to_element(exit_button).click().perform()
            time.sleep(1)

        button_navigation = ["//a[normalize-space()='Our Products']",
                             "//a[normalize-space()='Contact Us']"]
        for each_button_navigation in button_navigation:
            self.driver.find_element(By.XPATH, each_button_navigation).click()
            time.sleep(1)
            self.driver.back()
            time.sleep(1)

        self.driver.close()
        self.driver.switch_to.window(main_window)

    def nav_our_products(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        # NAVIGATE TO [OUR PRODUCTS]
        action_click = ActionChains(self.driver)

        navigate_our_products = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Products']")
        action_click.move_to_element(navigate_our_products).click().perform()

        product_list = ["//div[@id='special-offers']//p",
                        "//div[@id='cameras']//p",
                        "//div[@id='new-laptops']//p",
                        "//div[@id='used-laptops']//p",
                        "//div[@id='game-consoles']//p",
                        "//div[@id='components']//p",
                        "//div[@id='desktop-systems']//p",
                        "//div[@id='audio']//p"]

        for each_product in product_list:
            self.driver.find_element(By.XPATH, each_product).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()
        for each_product in product_list:
            self.driver.find_element(By.XPATH, each_product).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Close']").click()
        for each_product in product_list:
            self.driver.find_element(By.XPATH, each_product).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='×']").click()
        for each_product in product_list:
            click_print = self.driver.find_element(By.XPATH, each_product)
            click_print.click()
            print("\nClicked: ", click_print.text)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//div[@id='myModal']").click()
            time.sleep(1)

        button_navigation = ["//a[normalize-space()='Home']",
                             "//a[normalize-space()='Contact Us']"]
        for each_button_navigation in button_navigation:
            self.driver.find_element(By.XPATH, each_button_navigation).click()
            time.sleep(1)
            self.driver.back()
            time.sleep(1)

        self.driver.close()
        self.driver.switch_to.window(main_window)

    def nav_contact_us(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        self.driver.find_element(By.XPATH, "//a[normalize-space()='Contact Us']").click()

        self.driver.close()
        self.driver.switch_to.window(main_window)
