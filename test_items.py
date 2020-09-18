import time
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_add_to_cart_button(browser):
    browser.get(LINK)
    time.sleep(5)
    add_to_cart_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(add_to_cart_button), f"No add to cart button on: {LINK}"
