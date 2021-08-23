from pages.UserLoginPage import LoginForm
from pages.elements.TopNavbar import TopNavbar


def test_user_login_page(browser, url):
    """Test for login page"""
    page = TopNavbar(browser, url)
    page.open_browser()
    page.click_my_account_icon()
    page.click_login_item()
    page = LoginForm(browser, url)
    page.verify_login_form_title()
    page.should_be_input_login()
    page.should_be_input_password()
    page.should_be_login_button()
    page.should_be_forgotten_password_link()
