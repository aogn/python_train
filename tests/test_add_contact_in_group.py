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
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    group_id = group.id
    contacts_without_group = db.get_contacts_not_in_group(Group(id=group_id))
    contact = random.choice(contacts_without_group)
    contact_id = contact.id
    app.contact.add_contact_to_group(contact_id, group_id)
    contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    print(contacts_in_group)
    print(group_id)
    print(contact_id)

# old_contacts = db.get_contact_list()
  #  old_groups = db.get_group_list()
   # group = random.choice(old_groups)
   # app.contact.creation_with_group(Contact(first_name="test"), group.id)
   # new_contacts = db.get_contact_list()
   # old_contacts.append(contact)
  #  assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)