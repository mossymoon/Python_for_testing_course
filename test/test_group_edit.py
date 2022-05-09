from model.group import Group

def test_edit_first_group(app):
    app.group.test_edit_first_group(Group(name="Ivanov3"))