from selene.support.shared import browser
from selene import be, have


def test_first(open_browser):
    browser.element('[id="submit"]').click()
    assert browser.element("//*[text()='Thanks for submitting the form']").is_displayed() == False



def test_second(open_browser):
    # browser.config.timeout()
    browser.element('[id="firstName"]').type('selene')
    browser.element('[id="lastName"]').type('selene1')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('[id="userNumber"]').type('1234567890')
    browser.element('[id="submit"]').click()
    assert browser.element("//*[text()='Thanks for submitting the form']").is_displayed() == True


