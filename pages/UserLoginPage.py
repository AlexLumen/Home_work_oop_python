from pages.BasePage import BasePage
from pages.locators.UserLoginPageLocators import UserLoginFormLocators


class UserLoginPage(BasePage):
    def verify_login_form_title(self):
        login_form_title_text = self.get_text(*UserLoginFormLocators.TITLE_LOGIN_FORM)
        assert login_form_title_text == "Returning Customer", \
            "Invalid login title"

    def should_be_input_login(self):
        self.verify_element_visibility(*UserLoginFormLocators.INPUT_EMAIL)

    def should_be_input_password(self):
        self.verify_element_visibility(*UserLoginFormLocators.INPUT_PASSWORD)

    def should_be_login_button(self):
        self.verify_element_visibility(*UserLoginFormLocators.LOGIN_BUTTON)

    def should_be_forgotten_password_link(self):
        self.verify_element_visibility(*UserLoginFormLocators.FORGOTTEN_PASSWORD_LINK)
