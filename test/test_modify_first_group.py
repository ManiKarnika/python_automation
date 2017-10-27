from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group_name_mod", header="group_header_mod", footer="group_footer_mod"))
    app.session.logout()