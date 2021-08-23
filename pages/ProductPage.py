from .BasePage import BasePage
from .locators.ProductPageLocators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        self.verify_element_visibility(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def should_be_count_items_input(self):
        self.verify_element_visibility(*ProductPageLocators.COUNT_INPUT)

    def should_be_description_tab(self):
        self.verify_element_visibility(*ProductPageLocators.DESCRIPTION_TAB)

    def should_be_product_name(self):
        self.verify_element_visibility(*ProductPageLocators.PRODUCT_NAME)

    def should_be_product_price(self):
        self.verify_element_visibility(*ProductPageLocators.PRODUCT_PRICE)
