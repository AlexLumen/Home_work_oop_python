from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog(browser, url):
    """Test for catalog page"""
    browser.get(url)
    wait = WebDriverWait(browser, 7)
    tablets = browser.find_element(By.CSS_SELECTOR, ".navbar-nav>li:nth-child(4)")
    tablets.click()
    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))
    title_text = title.text
    assert title_text == 'Tablets', \
        'Title invalid'
    try:
        assert wait.until((EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-sort'))))
    except TimeoutException:
        raise AssertionError("Didn't wait for the sort input element to be visible, it might be missing")
    try:
        assert wait.until((EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-limit'))))
    except TimeoutException:
        raise AssertionError("Didn't wait for the limit input element to be visible, it might be missing")
    try:
        assert wait.until((EC.visibility_of_element_located((By.CSS_SELECTOR, '#grid-view'))))
    except TimeoutException:
        raise AssertionError("Didn't wait for the grid view button element to be visible, it might be missing")
    try:
        assert wait.until((EC.visibility_of_element_located((By.CSS_SELECTOR, '.price'))))
    except TimeoutException:
        raise AssertionError("Didn't wait for the price element to be visible, it might be missing")
