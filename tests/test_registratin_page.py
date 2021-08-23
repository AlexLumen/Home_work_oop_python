from pages.RegistrationPage import RegistrationPage
from pages.elements.TopNavbar import TopNavbar
import time


def test_registration_user(browser, url):
    page = TopNavbar(browser, url)
    page.open_browser()
    page.click_my_account_icon()
    page.click_registration_item()
    page = RegistrationPage(browser, url)
    page.input_first_name()
    page.input_last_name()
    page.input_email()
    page.input_email()
    page.input_phone()
    page.input_password()
    page.input_password_confirm()
    page.click_check_box_policy()
    page.click_continue_button()
    page.verify_success_message()
