
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def filling_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def creation(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.filling_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        # fill form
        self.filling_form(new_contact_data)
        # submit
        wd.find_element_by_name("update").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # edit contact
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.filling_form(contact)
        # submit edition
        wd.find_element_by_name("update").click()