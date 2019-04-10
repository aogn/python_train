from models.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="NameTest", middle_name="TT", last_name="LastTest"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

