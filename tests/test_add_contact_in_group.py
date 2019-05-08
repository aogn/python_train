from models.contact import Contact
from models.group import Group
import random

def add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.creation(Group(name="test"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.contact.creation_with_group(Contact(first_name="test"), group.id)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)