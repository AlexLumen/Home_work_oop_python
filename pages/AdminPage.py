from allure import step
from .BasePage import BasePage
from .locators.AdminPageLocators import AdminPageLocators


class AdminPage(BasePage):
    @step("Авторизация в админке")
    def authorization_to_admin_page(self, login, password):
        self.send_text(*AdminPageLocators.INPUT_LOGIN, login)
        self.send_text(*AdminPageLocators.INPUT_PASSWORD, password)
        self.click_element(*AdminPageLocators.LOGIN_BUTTON)

    @step("Проверка отображения логотипа опенкарта")
    def should_be_logo_open_cart(self):
        self.verify_element_visibility(*AdminPageLocators.LOGO_OPEN_CART)

    @step("Проверка отображения профиля пользователя")
    def should_be_user_profile(self):
        self.verify_element_visibility(*AdminPageLocators.USER_PROFILE)

    @step("Проверка отображения иконки логаута")
    def should_be_logout_icon(self):
        self.verify_element_visibility(*AdminPageLocators.LOGOUT_ICON)

    @step("Проверка отображения заголовка меню навигации")
    def should_be_header_menu_navigation(self):
        self.verify_element_visibility(*AdminPageLocators.HEADER_NAVIGATION_MENU)

    @step("Проверка отображения кнопки настроек")
    def should_be_settings_button(self):
        self.verify_element_visibility(*AdminPageLocators.BUTTON_SETTING)
