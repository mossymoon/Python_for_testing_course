# Задание №4 создание фикстуры с вынесением отдельного класса
import pytest
from model.contact import Contact
from fixture.application_contact import Contact_Else

@pytest.fixture()
def app(request):
    fixture = Contact_Else()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_case_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    # app.new_contact()
    app.create_new_contact(Contact(firstname="Ivan", lastname="Ivanov", address="Moscow", mobile=3232323))
    # app.return_to_homepage()
    app.session.logout()

def test_empty_case_contact(app):
    app.session.login("admin", "secret")
    app.create_new_contact(Contact(firstname="", lastname="", address="", mobile=""))
    app.session.logout()

def tearDown(self):
    self.app.destroy()

