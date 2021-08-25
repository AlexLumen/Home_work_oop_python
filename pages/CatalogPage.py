from .BasePage import BasePage
from .locators.CatalogPageLocators import CatalogPageLocators


class CatalogPage(BasePage):

    def find_catalog_title(self):
        title_text = self.get_text(*CatalogPageLocators.CATALOG_HEADER)
        return title_text

    def verify_tablets_title(self):
        assert self.find_catalog_title() == 'Tablets', \
            'Catalog title invalid'

    def should_be_greed_view_button(self):
        self.verify_element_visibility(*CatalogPageLocators.GREED_VIEW_BUTTON)

    def should_be_list_view_button(self):
        self.verify_element_visibility(*CatalogPageLocators.LIST_VIEW_BUTTON)

    def should_be_select_for_sort_by(self):
        self.verify_element_visibility(*CatalogPageLocators.SELECT_SORT_BY)

    def should_be_select_for_items_limit(self):
        self.verify_element_visibility(*CatalogPageLocators.SELECT_ITEMS_LIMIT)
