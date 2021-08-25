import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_browser(self):
        self.browser.get(self.url)

    def verify_element_visibility(self, how, what, timeout=10):
        """Проверка видимости элемента"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise AssertionError("Не дождался видимости элемента: {}".format(what))

    def click_element(self, how, what):
        """Кликнуть по элементу"""
        element = self.browser.find_element(how, what)
        element.click()

    def click_element_action(self, how, what):
        element = self.browser.find_element(how, what)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click(element).perform()

    def get_text(self, how, what):
        """Получить текст элемента"""
        element_text = self.browser.find_element(how, what).text
        return element_text

    def send_text(self, how, what, text):
        """Получить текст элемента"""
        element = self.browser.find_element(how, what)
        element.clear()
        element.send_keys(text)

    def alert_accept(self):
        confirm_alert = self.browser.switch_to.alert
        print(confirm_alert.text)
        confirm_alert.accept()
