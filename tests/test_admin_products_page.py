from pages.AdminProductsPage import AdminProductsPage


def test_add_new_product(browser, url, authorization_to_admin_page, add_new_product_on_admin_page):
    page = AdminProductsPage(browser, url)
    page.verify_success_message()


def test_delete_product(browser, url, authorization_to_admin_page, add_new_product_on_admin_page):
    page = AdminProductsPage(browser, url)
    page.find_product_name()
    page.click_button_filter()
    page.click_check_box_by_position()
    page.click_delete_product_button()
    page.alert_accept()
    page.verify_success_message()
