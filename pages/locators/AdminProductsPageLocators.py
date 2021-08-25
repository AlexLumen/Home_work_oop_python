from selenium.webdriver.common.by import By


class AdminProductsPageLocators:
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(2)")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(4)")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_MEGA_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_TAB = (By.CSS_SELECTOR, ".nav-tabs>:nth-child(2)")
    INPUT_MODEL = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")
    CHECK_BOX_IN_PRODUCT_TABLE = (By.CSS_SELECTOR, "input[type=checkbox]")
    INPUT_PRODUCT_NAME_IN_FILTER = (By.CSS_SELECTOR, "#input-name")
    BUTTON_FILTER = (By.CSS_SELECTOR, "#button-filter")
