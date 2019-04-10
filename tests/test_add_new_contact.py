# -*- coding: utf-8 -*-
from models.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.creation(Contact(first_name="NameTest", middle_name="TT", last_name="LastTest", company_name="TestCompany", nick="NickTest", address="TestAddress", home_phone="TestPhone", email="TestEmail"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
