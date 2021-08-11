from selenium.webdriver.common.by import By
from pages.base_page import assert_element


def test_product_page(browser, url):
    """Test for product page"""
    browser.get(url)
    tablets = browser.find_element(By.CSS_SELECTOR, ".navbar-nav>li:nth-child(4)")
    tablets.click()
    caption_header = browser.find_element(By.CSS_SELECTOR, "h4")
    caption_header.click()
    assert_element("#button-cart", browser, 5)
    assert_element(".col-sm-3>.btn-block", browser, 5)
    assert_element(".form-group>.form-control", browser, 5)
    assert_element("[href='#tab-description']", browser, 5)
    assert_element("h1", browser, 5)
