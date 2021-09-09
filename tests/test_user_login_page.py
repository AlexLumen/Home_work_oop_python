import allure
from pages.UserLoginPage import UserLoginPage
from pages.elements.TopNavbar import TopNavbar


@allure.title("Проверка страницы авторизации")
def test_user_login_page(browser, url):
    """Test for login page"""
    top_nav_bar_page = TopNavbar(browser, url)
    top_nav_bar_page.open_browser()
    top_nav_bar_page.click_my_account_icon()
    top_nav_bar_page.click_login_item()
    login_form_page = UserLoginPage(browser, url)
    login_form_page.verify_login_form_title()
    login_form_page.should_be_input_login()
    login_form_page.should_be_input_password()
    login_form_page.should_be_login_button()
    login_form_page.should_be_forgotten_password_link()
