from models.contact import Contact

def test_modify_contact_name(app):
    app.contact.creation(Contact(first_name="NameTest", middle_name="TT", last_name="LastTest"))

