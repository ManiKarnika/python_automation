# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.user.create(Contact (name="name", last_name="last_name", address="address", phone="+15031234567", e_mail="sc@sc.com"))

def test_add_empty_contact(app):
    app.user.create(Contact (name="", last_name="", address="", phone="", e_mail=""))

