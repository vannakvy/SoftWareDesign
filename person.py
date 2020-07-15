from address import Address
from typing import List
from aifc import Error


class Person:
    def __init__(self, first, last, dob, phone, address):
        self.first_name = first
        self.last_name = last
        self.phone = phone
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, List):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Error("Invalid Address...")

            self.addresses = address
        else:
            raise Error("Invalid Address..")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise Error("Invalid Address...")

        self.addresses.append(address)
