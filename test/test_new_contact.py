from model.contact import Contact


def test_case_contact(app):
    old_contacts = app.contact.get_contact_list()[0]
    contact = Contact(firstname="Ivan2", lastname="Ivanov3", address="Moscow4", home=123456, mobile=123456,
                      work=123456, phone2=123456)
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_empty_case_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", lastname="", address="", mobile="")
#     app.contact.create_new_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)