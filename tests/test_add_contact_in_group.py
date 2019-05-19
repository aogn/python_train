from models.contact import Contact
from models.group import Group
from fixture.orm import ORMFixture
import random
import allure

def test_add_contact_in_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    with allure.step('Check group and contact'):
        if len(db.get_group_list()) == 0:
            app.group.creation(Group(name="test"))
        if len(db.get_contact_list()) == 0:
            app.contact.creation(Contact(first_name="test"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a group, contact not in group and contact in group'):
        group = random.choice(old_groups)
        group_id = group.id
        contacts_without_group = db.get_contacts_not_in_group(Group(id=group_id))
        contact = random.choice(contacts_without_group)
        contact_id = contact.id
        old_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    with allure.step('When I add a contact %s to the group %s' % (contact, group)):
        app.contact.add_contact_to_group(contact_id, group_id)
    with allure.step('Then the new contacts in group list is equal to the old contacts in group list with the added contact'):
        new_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
        old_contacts_in_group.append(contact)
        assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(old_contacts_in_group, key=Contact.id_or_max)
