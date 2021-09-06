import logging
import allure

from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
        try:
            self.logger.info(f"Wait {what} to be visibility")
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            self.logger.error(f"Element {what} is not visibility in page")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Не дождался видимости элемента: {}".format(what))

    def click_element(self, how, what):
        """Кликнуть по элементу"""
        try:
            self.logger.info(f"Wait {what} to be visibility")
            element = self.browser.find_element(how, what)
            element.click()
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def click_element_action(self, how, what):
        try:
            self.logger.info("Clicking element: {}".format(what))
            element = self.browser.find_element(how, what)
            ActionChains(self.browser).pause(0.3).move_to_element(element).click(element).perform()
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def get_text(self, how, what):
        """Получить текст элемента"""
        try:
            self.logger.info("Get text: {}".format(what))
            element_text = self.browser.find_element(how, what).text
            return element_text
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def send_text(self, how, what, text):
        """Напечатать текст"""
        try:
            element = self.browser.find_element(how, what)
            self.logger.info("Clearing text: {}".format(what))
            element.clear()
            self.logger.info("Input text: {}".format(what))
            element.send_keys(text)
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def alert_accept(self):
        confirm_alert = self.browser.switch_to.alert
        print(confirm_alert.text)
        self.logger.info("Accept alert")
        confirm_alert.accept()
