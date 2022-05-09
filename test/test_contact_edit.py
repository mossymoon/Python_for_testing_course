from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.test_edit_first_contact(Contact(lastname="Ivanov3"))