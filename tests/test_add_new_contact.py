# -*- coding: utf-8 -*-
from models.contact import Contact

def test_add_contact(app):
    app.contact.creation(Contact(first_name="NameTest", middle_name="TT", last_name="LastTest", company_name="TestCompany", nick="NickTest", address="TestAddress", home_phone="TestPhone", email="TestEmail"))
