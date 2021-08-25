import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    def open_browser(self):
        self.logger.info("Opening url: {}".format(self.url))
        self.browser.get(self.url)

    def verify_element_visibility(self, how, what, timeout=10):
        """Проверка видимости элемента"""
        try:
            self.logger.info(f"Wait {what} to be visibility")
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            self.logger.error(f"Element {what} is not visibility in page")
            raise AssertionError("Не дождался видимости элемента: {}".format(what))

    def click_element(self, how, what):
        """Кликнуть по элементу"""
        self.logger.info(f"Wait {what} to be visibility")
        element = self.browser.find_element(how, what)
        element.click()

    def click_element_action(self, how, what):
        self.logger.info("Clicking element: {}".format(what))
        element = self.browser.find_element(how, what)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click(element).perform()

    def get_text(self, how, what):
        """Получить текст элемента"""
        self.logger.info("Get text: {}".format(what))
        element_text = self.browser.find_element(how, what).text
        return element_text

    def send_text(self, how, what, text):
        """Напечатать текст"""
        element = self.browser.find_element(how, what)
        self.logger.info("Clearing text: {}".format(what))
        element.clear()
        self.logger.info("Input text: {}".format(what))
        element.send_keys(text)

    def alert_accept(self):
        confirm_alert = self.browser.switch_to.alert
        print(confirm_alert.text)
        self.logger.info("Accept alert")
        confirm_alert.accept()
