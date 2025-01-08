import pytest
from selene import browser


# Для test_authorization_different_fix.py
# Для test_authorization_indirect2.py
@pytest.fixture(params=[(2560, 1440), (1920, 1080)])
def size_browser_window_desktop(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com/'

    yield
    browser.quit()


# Для test_authorization_different_fix.py
# Для test_authorization_indirect2.py
@pytest.fixture(params=[(640, 360)])
def size_browser_window_mobile(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com/'

    yield
    browser.quit()


# Для test_authorization_indirect.py
@pytest.fixture(params=['mobile', 'desktop'])
def size_browser_window_indirect(request):
    if request.param == 'mobile':
        browser.config.window_height = 360
        browser.config.window_width = 640

    if request.param == 'desktop':
        browser.config.window_height = 1080
        browser.config.window_width = 1920

    browser.config.base_url = 'https://github.com/'

    yield
    browser.quit()


# Для test_skip.py
@pytest.fixture(params=[(2560, 1440), (1920, 1080), (640, 360)])
def skip_if_mobile(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com/'
    if width < 1011:
        pytest.skip('Skipping test for mobile version')

    yield
    browser.quit()


# Для test_skip.py
@pytest.fixture(params=[(2560, 1440), (1920, 1080), (640, 360)])
def skip_if_desktop(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com/'
    if width >= 1011:
        pytest.skip('Skipping test for mobile version')

    yield
    browser.quit()
