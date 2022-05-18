from model.contact import Contact

def test_case_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan2", lastname="Ivanov3", address="Moscow4", mobile=3232323)
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_empty_case_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", address="", mobile="")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)