import allure
from pages.AdminProductsPage import AdminProductsPage


@allure.title("Добавление нового продукта")
def test_add_new_product(browser, url, authorization_to_admin_page, add_new_product_on_admin_page):
    admin_products_page = AdminProductsPage(browser, url)
    admin_products_page.verify_success_message()


@allure.title("Удаление продукта")
def test_delete_product(browser, url, authorization_to_admin_page, add_new_product_on_admin_page):
    admin_products_page = AdminProductsPage(browser, url)
    admin_products_page.find_product_name()
    admin_products_page.click_button_filter()
    admin_products_page.click_check_box_by_position()
    admin_products_page.click_delete_product_button()
    admin_products_page.alert_accept()
    admin_products_page.verify_success_message()
