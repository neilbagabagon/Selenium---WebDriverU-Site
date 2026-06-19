import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from window_utils import WindowUtils

class ToDoListTab:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    # ADD TO LIST
    def add_to_list(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='to-do-list']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

        todo_list = {"Go to work",
                     "Eat lunch",
                     "Go home"}
        for each_todo in todo_list:
            self.driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys(each_todo + Keys.ENTER)
            time.sleep(1)

        self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        time.sleep(1)

    # STRIKETHROUGH AND REMOVE
    def strike_and_remove(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='to-do-list']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

        to_do_list = self.driver.find_elements(By.XPATH, "//div[@id='container']//ul/li")

        for each_todo_list in to_do_list:
            each_todo_list.click()
            time.sleep(1)


        self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        time.sleep(1)