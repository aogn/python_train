from models.contact import Contact
from models.group import Group
from fixture.orm import ORMFixture
import random
import allure

def test_delete_contact_from_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    with allure.step('Check group and contact'):
        if len(db.get_group_list()) == 0:
            app.group.creation(Group(name="test"))
        if len(db.get_contact_list()) == 0:
            app.contact.creation(Contact(first_name="test"))
    with allure.step('Given a group list, contact list and random group'):
        old_groups = db.get_group_list()
        old_contacts = db.get_contact_list()
        group = random.choice(old_groups)
        group_id = group.id
    with allure.step('Check contact in group %s' % group):
        if len(db.get_contacts_in_group(Group(id=group_id))) == 0:
            contact = random.choice(old_contacts)
            contact_id = contact.id
            app.contact.add_contact_to_group(contact_id, group_id)
    with allure.step('Given a old contacts in group list and random contact to delete'):
        old_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
        contact_to_delete = random.choice(old_contacts_in_group)
        contact_to_delete_id = contact_to_delete.id
    with allure.step('When I remove a contact %s from the group %s' % (contact_to_delete, group)):
        app.contact.delete_contact_from_group(contact_to_delete_id, group_id)
    with allure.step('Then the new contacts in group list is equal to the old contacts in group list withouth the deleted contact'):
        new_contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
        old_contacts_in_group.remove(contact_to_delete)
        assert new_contacts_in_group == old_contacts_in_group