import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Fixture to initialize and quit the browser."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()