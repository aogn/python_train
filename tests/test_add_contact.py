# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from models.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contanct()
    app.create_contact(Contact(first_name="NameTest", middle_name="TT", last_name="LastTest", company_name="TestCompany", nick="NickTest", address="TestAddress", home_phone="TestPhone", email="TestEmail"))
    app.session.logout()
