from selenium.webdriver.common.by import By
from pages.base_page import assert_element


def test_catalog(browser, url):
    """Test for catalog page"""
    browser.get(url)
    tablets = browser.find_element(By.CSS_SELECTOR, ".navbar-nav>li:nth-child(4)")
    tablets.click()
    title = browser.find_element(By.CSS_SELECTOR, "h2")
    title_text = title.text
    assert title_text == 'Tablets', \
        'Title invalid'
    assert_element("#input-sort", browser, 5)
    assert_element("#input-limit", browser, 5)
    assert_element("#grid-view", browser, 5)
    assert_element(".price", browser, 5)
