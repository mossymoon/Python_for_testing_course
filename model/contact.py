from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, title=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, e_mail=None,
                 e_mail2=None, e_mail3=None, homepage=None, secondaryaddress=None, secondaryphone=None,
                 notes=None, all_phones_from_home_page=None, all_emails_from_home_page=None, id=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.title = title
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.e_mail = e_mail
        self.e_mail2 = e_mail2
        self.e_mail3 = e_mail3
        self.homepage = homepage
        self.secondaryaddress = secondaryaddress
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s%s%s%s%s%s%s%s%s%s" % (self.id, self.firstname, self.lastname, self.address, self.homephone,
                                         self.mobilephone, self.workphone, self.e_mail, self.e_mail2,
                                         self.e_mail3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
