from models.contact import Contact
#import random

def test_contact_info(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip())
    contacts_from_db = map(clean, db.get_contact_list())
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)


#def test_contact_info(app, db):
 #   contacts = app.contact.get_contact_list()
  #  contact_to_compare = random.choice(contacts)
   # id = contact_to_compare.id
    #contact_from_home_page = app.contact.get_contact_list()
    #contact_from_db = db.get_contact_list()
    #assert contact_from_home_page == contact_from_db.last_name
    #assert contact_from_home_page.first_name == contact_from_db.first_name
    #assert contact_from_home_page.id == contact_from_db.id
    #assert contact_from_home_page.address == contact_from_edit_page.address
    #assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

#def test_contact_info(app, db):
    #contacts = app.contact.get_contact_list()
    #index = randrange(len(contacts))
    #contacts_from_home_page = app.contact.get_contact_list()
    #def clean(contact):
     #   return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip())
    #contacts_from_db = map(clean, db.get_contact_list())
    #assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    #assert contacts_from_home_page.last_name == contacts_from_db.last_name
    #assert contacts_from_home_page.first_name == contacts_from_db.first_name
    #assert contacts_from_home_page.id == contacts_from_db.id
    #assert contact_from_home_page.address == contact_from_db.address
    #assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

#def clear(s):
  #  return re.sub("[() -]", "", s)

#def merge_phones_like_on_home_page(contact):
 #   return "\n".join(filter (lambda x: x != "",
  #                           map(lambda x: clear(x),
   #                              filter(lambda x: x is not None,
    #                                    [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))

#def merge_emails_like_on_home_page(contact):
#    return "\n".join(filter (lambda x: x != "",
 #                            map(lambda x: clear(x),
  #                               filter(lambda x: x is not None,
   #                                     [contact.email, contact.email2, contact.email3]))))