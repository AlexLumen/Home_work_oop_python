from selenium.webdriver.common.by import By


class AdminNavigationMenuLocators:
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    CATALOG_PRODUCTS = (By.CSS_SELECTOR, "#collapse1>li:nth-child(2)>a")
