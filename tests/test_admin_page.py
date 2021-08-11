from pages.base_page import assert_element


def test_admin_page(browser, url, credentials):
    assert_element("#header-logo", browser, 5)
    assert_element("#user-profile", browser, 5)
    assert_element(".fa-sign-out", browser, 5)
    assert_element("#navigation", browser, 5)
    assert_element("#button-setting", browser, 5)
