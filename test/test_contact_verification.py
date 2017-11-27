from random import randrange
import re


def test_contact_full_name_verification(app):
    contacts = app.user.get_contacts_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.user.get_contacts_list()[index]
    contact_from_edit_page = app.user.get_contact_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert format_address(contact_from_home_page.address) == format_address(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def format_address(s):
    return re.sub("\n", "", s)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.e_mail, contact.e_mail2, contact.e_mail3]))))