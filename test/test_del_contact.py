from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="deletion_contact_test"))
    old_contacts = app.user.get_contacts_list()
    index = randrange(len(old_contacts))
    app.user.delete_contact_by_index(index)
    #  control
    assert len(old_contacts) - 1 == app.user.count()
    new_contacts = app.user.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
