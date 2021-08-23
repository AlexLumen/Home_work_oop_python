from helpers import random_string
from .BasePage import BasePage
from .locators.AdminProductsPageLocators import AdminProductsPageLocators


class AdminProductsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.product_name = '123456'

    def click_add_product_button(self):
        self.click_element(*AdminProductsPageLocators.ADD_PRODUCT_BUTTON)

    def input_product_name(self):
        self.send_text(*AdminProductsPageLocators.INPUT_PRODUCT_NAME, self.product_name)

    def input_meta_tag_title(self):
        self.send_text(*AdminProductsPageLocators.INPUT_MEGA_TAG_TITLE, random_string())

    def click_tab_data(self):
        self.click_element(*AdminProductsPageLocators.DATA_TAB)

    def input_model(self):
        self.send_text(*AdminProductsPageLocators.INPUT_MODEL, random_string())

    def click_save_product_button(self):
        self.click_element(*AdminProductsPageLocators.SAVE_BUTTON)

    def verify_success_message(self):
        success_message = self.get_text(*AdminProductsPageLocators.SUCCESS_MESSAGE)
        success_message = success_message[:-2:]
        assert success_message == "Success: You have modified products!", \
            "Success message incorrect"

    def find_product_name(self):
        self.send_text(*AdminProductsPageLocators.INPUT_PRODUCT_NAME_IN_FILTER, self.product_name)

    def click_button_filter(self):
        self.click_element(*AdminProductsPageLocators.BUTTON_FILTER)

    def click_check_box_by_position(self):
        checkboxes = self.browser.find_elements(*AdminProductsPageLocators.CHECK_BOX_IN_PRODUCT_TABLE)
        for index in range(len(checkboxes)):
            if index == 1:
                checkboxes[index].click()

    def click_delete_product_button(self):
        self.click_element_action(*AdminProductsPageLocators.DELETE_PRODUCT_BUTTON)
