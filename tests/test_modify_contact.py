from models.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="NameTest", middle_name="TT", last_name="LastTest")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


