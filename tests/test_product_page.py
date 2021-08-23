from pages.ProductPage import ProductPage
from pages.elements.MainMenu import MainMenu
from pages.elements.ProductItems import ProductItems


def test_product_page(browser, url):
    """Test for product page"""
    page = MainMenu(browser, url)
    page.open_browser()
    page.click_tablet_menu_item()
    page = ProductItems(browser, url)
    page.click_on_product_name()
    page = ProductPage(browser, url)
    page.should_be_product_name()
    page.should_be_description_tab()
    page.should_be_count_items_input()
    page.should_be_add_to_cart_button()
    page.should_be_product_price()
