import pytest
from selene import browser



@pytest.fixture(scope='function', autouse=True)
def browser_setting():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 750
    browser.config.window_height = 1080

    yield

    browser.quit()
