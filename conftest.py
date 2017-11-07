import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None: #  to create first fixture
        fixture = Application()
    else:
        if not fixture.is_valid():  # to check fixture's validity
            fixture = Application() # if not, to create new one
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope='session', autouse=True) # only one time in the session's end, case of scope
def stop(request):                             # autouse for that procedure
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture