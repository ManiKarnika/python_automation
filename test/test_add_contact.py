# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "e" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen / 2))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen / 2))]) + ".com"

testdata = [
    Contact(firstname=name, lastname=lastname, address=random_string("", 20), homephone=random_number(10), mobilephone=random_number(10), workphone=random_number(10), secondaryphone=random_number(10), e_mail=random_email(8))
    for name in ["", random_string("name", 7)]
    for lastname in [random_string("last", 10)]*3
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(y) for y in testdata])
def test_add_contact(app, contact):
    old_contacts = app.user.get_contacts_list()
    app.user.create(contact)
    assert len(old_contacts) + 1 == app.user.count()
    new_contacts = app.user.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


