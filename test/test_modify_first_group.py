from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="group_name_mod", header="group_header_mod", footer="group_footer_mod"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="group_name_mod"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="group_header_mod"))
