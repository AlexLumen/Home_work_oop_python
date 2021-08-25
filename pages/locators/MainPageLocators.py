from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_NAVBAR = (By.CSS_SELECTOR, "#top")
    LOGO_YOUR_STORE = (By.CSS_SELECTOR, "#logo")
    INPUT_SEARCH = (By.CSS_SELECTOR, ".input-lg")
    BUTTON_SEARCH = (By.CSS_SELECTOR, ".input-group-btn>.btn-lg")
    BUTTON_CART = (By.CSS_SELECTOR, "#cart")
