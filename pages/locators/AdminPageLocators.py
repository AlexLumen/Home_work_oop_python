from selenium.webdriver.common.by import By


class AdminPageLocators:
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    BUTTON_SETTING = (By.CSS_SELECTOR, "#button-setting")
    HEADER_NAVIGATION_MENU = (By.CSS_SELECTOR, "#navigation")
    LOGO_OPEN_CART = (By.CSS_SELECTOR, "#header-logo")
    LOGOUT_ICON = (By.CSS_SELECTOR, ".fa-sign-out")
    USER_PROFILE = (By.CSS_SELECTOR, "#user-profile")
