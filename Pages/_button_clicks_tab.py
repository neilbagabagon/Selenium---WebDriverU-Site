import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from window_utils import WindowUtils

class ButtonClickTab:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://webdriveruniversity.com/"

    def open(self):
        self.driver.get("https://webdriveruniversity.com/")

    def window_handler(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='button-clicks']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

    # Using WebElement.click()
    def button_dot_clicks(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='button-clicks']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)


        self.driver.find_element(By.XPATH, "//span[@id='button1']").click()
        time.sleep(1)
        button_close = self.driver.find_element(By.XPATH, "//div[@id='myModalClick']//button[@type='button'][normalize-space()='Close']")
        button_close.click()
        print("\nButton Clicked (WebEl): ", button_close.text)
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//span[@id='button1']").click()
        time.sleep(1)
        button_x = self.driver.find_element(By.XPATH, "//div[@id='myModalClick']//button[@type='button'][normalize-space()='×']")
        button_x.click()
        print("Button Clicked (WebEl): ", button_x.text)
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//span[@id='button1']").click()
        time.sleep(1)
        button_backdrop = self.driver.find_element(By.XPATH, "//div[@id='myModalClick']")
        button_backdrop.click()
        time.sleep(1)

        self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        time.sleep(1)

    # Using JavaScript click
    def button_js_clicks(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='button-clicks']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

        def open_click_me():
            time.sleep(1)
            click_me_button = self.driver.find_element(By.CSS_SELECTOR, "#button2")
            self.driver.execute_script("arguments[0].click();", click_me_button)
            time.sleep(1)

        open_click_me()
        button_close = self.driver.find_element(By.CSS_SELECTOR, "div[class='modal-dialog modal-md'] div[class='modal-footer'] button[type='button']")
        self.driver.execute_script("arguments[0].click();", button_close)
        print("\nButton Clicked (JS): ", button_close.text)
        time.sleep(1)

        open_click_me()
        button_x = self.driver.find_element(By.CSS_SELECTOR, "div[class='modal-dialog modal-md'] div[class='modal-header'] button[type='button']")
        self.driver.execute_script("arguments[0].click();", button_x)
        print("Button Clicked (JS): ", button_x.text)
        time.sleep(1)

        open_click_me()
        button_backdrop = self.driver.find_element(By.XPATH, "//div[@id='myModalJSClick']")
        self.driver.execute_script("arguments[0].click();", button_backdrop)
        time.sleep(1)

        self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        time.sleep(1)

    # Using Action Move & Click
    def button_action_move_click(self):
        button = self.driver.find_element(By.XPATH, "//a[@id='button-clicks']")
        main_window = self.driver.current_window_handle

        self.driver.execute_script("arguments[0].click();", button)
        WindowUtils.driver_switch_wait(self.driver)

        move_action = ActionChains(self.driver)

        def open_click_me():
            time.sleep(1)
            button_click_me = self.driver.find_element(By.XPATH, "//span[@id='button3']")
            move_action.move_to_element(button_click_me).click().perform()
            time.sleep(1)

        open_click_me()
        button_close = self.driver.find_element(By.XPATH, "//div[@id='myModalMoveClick']//button[@type='button'][normalize-space()='Close']")
        move_action.move_to_element(button_close).click().perform()
        print("\nButton Clicked (ActMove): ", button_close.text)
        time.sleep(1)

        open_click_me()
        button_x = self.driver.find_element(By.XPATH, "//div[@id='myModalMoveClick']//button[@type='button'][normalize-space()='×']")
        move_action.move_to_element(button_x).click().perform()
        print("Button Clicked (ActMove): ", button_x.text)
        time.sleep(1)

        open_click_me()
        button_backdrop = self.driver.find_element(By.XPATH, "//div[@id='myModalMoveClick']")
        self.driver.execute_script("arguments[0].click();", button_backdrop)
        time.sleep(1)

        self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        time.sleep(1)