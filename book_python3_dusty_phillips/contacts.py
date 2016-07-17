class ContactList(list):
    def search(self, name):
        matched = []
        for contact in self:
            if name in contact.firstname:
                matched.append(contact)
        return matched


class Contact(object):
    all_contacts = ContactList()

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@fs.co.jp'
        Contact.all_contacts.append(self)


class MailSender(object):
        def send_mail(self, subject, recipient):
                    print('Sent message {} to {}'.format(subject, recipient))


class Friend(Contact, MailSender):
    def __init__(self, firstname, lastname, phone):
        super().__init__(firstname, lastname)
        self.phone = phone
    def get_info(self):
        print(self.firstname, self.lastname, self.email)

