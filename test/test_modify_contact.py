from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))