from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, url):
    """Test for main page"""
    browser.get(url)
    wait = WebDriverWait(browser, 7)
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    logo_text = logo.text
    assert logo_text == 'Your Store', \
        'Logo text invalid'
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#top")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the header element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input-lg")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the search input element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input-group-btn>.btn-lg")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the search button element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-3>.btn-block")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the button cart element to be visible, it might be missing")
