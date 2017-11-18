# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.user.count() == 0:
        app.user.create(Contact(name="deletion_test"))
    old_contacts = app.user.get_contacts_list()
    contact = Contact(name="name_mod", last_name="last_name_mod", address="address_mod", phone="+150312", e_mail="sc_mod@sc.com")
    contact.id = old_contacts[0].id
    #  main
    app.user.modify_first_contact(contact)
    #  control
    assert len(old_contacts) == app.user.count()
    new_contacts = app.user.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_first_contact_name(app):
#     if app.user.count() == 0:
#         app.user.create(Contact(name="deletion_test"))
#     old_contacts = app.user.get_contacts_list()
#     app.user.modify_first_contact(Contact(name="name_mod"))
#     new_contacts = app.user.get_contacts_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_modify_first_contact_email(app):
#     if app.user.count() == 0:
#         app.user.create(Contact(name="deletion_test"))
#     old_contacts = app.user.get_contacts_list()
#     app.user.modify_first_contact(Contact(e_mail="sc_mod@sc.com"))
#     new_contacts = app.user.get_contacts_list()
#     assert len(old_contacts) == len(new_contacts)
