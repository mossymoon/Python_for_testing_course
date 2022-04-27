# тест из задания №1 (1 урок): с добавленными методами и классами

import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login("admin")
    app.group.create(Group(name="test", header="test", footer="test"))
    app.session.logout()

def test_empty_group(app):
    app.session.login("admin")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
