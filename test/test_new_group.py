from model.group import Group

def test_add_group(app):
    app.session.login("admin")
    app.group.create(Group(name="test23", header="test23", footer="test23"))
    app.session.logout()

def test_empty_group(app):
    app.session.login("admin")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
