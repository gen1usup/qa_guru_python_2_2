import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def open_browser():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # options.add_argument('--ignore-certificate-errors-spki-list')
    # browser.config.driver = webdriver.Chrome("E:\drivers\chromedriver_win32\chromedriver.exe", chrome_options=options)
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.close_current_tab()