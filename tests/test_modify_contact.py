from models.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(first_name="test"))
    app.contact.creation(Contact(first_name="NameTest", middle_name="TT", last_name="LastTest"))

