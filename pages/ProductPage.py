from allure import step
from .BasePage import BasePage
from .locators.ProductPageLocators import ProductPageLocators


class ProductPage(BasePage):
    @step("Проверка отображения кнопки добавления товара в корзину")
    def should_be_add_to_cart_button(self):
        self.verify_element_visibility(*ProductPageLocators.ADD_TO_CART_BUTTON)

    @step("Проверка отображения поля ввода количества товара")
    def should_be_count_items_input(self):
        self.verify_element_visibility(*ProductPageLocators.COUNT_INPUT)

    @step("Проверка отображения таба Описание")
    def should_be_description_tab(self):
        self.verify_element_visibility(*ProductPageLocators.DESCRIPTION_TAB)

    @step("Проверка отображения названия продукта")
    def should_be_product_name(self):
        self.verify_element_visibility(*ProductPageLocators.PRODUCT_NAME)

    @step("Проверка отображения стоимости продукта")
    def should_be_product_price(self):
        self.verify_element_visibility(*ProductPageLocators.PRODUCT_PRICE)
