from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group_name_mod", header="group_header_mod", footer="group_footer_mod"))
    app.session.logout()


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group_name_mod"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="group_header_mod"))
    app.session.logout()