from models.contact import Contact
from models.group import Group
from fixture.orm import ORMFixture
import random

def test_add_contact_in_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_group_list()) == 0:
        app.group.creation(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.creation(Contact(first_name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_id = group.id
    contacts_without_group = db.get_contacts_not_in_group(Group(id=group_id))
    contact = random.choice(contacts_without_group)
    contact_id = contact.id
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    app.contact.add_contact_to_group(contact_id, group_id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    old_contacts_in_group.append(contact)
    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(old_contacts_in_group, key=Contact.id_or_max)
