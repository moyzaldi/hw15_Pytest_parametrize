import pytest
from selene import browser, by, be


@pytest.mark.parametrize('size_browser_window_indirect', ['mobile'], indirect=True)
def test_button_sign_in_mobile(size_browser_window_indirect):
    browser.open('https://github.com/')
    browser.element(by.text("Sign in")).should(be.visible)
    browser.element(by.text("Sign in")).click()
    browser.element('.auth-form-header').should(be.visible)


@pytest.mark.parametrize('size_browser_window_indirect', ['desktop'], indirect=True)
def test_button_sign_in_desktop(size_browser_window_indirect):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)
