from pages.ProductPage import ProductPage
from pages.elements.MainMenu import MainMenu
from pages.elements.ProductItems import ProductItems


def test_product_page(browser, url):
    """Test for product page"""
    main_menu_page = MainMenu(browser, url)
    main_menu_page.open_browser()
    main_menu_page.click_tablet_menu_item()
    product_items_page = ProductItems(browser, url)
    product_items_page.click_on_product_name()
    product_page = ProductPage(browser, url)
    product_page.should_be_product_name()
    product_page.should_be_description_tab()
    product_page.should_be_count_items_input()
    product_page.should_be_add_to_cart_button()
    product_page.should_be_product_price()
