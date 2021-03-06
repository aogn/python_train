from sys import maxsize

class Contact:

    id: object

    def __init__(self, first_name=None, middle_name=None, last_name=None, company_name=None,
                 nick=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 fax_phone=None, email=None, email2=None, email3=None, secondary_phone=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.company_name = company_name
        self.nick = nick
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s;%s;%s" % (self.id, self.first_name, self.last_name, self.middle_name, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
