from allure import step
from .BasePage import BasePage
from .locators.MainPageLocators import MainPageLocators


class MainPage(BasePage):
    @step("Проверка текста логотипа")
    def verify_logo_store(self):
        self.verify_element_visibility(*MainPageLocators.LOGO_YOUR_STORE)

    @step("Проверка верхнего меню")
    def should_be_top_navbar(self):
        self.verify_element_visibility(*MainPageLocators.TOP_NAVBAR)

    @step("Проверка отображения поля поиска")
    def should_be_input_search(self):
        self.verify_element_visibility(*MainPageLocators.INPUT_SEARCH)

    @step("Проверка отображения кнопки поиска")
    def should_be_search_button(self):
        self.verify_element_visibility(*MainPageLocators.BUTTON_SEARCH)

    @step("Проверка отображения кнопки добавления в корзину")
    def should_be_button_cart(self):
        self.verify_element_visibility(*MainPageLocators.BUTTON_CART)
