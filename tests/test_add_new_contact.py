# -*- coding: utf-8 -*-
from models.contact import Contact

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.creation(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
