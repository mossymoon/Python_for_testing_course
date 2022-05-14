from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="Ivanovich"))
    app.contact.test_edit_first_contact(Contact(firstname="New firstname"))