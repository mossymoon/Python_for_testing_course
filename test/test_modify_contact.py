from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivanov3", lastname="Ivanov3")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # if app.contact.count() == 0:
    #     app.contact.create_new_contact(Contact(firstname="test"))
    # app.contact.modify_first_contact(Contact(firstname="New firstname"))