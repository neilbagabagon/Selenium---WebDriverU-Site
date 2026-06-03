import pytest
from selenium import webdriver
from Pages.home_page import HomePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_scroll(driver):
    page = HomePage(driver)
    page.open()
    page.scroll_page()


def test_logo_button(driver):
    page = HomePage(driver)
    page.open()
    page.click_logo()


def test_course_button(driver):
    page = HomePage(driver)
    page.open()
    page.click_course()


def test_contact_us(driver):
    page = HomePage(driver)
    page.open()
    page.click_contact_us()


def test_login(driver):
    page = HomePage(driver)
    page.open()
    page.click_login()


def test_button_click(driver):
    page = HomePage(driver)
    page.open()
    page.click_button_click()


def test_to_do(driver):
    page = HomePage(driver)
    page.open()
    page.click_to_do()


def test_object_model(driver):
    page = HomePage(driver)
    page.open()
    page.click_object_model()


def test_card_link(driver):
    page = HomePage(driver)
    page.open()
    page.click_card_link()


def test_drop_check_radio(driver):
    page = HomePage(driver)
    page.open()
    page.click_drop_check_radio()


def test_ajax_loader(driver):
    page = HomePage(driver)
    page.open()
    page.click_ajax_loader()


def test_actions(driver):
    page = HomePage(driver)
    page.open()
    page.click_actions()


def test_scroll_around(driver):
    page = HomePage(driver)
    page.open()
    page.click_scroll_around()


def test_popup_alerts(driver):
    page = HomePage(driver)
    page.open()
    page.click_popup_alerts()


def test_iframes(driver):
    page = HomePage(driver)
    page.open()
    page.click_iframe()


def test_hidden_elements(driver):
    page = HomePage(driver)
    page.open()
    page.click_hidden_elements()


def test_data_table(driver):
    page = HomePage(driver)
    page.open()
    page.click_data_table()

def test_autocomplete_textfield(driver):
    page = HomePage(driver)
    page.open()
    page.click_autocomplete_textfield()

def test_file_upload(driver):
    page = HomePage(driver)
    page.open()
    page.click_file_upload()

def test_date_picker(driver):
    page = HomePage(driver)
    page.open()
    page.click_date_picker()

def test_ai_playground(driver):
    page = HomePage(driver)
    page.open()
    page.click_ai_playground()
