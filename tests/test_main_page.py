from selenium.webdriver.common.by import By
from pages.base_page import assert_element


def test_main_page(browser, url):
    """Test for main page"""
    browser.get(url)
    logo = browser.find_element(By.CSS_SELECTOR, "#logo")
    logo_text = logo.text
    assert logo_text == 'Your Store', \
        'Logo text invalid'
    assert_element("#top", browser, 5)
    assert_element(".input-lg", browser, 5)
    assert_element(".input-group-btn>.btn-lg", browser, 5)
    assert_element(".col-sm-3>.btn-block", browser, 5)
