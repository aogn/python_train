from models.contact import Contact
from random import randrange
import allure

def test_modify_contact_name(app, db, check_ui):
    with allure.step('Check contact'):
        if len(db.get_contact_list()) == 0:
            app.contact.creation(Contact(first_name="test"))
    with allure.step('Given a contact list and contact to modify'):
        old_contacts = db.get_contact_list()
        index = randrange(len(old_contacts))
        contact = Contact(first_name="NameTest", middle_name="TT", last_name="LastTest")
        contact.id = old_contacts[index].id
    with allure.step('When I change a contact info to %s' % contact):
        app.contact.modify_contact_by_id(contact, contact.id)
    with allure.step('Then the new contact list is equal to the old list with new contact info'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[index] = contact
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)



