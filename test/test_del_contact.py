

def test_delete_first_contact(app):
    app.session.login("admin")
    app.contact.delete_first_contact()
    app.session.logout()