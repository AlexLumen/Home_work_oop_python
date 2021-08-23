from ..BasePage import BasePage
from pages.elements.locators.AdminNavigationMenuLocators import AdminNavigationMenuLocators


class AdminNavigationMenu(BasePage):
    def click_catalog_menu(self):
        self.click_element_action(*AdminNavigationMenuLocators.MENU_CATALOG)

    def click_product_catalog(self):
        self.click_element_action(*AdminNavigationMenuLocators.CATALOG_PRODUCTS)

    def open_products_catalog(self):
        self.click_catalog_menu()
        self.click_product_catalog()
