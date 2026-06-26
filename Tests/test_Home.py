import pytest
from selenium import webdriver

from Pages.home_page import HomePage
from Pages._contact_tab import ContactTab
from Pages._login_tab import LoginTab
from Pages._button_clicks_tab import ButtonClickTab
from Pages._todo_list_tab import ToDoListTab
from Pages._page_object_model import PageObjectModel
from Pages._accordion_tab import AccordionTextEffect


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# HOME PAGE
def test_home_navigation(driver):
    page = HomePage(driver)
    page.open()
    page.scroll_page()
    page.click_logo()

def test_course_navigation(driver):
    page = HomePage(driver)
    page.open()
    page.click_course()

def test_challenges_navigation(driver):
    page = HomePage(driver)
    page.open()
    page.click_contact_us()
    page.click_login()
    page.click_button_click()
    page.click_to_do()
    page.click_object_model()
    page.click_card_link()
    page.click_drop_check_radio()
    page.click_ajax_loader()
    page.click_actions()
    page.click_scroll_around()
    page.click_popup_alerts()
    page.click_iframe()
    page.click_hidden_elements()
    page.click_data_table()
    page.click_autocomplete_textfield()
    page.click_file_upload()
    page.click_date_picker()
    page.click_ai_playground()

# CONTACT US
def test_contact_inputs(driver):
    page = ContactTab(driver)
    page.open()
    page.input_details()
    page.input_empty()

# LOGIN PORTAL
def test_login_portal(driver):
    page = LoginTab(driver)
    page.open()
    page.login_portal()

# BUTTON CLICKS
def test_button_clicks(driver):
    page = ButtonClickTab(driver)
    page.open()
    page.button_dot_clicks()
    page.button_js_clicks()
    page.button_action_move_click()

# TO DO LIST
def test_to_do_list(driver):
    page = ToDoListTab(driver)
    page.open()
    page.add_to_list()
    page.strikethrough()
    page.hover_delete()
    page.add_strike_remove()

# PAGE OBJECT MODEL
def test_page_object_model(driver):
    page = PageObjectModel(driver)
    page.open()
    page.controls_and_navigation()
    page.nav_our_products()
    page.nav_contact_us()

# ACCORDION AND TEXT EFFECTS
def test_accordion_and_text_effect(driver):
    page = AccordionTextEffect(driver)
    page.open()
    page.toggle_panels()