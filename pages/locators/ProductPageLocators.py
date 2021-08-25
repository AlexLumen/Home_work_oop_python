from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    COUNT_INPUT = (By.CSS_SELECTOR, "input[name=quantity]")
    DESCRIPTION_TAB = (By.CSS_SELECTOR, "[href='#tab-description']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-4>.list-unstyled:nth-child(4)")
