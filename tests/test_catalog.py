from pages.CatalogPage import CatalogPage
from pages.elements.MainMenu import MainMenu


def test_catalog(browser, url):
    """Test for catalog page"""
    page = MainMenu(browser, url)
    page.browser.get(url)
    page.click_tablet_menu_item()
    page = CatalogPage(browser, url)
    page.verify_tablets_title()
    page.should_be_greed_view_button()
    page.should_be_list_view_button()
    page.should_be_select_for_items_limit()
    page.should_be_select_for_sort_by()
