# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="modification_test"))
    old_contacts = app.user.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="name_mod", lastname="last_name_mod", address="address_mod",
                      homephone="+150312", e_mail="sc_mod@sc.com")
    contact.id = old_contacts[index].id
    #  main
    app.user.modify_contact_by_index(index, contact)
    #  control
    assert len(old_contacts) == app.user.count()
    new_contacts = app.user.get_contacts_list()
    old_contacts[index] = contact
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
