import os
import pytest
import allure
import logging
from selenium import webdriver
from pages.AdminPage import AdminPage
from pages.AdminProductsPage import AdminProductsPage
from pages.elements.AdminNavigationMenu import AdminNavigationMenu
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser('C://browdriver')

logging.basicConfig(level=logging.INFO, filename="../selenium.log")
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     choices=["chrome", "firefox", "opera", "yandex"])
    parser.addoption('--url', action='store', default='https://demo.opencart.com')
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--bversion", action="store", default="92.0")
    parser.addoption("--vnc", action="store_true", default=True)


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")

    driver = None
    logger.info(f"Run browser {browser_name}")

    if executor == "localhost":

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver.exe", options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/geckodriver.exe", options=options)
        elif browser_name == "opera":
            options = OperaOptions()
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver.exe", options=options)
        elif browser_name == "yandex":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/yandexdriver.exe", options=options)
        else:
            raise pytest.UsageError("--browser_name should be chrome, firefox, opera, yandex")

        if maximized:
            driver.maximize_window()
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser_name,
            "browserVersion": version,
            "name": "test_opencart",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc
            }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities
        )

        driver.maximize_window()

    def final():
        logger.info(f"Browser {browser_name} close")
        driver.quit()

    request.addfinalizer(final)
    return driver


@allure.title("Просмотр страницы администратора")
@pytest.fixture(scope='function', autouse=False)
def authorization_to_admin_page(browser, url):
    login = 'demo'
    password = 'demo'
    browser.get(url + '/admin')
    if url != 'https://demo.opencart.com':
        login = 'user'
        password = 'bitnami'
    with allure.step("Авторизация в админке"):
        admin_page = AdminPage(browser, url)
        admin_page.authorization_to_admin_page(login, password)


@pytest.fixture(scope='function', autouse=False)
def add_new_product_on_admin_page(browser, url):
    with allure.step("Открыть каталог продуктов в меню навигации админки"):
        admin_navigation_menu_page = AdminNavigationMenu(browser, url)
        admin_navigation_menu_page.open_products_catalog()
    with allure.step("Добавить новый продукт"):
        admin_products_page = AdminProductsPage(browser, url)
        admin_products_page.click_add_product_button()
        admin_products_page.input_product_name()
        admin_products_page.input_meta_tag_title()
        admin_products_page.click_tab_data()
        admin_products_page.input_model()
        admin_products_page.click_save_product_button()
