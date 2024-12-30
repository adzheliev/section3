import time

def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element("xpath", '//button[@type="submit"]')
    assert button.is_displayed(), "Button 'Add to basket' not found on the page"
