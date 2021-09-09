from allure import step
from ..BasePage import BasePage
from pages.elements.locators.ProductItemsLocators import ProductItemsLocators


class ProductItems(BasePage):
    @step("Клик по наименованю продукта")
    def click_on_product_name(self):
        self.click_element(*ProductItemsLocators.PRODUCT_NAME)
