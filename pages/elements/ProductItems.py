from ..BasePage import BasePage
from pages.elements.locators.ProductItemsLocators import ProductItemsLocators


class ProductItems(BasePage):
    def click_on_product_name(self):
        self.click_element(*ProductItemsLocators.PRODUCT_NAME)
