from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=firstname]")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=lastname]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name=email]")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "input[name=telephone]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=password]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=confirm]")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#content>h1")
    CHECK_BOX_POLICY = (By.CSS_SELECTOR, "input[type=checkbox]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value=Continue]")
