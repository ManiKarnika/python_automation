from model.contact import Contact


def test_delete_first_contact(app):
    if app.user.count() == 0:
        app.user.create(Contact(name="deletion_contact_test"))
    old_contacts = app.user.get_contacts_list()
    app.user.delete_first_contact()
    #  control
    new_contacts = app.user.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
