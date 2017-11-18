from sys import maxsize


class Contact:

    def __init__(self, name=None, last_name=None, address=None, phone=None, e_mail=None, id=None):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.e_mail = e_mail
        self.id = id

    def __repr__(self):
        #  to format output in console log
        return "%s:%s:%s" % (self.id, self.name, self.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name == other.name and self.last_name == other.last_name)