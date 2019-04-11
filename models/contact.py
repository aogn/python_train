class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, company_name=None, nick=None, address=None, home_phone=None, email=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.company_name = company_name
        self.nick = nick
        self.address = address
        self.home_phone = home_phone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name
