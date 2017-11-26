# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.user.get_contacts_list()
    contact = Contact(firstname="name", lastname="last_name", address="address", homephone="+15031234567", mobilephone="+17866876876", workphone="+159875757865", secondaryphone="+12546576578", e_mail="sc@sc.com")
    app.user.create(contact)
    assert len(old_contacts) + 1 == app.user.count()
    new_contacts = app.user.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.user.get_contacts_list()
#     contact = Contact(name="", last_name="", address="", phone="", e_mail="")
#     app.user.create(contact)
#     new_contacts = app.user.get_contacts_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)