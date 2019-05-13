from models.contact import Contact
from random import randrange
import re

def test_contact_info(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_db) == len(contacts_from_home_page)
    l = len(contacts_from_home_page)
    for i in range(l):
        index = i
        contact_homepage = contacts_from_home_page[index]
        contact_db = contacts_from_db[index]
        assert contact_homepage.first_name == contact_db.first_name
        assert contact_homepage.last_name == contact_db.last_name
        assert contact_homepage.id == contact_db.id
        assert contact_homepage.address == contact_db.address
        assert contact_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)
    print(contact_db)
    print(contact_homepage)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))


