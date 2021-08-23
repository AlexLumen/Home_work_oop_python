from pages.AdminPage import AdminPage


def test_admin_page(authorization_to_admin_page, browser, url):
    page = AdminPage(browser, url)
    page.should_be_logo_open_cart()
    page.should_be_header_menu_navigation()
    page.should_be_user_profile()
    page.should_be_logout_icon()
    page.should_be_settings_button()
