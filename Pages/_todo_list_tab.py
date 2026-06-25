import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from window_utils import WindowUtils


class ToDoListTab:
    todo_list = ["Go to work",
                 "Eat lunch",
                 "Go home"]

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    def window_handler(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='to-do-list']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

    # ADD TO LIST
    def add_to_list(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        for each_todo in self.todo_list:
            self.driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys(each_todo + Keys.ENTER)
            time.sleep(1)

        self.driver.close()
        self.driver.switch_to.window(main_window)

    # STRIKETHROUGH
    def strikethrough(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        to_do_list = self.driver.find_elements(By.XPATH, "//div[@id='container']//ul/li")

        for each_todo_list in to_do_list:
            each_todo_list.click()
            time.sleep(1)

        self.driver.close()
        self.driver.switch_to.window(main_window)

    # HOVER AND DELETE
    def hover_delete(self):
        main_window = self.driver.current_window_handle
        self.window_handler()

        to_do_list = self.driver.find_elements(By.XPATH, "//div[@id='container']//ul/li")

        for each_todo_list in to_do_list:
            each_todo_list.find_element(By.XPATH, "//i[@class='fa fa-trash']").click()
            time.sleep(1)

        self.driver.close()
        self.driver.switch_to.window(main_window)

    def add_strike_remove(self):
        self.window_handler()

        # ADD TO LIST
        for each_todo in self.todo_list:
            self.driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys(each_todo + Keys.ENTER)
            time.sleep(1)

        # STRIKETHROUGH
        to_do_list = self.driver.find_elements(By.XPATH, "//div[@id='container']//ul/li")

        for each_todo_list in range(3):
            strike = to_do_list[each_todo_list]
            strike.click()
            time.sleep(1)

        # REMOVE
        for each_todo_list in to_do_list:
            each_todo_list.find_element(By.XPATH, "//i[@class='fa fa-trash']").click()
            time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[@id='home-link']").click()
        time.sleep(1)
        self.driver.close()
