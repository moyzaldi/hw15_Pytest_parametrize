from selene import browser, by, be


def test_button_sign_in_desktop(skip_if_mobile):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)


def test_button_sign_in_mobile(skip_if_desktop):
    browser.open('https://github.com/')
    browser.element(by.text("Sign in")).should(be.visible)
    browser.element(by.text("Sign in")).click()
    browser.element('.auth-form-header').should(be.visible)
