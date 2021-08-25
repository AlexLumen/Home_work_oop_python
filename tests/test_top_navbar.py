from pages.elements.TopNavbar import TopNavbar


def test_chose_euro_currency(browser, url):
    top_nav_bar_page = TopNavbar(browser, url)
    top_nav_bar_page.open_browser()
    top_nav_bar_page.click_chose_currency_button()
    top_nav_bar_page.click_eur_button()
    top_nav_bar_page.verify_chosen_euro_currency()


def test_chose_usd_currency(browser, url):
    top_nav_bar_page = TopNavbar(browser, url)
    top_nav_bar_page.open_browser()
    top_nav_bar_page.click_chose_currency_button()
    top_nav_bar_page.click_usd_button()
    top_nav_bar_page.verify_chosen_usd_currency()


def test_chose_gbp_currency(browser, url):
    top_nav_bar_page = TopNavbar(browser, url)
    top_nav_bar_page.open_browser()
    top_nav_bar_page.click_chose_currency_button()
    top_nav_bar_page.click_gbp_button()
    top_nav_bar_page.verify_chosen_gbp_currency()
