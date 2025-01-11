from selene import browser, by, be
import pytest


def test_button_sign_in_desktop(setup_browser):
    if setup_browser == 'mobile':
        pytest.skip('Skipping test for desktop version')

    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)


def test_button_sign_in_mobile(setup_browser):
    if setup_browser == 'desktop':
        pytest.skip('Skipping test for mobile version')

    browser.open('https://github.com/')
    browser.element(by.text("Sign in")).should(be.visible)
    browser.element(by.text("Sign in")).click()
    browser.element('.auth-form-header').should(be.visible)
