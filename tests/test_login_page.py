from selenium.webdriver.common.by import By
from pages.base_page import assert_element


def test_login_page(browser, url):
    """Test for login page"""
    browser.get(url)
    fa_account = browser.find_element(By.CSS_SELECTOR, ".fa-user")
    fa_account.click()
    login_menu_item = browser.find_element(By.CSS_SELECTOR, ".dropdown-menu-right>li:nth-child(2)")
    login_menu_item.click()
    title_login_form = browser.find_element(By.CSS_SELECTOR, ".col-sm-6:nth-child(2)>.well>h2")
    title_login_form_text = title_login_form.text
    assert title_login_form_text == "Returning Customer", \
        "Invalid login title"
    assert_element("#input-email", browser, 5)
    assert_element("#input-password", browser, 5)
    assert_element("input.btn", browser, 5)
    assert_element(".form-group>a", browser, 5)
