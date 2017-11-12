from model.contact import Contact


def test_delete_first_contact(app):
    if app.user.count() == 0:
        app.user.create(Contact(name="deletion_contact_test"))
    app.user.delete_first_contact()
