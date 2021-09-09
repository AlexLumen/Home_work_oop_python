import allure
from pages.RegistrationPage import RegistrationPage
from pages.elements.TopNavbar import TopNavbar


@allure.title("Тест регистрации пользователя")
def test_registration_user(browser, url):
    top_navbar_page = TopNavbar(browser, url)
    top_navbar_page.open_browser()
    top_navbar_page.click_my_account_icon()
    top_navbar_page.click_registration_item()
    registration_page = RegistrationPage(browser, url)
    registration_page.input_first_name()
    registration_page.input_last_name()
    registration_page.input_email()
    registration_page.input_email()
    registration_page.input_phone()
    registration_page.input_password()
    registration_page.input_password_confirm()
    registration_page.click_check_box_policy()
    registration_page.click_continue_button()
    registration_page.verify_success_message()
