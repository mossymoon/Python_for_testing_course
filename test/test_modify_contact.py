from model.contact import Contact
from random import randrange


def test_modify_contact(app, db, check_ui):
    contact = Contact(firstname="firstname", lastname="lastname")
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="test", lastname="fdfd", id=id))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = []
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)