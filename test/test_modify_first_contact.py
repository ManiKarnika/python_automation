# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.user.modify_first_contact(Contact (name="name_mod", last_name="last_name_mod", address="address_mod", phone="+150312", e_mail="sc_mod@sc.com"))

def test_modify_first_contact_name(app):
    app.user.modify_first_contact(Contact (name="name_mod"))

def test_modify_first_contact_email(app):
    app.user.modify_first_contact(Contact (e_mail="sc_mod@sc.com"))
