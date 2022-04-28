# Задание №5 двухуровневая архитектура теста

from model.contact import Contact

def test_case_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    # app.new_contact()
    app.contact.create_new_contact(Contact(firstname="Ivan", lastname="Ivanov", address="Moscow", mobile=3232323))
    # app.return_to_homepage()
    app.session.logout()

def test_empty_case_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_new_contact(Contact(firstname="", lastname="", address="", mobile=""))
    app.session.logout()

def tearDown(self):
    self.app.destroy()

