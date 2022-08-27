import logging

logging.basicConfig(filename='address_book.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Contact:
    def __init__(self, sl_no, first_name, last_name, address, phone_number, email):
        self.sl_no = sl_no
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    @property
    def full_name(self):
        """
        Function to get the full name
        """
        try:
            return self.first_name + "" + self.last_name
        except Exception as e:
            logging.error(e)
            return " "

    def as_string(self):
        """
        Function to get the all values in the form of list
        """

        return "{:<10} {:<10} {:<10} {:<10} {:<10}  ".format(self.sl_no, self.full_name,
                                                             self.address, self.phone_number, self.email)


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contact_dict = {}

    def add_contact(self, person):
        """
        Function to add the contact person
        """
        try:
            self.contact_dict.update({person.first_name: person})
        except Exception as e:
            logging.error(e)

    def get_contact(self, name):
        """
        Function to get the contact
        """
        try:
            return self.contact_dict.get(name)
        except Exception as e:
            logging.error(e)

    # def update_contact(self, sl_no, first_name, last_name, address, phone_number, email):
    #     """
    #     Function to update the contact
    #     """
    #     try:
    #         person_name = input("Enter person name you want to update: ")
    #         contact_exist = self.contact_dict.get(person_name)
    #         if not contact_exist:
    #             print("name not present")
    #             return
    #         contact_exist.sl_no = sl_no
    #         contact_exist.first_name = first_name
    #         contact_exist.last_name = last_name
    #         contact_exist.address = address
    #         contact_exist.phone_number = phone_number
    #         contact_exist.email = email
    #         print("updated successfully")
    #     except Exception as e:
    #         logging.error(e)

    def display_contact(self):
        """
        Function to display the contact
        """
        try:
            print(
                "{:<10} {:<10} {:<10} {:<10} {:<10} ".format('sl_no', 'full_name', 'address', 'phone_number', 'email'))
            for i in self.contact_dict:
                contact_obj = self.contact_dict.get(i)
                print(contact_obj.as_string())
        except Exception as e:
            logging.error(e)

    def delete_contact(self, name_):
        """
        Function to delete the contact
        """
        try:
            if not self.get_contact(name_):
                print("name doesn't exist")
                return

            self.contact_dict.pop(name_)
        except Exception as e:
            logging.error(e)


def add_addressbook():
    """
    Function add addressbook to addressbook dictionary
    """
    try:
        address_book = input("Enter addressbook name : ")
        addressbook_obj = AddressBook(address_book)
        address_dict.update({addressbook_obj.name: addressbook_obj})
        return address_dict
    except Exception as e:
        logging.error(e)


def display_addressbook():
    """
    Function to display address book
    """
    try:
        print(address_dict)
    except Exception as e:
        logging.error(e)


def add_contact_with_addressbook():
    """
    Function to add contact with the person details
    """
    try:
        addressbook_name = input("Enter addressbook name : ")
        contact_exist = address_dict.get(addressbook_name)
        if contact_exist is None:
            contact_exist = AddressBook(addressbook_name)
            address_dict.update({contact_exist.name: contact_exist})
            print("address book does not exist")
            return

        sl_no = input("Enter sl_no : ")
        first_name = input("Enter first name : ")
        last_name = input("Enter last name : ")
        address = input("Enter address : ")
        phone_number = input("Enter phone_number : ")
        email = input("Enter email : ")
        contact = Contact(sl_no, first_name, last_name, address, phone_number, email)
        contact_exist.add_contact(contact)
    except Exception as e:
        logging.error(e)


def update_contact():
    try:
        addressbook_name = input("Enter addressbook name name : ")
        addressbook_exist = address_dict.get(addressbook_name)
        if addressbook_exist is None:
            print("address book doesn,t exist")
            return
            # contact_exist = AddressBook(addressbook_name)
            # address_dict.update({contact_exist.name: contact_exist})
        first_name = input("Enter first name : ")
        contact = addressbook_exist.get_contact(first_name)
        if not contact:
            print("contact not exist")
            return
        sl_no = input("Enter sl_no : ")

        last_name = input("Enter last name : ")
        address = input("Enter address : ")
        phone_number = input("Enter phone_number : ")
        email = input("Enter email : ")
        contact = Contact(sl_no=sl_no, first_name=first_name, last_name=last_name, address=address,
                          phone_number=phone_number, email=email)
        addressbook_exist.add_contact(contact)
    except Exception as e:
        print(e)


def get_contact():
    try:
        addressbook_name = input("Enter addressbook name name : ")
        addressbook = address_dict.get(addressbook_name)
        if addressbook is None:
            print("addressbook doesnot exist")
            return
        first_name = input("Enter first name : ")
        contact = addressbook.get_contact(first_name)
        if contact is None:
            print("conact doesnot exist")
            return
        print(contact.as_string())


    except Exception as e:
        print(e)


def delete_contact_with_addressbook():
    try:
        addressbook_name = input("Enter addressbook name name : ")
        contact_exist = address_dict.get(addressbook_name)
        if contact_exist is None:
            return "contact doesn't exit "
        first_name = input("Enter first name : ")
        contact_exist.delete_contact(first_name)
    except Exception as e:
        logging.error(e)


def display_contact_with_addressbook():
    try:
        addressbook_name = input("Enter addressbook name name : ")
        contact_exist = address_dict.get(addressbook_name)
        if contact_exist is None:
            return "contact doesn't exit "
        contact_exist.display_contact()
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    try:
        address_dict = {}
        while True:
            print("1.add_addressbook\n2.Display addressbook\n3.Add contact \n4.Delete "
                  "contact\n5.display_contact\n6.update_contact\n0.Exit")
            dict_e = {1: add_addressbook,
                      2: display_addressbook,
                      3: add_contact_with_addressbook,
                      4: delete_contact_with_addressbook,
                      5: display_contact_with_addressbook,
                      6: update_contact}

            choice = int(input("Enter a number : "))
            if choice == 0:
                break
            dict_e.get(choice)()
            input("Press enter to continue ")
            print("--------------------- Choose Option ----------------------")

    except Exception as e:
        print(e)
