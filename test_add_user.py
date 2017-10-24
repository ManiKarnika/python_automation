# -*- coding: utf-8 -*-
import pytest
from user import User
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_user(app):
    app.login(username="admin", password="secret")
    app.init_users_creation(User (name="name", last_name="last_name", address="address", phone="+15031234567", e_mail="sc@sc.com"))
    app.logout()

def test_test_add_empty_user(app):
    app.login(username="admin", password="secret")
    app.init_users_creation(User (name="", last_name="", address="", phone="", e_mail=""))
    app.logout()


