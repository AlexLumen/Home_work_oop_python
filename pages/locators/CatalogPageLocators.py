from selenium.webdriver.common.by import By


class CatalogPageLocators:
    CATALOG_HEADER = (By.CSS_SELECTOR, "h2")
    GREED_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    SELECT_SORT_BY = (By.CSS_SELECTOR, "#input-sort")
    SELECT_ITEMS_LIMIT = (By.CSS_SELECTOR, "#input-sort")
