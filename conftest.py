import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseURL")
    if fixture is None: #  to create first fixture
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():  # to check fixture's validity
            fixture = Application(browser=browser, base_url=base_url) # if not, to create new one
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope='session', autouse=True) # only one time in the session's end, case of scope
def stop(request):                             # autouse for that procedure
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/index.php")