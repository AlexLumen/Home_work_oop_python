from ..BasePage import BasePage
from pages.elements.locators.MainMenuLocators import MainMenuLocators


class MainMenu(BasePage):
    def click_tablet_menu_item(self):
        self.click_element(*MainMenuLocators.TABLETS)
