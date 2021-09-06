from allure import step
from ..BasePage import BasePage
from pages.elements.locators.AdminNavigationMenuLocators import AdminNavigationMenuLocators


class AdminNavigationMenu(BasePage):
    @step("Клик по меню каталога")
    def click_catalog_menu(self):
        self.click_element_action(*AdminNavigationMenuLocators.MENU_CATALOG)

    @step("Клик по продукту каталога")
    def click_product_catalog(self):
        self.click_element_action(*AdminNavigationMenuLocators.CATALOG_PRODUCTS)

    @step("Открытие каталога продуктов")
    def open_products_catalog(self):
        self.click_catalog_menu()
        self.click_product_catalog()
