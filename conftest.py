import pytest
from fixture.application import Application
from fixture.application_contact import Contact_Else

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app(request):
    fixture = Contact_Else()
    request.addfinalizer(fixture.destroy)
    return fixture