from pages.elements.TopNavbar import TopNavbar


def test_chose_euro_currency(browser, url):
    page = TopNavbar(browser, url)
    page.open_browser()
    page.click_chose_currency_button()
    page.click_eur_button()
    page.verify_chosen_euro_currency()


def test_chose_usd_currency(browser, url):
    page = TopNavbar(browser, url)
    page.open_browser()
    page.click_chose_currency_button()
    page.click_usd_button()
    page.verify_chosen_usd_currency()


def test_chose_gbp_currency(browser, url):
    page = TopNavbar(browser, url)
    page.open_browser()
    page.click_chose_currency_button()
    page.click_gbp_button()
    page.verify_chosen_gbp_currency()
