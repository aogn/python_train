from models.contact import Contact
import random

def test_modify_contact_name(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.creation(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    contact_to_change = random.choice(old_contacts)
    contact = Contact(first_name="NameTest", middle_name="TT", last_name="LastTest")
    id = contact_to_change.id
    app.contact.modify_contact_by_id(contact, id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


