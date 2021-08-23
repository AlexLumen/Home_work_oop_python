import os
import pytest
from selenium import webdriver
from pages.AdminPage import AdminPage
from pages.AdminProductsPage import AdminProductsPage
from pages.elements.AdminNavigationMenu import AdminNavigationMenu
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser('C://browdriver')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     choices=["chrome", "firefox", "opera", "yandex"])
    parser.addoption('--url', action='store', default='https://demo.opencart.com')
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

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

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver


@pytest.fixture(scope='function', autouse=False)
def authorization_to_admin_page(browser, url):
    login = 'demo'
    password = 'demo'
    browser.get(url + '/admin')
    if url != 'https://demo.opencart.com':
        login = 'user'
        password = 'bitnami'
    page = AdminPage(browser, url)
    page.authorization_to_admin_page(login, password)


@pytest.fixture(scope='function', autouse=False)
def add_new_product_on_admin_page(browser, url):
    page = AdminNavigationMenu(browser, url)
    page.open_products_catalog()
    page = AdminProductsPage(browser, url)
    page.click_add_product_button()
    page.input_product_name()
    page.input_meta_tag_title()
    page.click_tab_data()
    page.input_model()
    page.click_save_product_button()
