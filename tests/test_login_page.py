from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page(browser, url):
    """Test for login page"""
    browser.get(url)
    wait = WebDriverWait(browser, 7)
    fa_account = browser.find_element(By.CSS_SELECTOR, ".fa-user")
    fa_account.click()
    login_menu_item = browser.find_element(By.CSS_SELECTOR, ".dropdown-menu-right>li:nth-child(2)")
    login_menu_item.click()
    title_login_form = browser.find_element(By.CSS_SELECTOR, ".col-sm-6:nth-child(2)>.well>h2")
    title_login_form_text = title_login_form.text
    assert title_login_form_text == "Returning Customer", \
        "Invalid login title"
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    except TimeoutException:
        raise AssertionError("Did not wait for the email input element to be visible, it may be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    except TimeoutException:
        raise AssertionError("Did not wait for the password input element to be visible, it may be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.btn")))
    except TimeoutException:
        raise AssertionError("Did not wait for the login button element to be visible, it may be missing")
    try:
        assert wait.until((EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-group>a"))))
    except TimeoutException:
        raise AssertionError("Did not wait for the forgot password element to be visible, it may be missing")
