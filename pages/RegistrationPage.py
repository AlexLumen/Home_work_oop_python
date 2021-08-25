from helpers import random_string, random_email, random_phone
from pages.BasePage import BasePage
from pages.locators.RegistrationPageLocators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def input_first_name(self):
        self.send_text(*RegistrationPageLocators.FIRST_NAME_INPUT, random_string())

    def input_last_name(self):
        self.send_text(*RegistrationPageLocators.LAST_NAME_INPUT, random_string())

    def input_email(self):
        self.send_text(*RegistrationPageLocators.EMAIL_INPUT, random_email())

    def input_phone(self):
        self.send_text(*RegistrationPageLocators.TELEPHONE_INPUT, random_phone())

    def input_password(self):
        password = random_string()
        self.send_text(*RegistrationPageLocators.PASSWORD_INPUT, password)
        return password

    def input_password_confirm(self):
        self.send_text(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT, self.input_password())

    def click_check_box_policy(self):
        self.click_element(*RegistrationPageLocators.CHECK_BOX_POLICY)

    def click_continue_button(self):
        self.click_element(*RegistrationPageLocators.CONTINUE_BUTTON)

    def verify_success_message(self):
        success_message = self.get_text(*RegistrationPageLocators.SUCCESS_TITLE)
        assert success_message == "Your Account Has Been Created!", \
            "Invalid success message"
