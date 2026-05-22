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

def test_courses_button(driver):
    page = HomePage(driver)
    page.open()
    page.click_courses()