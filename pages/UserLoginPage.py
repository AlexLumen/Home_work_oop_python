from allure import step
from pages.BasePage import BasePage
from pages.locators.UserLoginPageLocators import UserLoginFormLocators


class UserLoginPage(BasePage):
    @step("Проверка отображения заголовка страницы")
    def verify_login_form_title(self):
        login_form_title_text = self.get_text(*UserLoginFormLocators.TITLE_LOGIN_FORM)
        assert login_form_title_text == "Returning Customer", \
            "Invalid login title"

    @step("Проверка отображения поля логин")
    def should_be_input_login(self):
        self.verify_element_visibility(*UserLoginFormLocators.INPUT_EMAIL)

    @step("Проверка отображения поля пароль")
    def should_be_input_password(self):
        self.verify_element_visibility(*UserLoginFormLocators.INPUT_PASSWORD)

    @step("Проверка отображения кнопки авторизации")
    def should_be_login_button(self):
        self.verify_element_visibility(*UserLoginFormLocators.LOGIN_BUTTON)

    @step("Проверка отображения ссылки Забыли пароль")
    def should_be_forgotten_password_link(self):
        self.verify_element_visibility(*UserLoginFormLocators.FORGOTTEN_PASSWORD_LINK)
