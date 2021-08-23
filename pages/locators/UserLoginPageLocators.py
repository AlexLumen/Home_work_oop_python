from selenium.webdriver.common.by import By


class UserLoginFormLocators:
    TITLE_LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6:nth-child(2)>.well>h2")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, ".form-group>a")

