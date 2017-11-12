from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modification_test"))
    app.group.modify_first_group(Group(name="group_name_mod", header="group_header_mod", footer="group_footer_mod"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modification_test"))
    app.group.modify_first_group(Group(name="group_name_mod"))
