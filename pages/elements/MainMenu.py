from allure import step
from ..BasePage import BasePage
from pages.elements.locators.MainMenuLocators import MainMenuLocators


class MainMenu(BasePage):
    @step("Клик по пункту меню Tablets")
    def click_tablet_menu_item(self):
        self.click_element(*MainMenuLocators.TABLETS)
