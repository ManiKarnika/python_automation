# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User (name="name", last_name="last_name", address="address", phone="+15031234567", e_mail="sc@sc.com"))
    app.session.logout()

def test_test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.user.create(User (name="", last_name="", address="", phone="", e_mail=""))
    app.session.logout()


