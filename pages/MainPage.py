from .BasePage import BasePage
from .locators.MainPageLocators import MainPageLocators


class MainPage(BasePage):
    def verify_logo_store(self):
        logo_text = self.get_text(*MainPageLocators.LOGO_YOUR_STORE)
        assert logo_text == 'Your Store', \
            'Logo text invalid'

    def should_be_top_navbar(self):
        self.verify_element_visibility(*MainPageLocators.TOP_NAVBAR)

    def should_be_input_search(self):
        self.verify_element_visibility(*MainPageLocators.INPUT_SEARCH)

    def should_be_search_button(self):
        self.verify_element_visibility(*MainPageLocators.BUTTON_SEARCH)

    def should_be_button_cart(self):
        self.verify_element_visibility(*MainPageLocators.BUTTON_CART)
