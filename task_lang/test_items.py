def test_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert bool(browser.find_element_by_css_selector('.btn-add-to-basket'))
