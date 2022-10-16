import addressbook
from addressbook import AddressBook, Contact


def test_add_contact():
    adderssbook = AddressBook("person1")
    contact_dict = {"sl_no": "1", "first_name": "shree", "last_name": "gowri", "address": "nagara",
                    "phone_number": "0123456789", "email": "abc@gmai.com"}
    contact = Contact(**contact_dict)
    assert len(adderssbook) == 0
    adderssbook.add_contact(contact)
    assert len(adderssbook) == 1


def test_delete_contact():
    adderssbook = AddressBook("person1")
    contact_dict = {"sl_no": "1", "first_name": "shree", "last_name": "gowri", "address": "nagara",
                    "phone_number": "0123456789", "email": "abc@gmai.com"}
    contact = Contact(**contact_dict)
    adderssbook.delete_contact(contact.first_name)
    assert len(adderssbook) == 0


def test_update_contact():
    contact = Contact("1", "sri", "gagana", "rrnagara", "0123456789", "abc@gmai.com")
    addressbook.update_contact()
    assert contact.sl_no == "1"
    assert contact.first_name == "sri"
    assert contact.last_name == "gagana"
    assert contact.address == "rrnagara"
    assert contact.phone_number == "0123456789"
    assert contact.email == "abc@gmai.com"
