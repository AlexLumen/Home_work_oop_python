from pages.AdminPage import AdminPage


def test_admin_page(authorization_to_admin_page, browser, url):
    admin_page = AdminPage(browser, url)
    admin_page.should_be_logo_open_cart()
    admin_page.should_be_header_menu_navigation()
    admin_page.should_be_user_profile()
    admin_page.should_be_logout_icon()
    admin_page.should_be_settings_button()
