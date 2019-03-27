from models.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="UpdateName", middle_name="Updatemiddle", last_name="UpdateLastTest", company_name="UpdateTestCompany", nick="UpdateNickTest", address="UpdateAddress", home_phone="UpdatePhone", email="UpdateEmail"))
    app.session.logout()