from model.contact import Contact

def test_case_contact(app):
    app.open_home_page()
    app.contact.create_new_contact(Contact(firstname="Ivan2", lastname="Ivanov3", address="Moscow4", mobile=3232323))

def test_empty_case_contact(app):
    app.contact.create_new_contact(Contact(firstname="", lastname="", address="", mobile=""))