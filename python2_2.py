from selene.support.shared import browser
from selene import be, have



def test_first(open_browser):
    assert browser.element("id='react-select-4-input']").matching(be.enabled) != True

def test_second(open_browser):
    browser.element('[id="firstName"]').type('selene')
    browser.element('[id="lastName"]').type('selene1')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('[id="userNumber"]').type('1234567890').press_enter()



