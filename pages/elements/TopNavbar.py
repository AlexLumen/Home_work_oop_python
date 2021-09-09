from allure import step
from ..BasePage import BasePage
from pages.elements.locators.TopNavbarLocators import TopNavbarLocators


class TopNavbar(BasePage):
    @step("Клик по иконке my account")
    def click_my_account_icon(self):
        self.click_element(*TopNavbarLocators.MY_ACCOUNT_ICON)

    @step("Клик по пункту меню логина")
    def click_login_item(self):
        self.click_element(*TopNavbarLocators.MY_ACCOUNT_MENU_LOGIN_ITEM)

    @step("Клик по пункту меню регистрации")
    def click_registration_item(self):
        self.click_element(*TopNavbarLocators.MY_ACCOUNT_MENU_REGISTRATION_ITEM)

    @step("Клик по кнопке выбора валюты")
    def click_chose_currency_button(self):
        self.click_element(*TopNavbarLocators.CHOSE_CURRENCY_BUTTON)

    @step("Клик по кнопке выбора евро")
    def click_eur_button(self):
        self.click_element(*TopNavbarLocators.BUTTON_EUR)

    @step("Клик по кнопке выбора долларов")
    def click_usd_button(self):
        self.click_element(*TopNavbarLocators.BUTTON_USD)

    @step("Клик по кнопке выбора фунтов стерлингов")
    def click_gbp_button(self):
        self.click_element(*TopNavbarLocators.BUTTON_GBP)

    @step("Проверка выбранной валюты евро")
    def verify_chosen_euro_currency(self):
        currency_symbol = self.get_text(*TopNavbarLocators.CURRENCY_SYMBOL)
        assert currency_symbol == "€"

    @step("Проверка выбранной валюты долларов")
    def verify_chosen_usd_currency(self):
        currency_symbol = self.get_text(*TopNavbarLocators.CURRENCY_SYMBOL)
        assert currency_symbol == "$"

    @step("Проверка выбранной валюты фунтов стерлингов")
    def verify_chosen_gbp_currency(self):
        currency_symbol = self.get_text(*TopNavbarLocators.CURRENCY_SYMBOL)
        assert currency_symbol == "£"
