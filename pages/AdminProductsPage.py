from allure import step
from helpers import random_string
from .BasePage import BasePage
from .locators.AdminProductsPageLocators import AdminProductsPageLocators


class AdminProductsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.product_name = '123456'

    @step("Клик по кнопке добавления продукта")
    def click_add_product_button(self):
        self.click_element(*AdminProductsPageLocators.ADD_PRODUCT_BUTTON)

    @step("Ввод названия продукта")
    def input_product_name(self):
        self.send_text(*AdminProductsPageLocators.INPUT_PRODUCT_NAME, self.product_name)

    @step("Ввод мета тега продукта")
    def input_meta_tag_title(self):
        self.send_text(*AdminProductsPageLocators.INPUT_MEGA_TAG_TITLE, random_string())

    @step("Клик по табу")
    def click_tab_data(self):
        self.click_element(*AdminProductsPageLocators.DATA_TAB)

    @step("Ввод модели")
    def input_model(self):
        self.send_text(*AdminProductsPageLocators.INPUT_MODEL, random_string())

    @step("Клик по кнопке сохранения продукта")
    def click_save_product_button(self):
        self.click_element(*AdminProductsPageLocators.SAVE_BUTTON)

    @step("Проверка сообщения об успешном добавлении")
    def verify_success_message(self):
        success_message = self.get_text(*AdminProductsPageLocators.SUCCESS_MESSAGE)
        success_message = success_message[:-2:]
        assert success_message == "Success: You have modified products!", \
            "Success message incorrect"

    @step("Поиск продукта по имени")
    def find_product_name(self):
        self.send_text(*AdminProductsPageLocators.INPUT_PRODUCT_NAME_IN_FILTER, self.product_name)

    @step("Клик по кнопке фильтрации")
    def click_button_filter(self):
        self.click_element(*AdminProductsPageLocators.BUTTON_FILTER)

    @step("Клик по чекбоксу")
    def click_check_box_by_position(self):
        checkboxes = self.browser.find_elements(*AdminProductsPageLocators.CHECK_BOX_IN_PRODUCT_TABLE)
        for index in range(len(checkboxes)):
            if index == 1:
                checkboxes[index].click()

    @step("Клик по кнопке удаления продукта")
    def click_delete_product_button(self):
        self.click_element_action(*AdminProductsPageLocators.DELETE_PRODUCT_BUTTON)
