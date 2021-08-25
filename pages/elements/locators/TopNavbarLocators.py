from selenium.webdriver.common.by import By


class TopNavbarLocators:
    MY_ACCOUNT_ICON = (By.CSS_SELECTOR, ".fa-user")
    MY_ACCOUNT_MENU_LOGIN_ITEM = (By.CSS_SELECTOR, ".dropdown-menu-right>li:nth-child(2)")
    MY_ACCOUNT_MENU_REGISTRATION_ITEM = (By.CSS_SELECTOR, ".dropdown-menu-right>li:nth-child(1)")
    CHOSE_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency>.btn-group>.dropdown-toggle")
    BUTTON_GBP = (By.CSS_SELECTOR, "button[name=GBP]")
    BUTTON_EUR = (By.CSS_SELECTOR, "button[name=EUR]")
    BUTTON_USD = (By.CSS_SELECTOR, "button[name=USD]")
    CURRENCY_SYMBOL = (By.CSS_SELECTOR, ".dropdown-toggle>strong")
