from models.contact import Contact
from random import randrange

def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.creation(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="NameTest", middle_name="TT", last_name="LastTest")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)



