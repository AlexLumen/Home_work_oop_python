from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_page(browser, url):
    """Test for admin page"""
    browser.get(url + 'admin/')
    wait = WebDriverWait(browser, 7)
    input_username = browser.find_element(By.CSS_SELECTOR, "#input-username")
    input_username.send_keys("demo")
    input_username = browser.find_element(By.CSS_SELECTOR, "#input-password")
    input_username.send_keys("demo")
    login_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    login_button.click()
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-logo")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the logo element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-profile")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the user profile element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-sign-out")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the fa-icon logout user element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#navigation")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the navigation element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-setting")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the setting button element to be visible, it might be missing")
