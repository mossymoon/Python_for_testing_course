def test_edit_first_contact(app):
    app.session.login("admin")
    app.contact.test_edit_first_contact()
    app.session.logout()