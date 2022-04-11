import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_basket_button_on_page(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements_by_css_selector(
        'button.btn'), 'Button Not Found'
