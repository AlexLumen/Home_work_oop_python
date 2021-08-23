from ..BasePage import BasePage
from pages.elements.locators.TopNavbarLocators import TopNavbarLocators


class TopNavbar(BasePage):
    def click_my_account_icon(self):
        self.click_element(*TopNavbarLocators.MY_ACCOUNT_ICON)

    def click_login_item(self):
        self.click_element(*TopNavbarLocators.MY_ACCOUNT_MENU_LOGIN_ITEM)

    def click_registration_item(self):
        self.click_element(*TopNavbarLocators.MY_ACCOUNT_MENU_REGISTRATION_ITEM)

    def click_chose_currency_button(self):
        self.click_element(*TopNavbarLocators.CHOSE_CURRENCY_BUTTON)

    def click_eur_button(self):
        self.click_element(*TopNavbarLocators.BUTTON_EUR)

    def click_usd_button(self):
        self.click_element(*TopNavbarLocators.BUTTON_USD)

    def click_gbp_button(self):
        self.click_element(*TopNavbarLocators.BUTTON_GBP)

    def verify_chosen_euro_currency(self):
        currency_symbol = self.get_text(*TopNavbarLocators.CURRENCY_SYMBOL)
        assert currency_symbol == "€"

    def verify_chosen_usd_currency(self):
        currency_symbol = self.get_text(*TopNavbarLocators.CURRENCY_SYMBOL)
        assert currency_symbol == "$"

    def verify_chosen_gbp_currency(self):
        currency_symbol = self.get_text(*TopNavbarLocators.CURRENCY_SYMBOL)
        assert currency_symbol == "£"
