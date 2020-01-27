import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_on_button_basket(browser):
    browser.get(link)
    time.sleep(10)
    button_basket = browser.find_element_by_class_name('btn-add-to-basket')
    assert button_basket, 'No button in page'
