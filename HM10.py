from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def search_records(self, **kwargs):
        results = []
        for record in self.data.values():
            if all(
                getattr(record, field).value == value for field, value in kwargs.items()
            ):
                results.append(record)
        return results


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass
