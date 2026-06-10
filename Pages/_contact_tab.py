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
        def inputs_all_true():
            self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Neil")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Bagabagon")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("njb@gmail.com")
            self.driver.find_element(By.XPATH, "//textarea[@placeholder='Comments']").send_keys("lorem ipsum")

        def inputs_all_false():
            self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("njb")

        def inputs_email_true_name_false():
            self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("njb@gmail.com")
            self.driver.find_element(By.XPATH, "//textarea[@placeholder='Comments']").send_keys("lorem ipsum")

        def inputs_email_false_name_true():
            self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Neil")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Bagabagon")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("njb@")
            self.driver.find_element(By.XPATH, "//textarea[@placeholder='Comments']").send_keys("lorem ipsum")

        button = self.driver.find_element(By.XPATH, "//a[@id='contact-us']")
        main_window = self.driver.current_window_handle
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_wait(self.driver)

        # TEST RESET BUTTON
        inputs_all_true()
        self.driver.find_element(By.XPATH, "//input[@value='RESET']").click()
        time.sleep(1)

        # TEST SUBMIT WHEN ALL FALSE
        inputs_all_false()
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)
        all_false = self.driver.find_element(By.XPATH, "//body")
        print("\nAll False: \n", all_false.text)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Try Again')]").click()
        time.sleep(1)


        # TEST SUBMIT WHEN EMAIL TRUE AND NAME FALSE
        inputs_email_true_name_false()
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)
        name_false = self.driver.find_element(By.XPATH, "//body")
        print("\nEmail True & Name False: \n", name_false.text)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Try Again')]").click()
        time.sleep(1)

        # TEST SUBMIT WHEN EMAIL FALSE AND NAME TRUE
        inputs_email_false_name_true()
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)
        email_false = self.driver.find_element(By.XPATH, "//body")
        print("\nEmail False & Name True: \n", email_false.text)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'← Try Again')]").click()
        time.sleep(1)

        # TEST SUBMIT WHEN ALL TRUE
        inputs_all_true()
        self.driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()
        time.sleep(1)
        all_true = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Thank You for your Message!']")
        print("\nAll True: \n", all_true.text)
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
