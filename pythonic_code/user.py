class User(object):

    def __init__(self, firstname=None, lastname=None, username=None):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username

    @classmethod
    def add(cls, user_info):
        firstname, lastname, username = user_info
        print('Calling subprocess to create', username)
        new_user = cls(firstname, lastname, username)
        return new_user

    @staticmethod
    def parse_strings(username):
        cleaned_username = username.lower()
        return cleaned_username

