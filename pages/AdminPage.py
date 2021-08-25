from .BasePage import BasePage
from .locators.AdminPageLocators import AdminPageLocators


class AdminPage(BasePage):
    def authorization_to_admin_page(self, login, password):
        self.send_text(*AdminPageLocators.INPUT_LOGIN, login)
        self.send_text(*AdminPageLocators.INPUT_PASSWORD, password)
        self.click_element(*AdminPageLocators.LOGIN_BUTTON)

    def should_be_logo_open_cart(self):
        """Должен отображаться логотип опенкарта"""
        self.verify_element_visibility(*AdminPageLocators.LOGO_OPEN_CART)

    def should_be_user_profile(self):
        """Должен отображаться профиль пользователя"""
        self.verify_element_visibility(*AdminPageLocators.USER_PROFILE)

    def should_be_logout_icon(self):
        """Должна отображаться иконка логаута"""
        self.verify_element_visibility(*AdminPageLocators.LOGOUT_ICON)

    def should_be_header_menu_navigation(self):
        """Должен отображаться заголовок меню навигации"""
        self.verify_element_visibility(*AdminPageLocators.HEADER_NAVIGATION_MENU)

    def should_be_settings_button(self):
        """Должна быть кнопка настроек"""
        self.verify_element_visibility(*AdminPageLocators.BUTTON_SETTING)
