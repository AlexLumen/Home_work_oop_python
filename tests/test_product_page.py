from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page(browser, url):
    """Test for product page"""
    browser.get(url)
    wait = WebDriverWait(browser, 7)
    tablets = browser.find_element(By.CSS_SELECTOR, ".navbar-nav>li:nth-child(4)")
    tablets.click()
    caption_header = browser.find_element(By.CSS_SELECTOR, "h4")
    caption_header.click()
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the add cart button element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-3>.btn-block")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the cart button element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-group>.form-control")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the input count element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='#tab-description']")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the tab description  element to be visible, it might be missing")
    try:
        assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    except TimeoutException:
        raise AssertionError("Didn't wait for the product name element to be visible, it might be missing")
