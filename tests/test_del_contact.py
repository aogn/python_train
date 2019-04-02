from models.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(first_name="test"))
    app.contact.delete_first_contact()
