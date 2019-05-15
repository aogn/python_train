from models.contact import Contact
from models.group import Group
from fixture.orm import ORMFixture
import random

def test_delete_contact_from_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_group_list()) == 0:
        app.group.creation(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.creation(Contact(first_name="test"))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    group_id = group.id
    if len(db.get_contacts_in_group(Group(id=group_id))) == 0:
        contact = random.choice(old_contacts)
        contact_id = contact.id
        app.contact.add_contact_to_group(contact_id, group_id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    contact_to_delete = random.choice(old_contacts_in_group)
    contact_to_delete_id = contact_to_delete.id
    app.contact.delete_contact_from_group(contact_to_delete_id, group_id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    old_contacts_in_group.remove(contact_to_delete)
    assert new_contacts_in_group == old_contacts_in_group