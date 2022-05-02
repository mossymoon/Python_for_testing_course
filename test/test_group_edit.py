def test_edit_first_group(app):
    app.session.login("admin")
    app.group.test_edit_first_group()
    app.session.logout()
