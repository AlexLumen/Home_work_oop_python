from pages.MainPage import MainPage


def test_main_page(browser, url):
    """Test for main page"""
    page = MainPage(browser, url)
    page.open_browser()
    page.verify_logo_store()
    page.should_be_input_search()
    page.should_be_top_navbar()
    page.should_be_search_button()
    page.should_be_button_cart()
