from model.group import Group


# def test_modify_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="modification_test"))
#     old_groups = app.group.get_group_list()
#
#     app.group.modify_first_group(Group(name="group_name_mod", header="group_header_mod", footer="group_footer_mod"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups)  == len(new_groups)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modification_test"))
    old_groups = app.group.get_group_list()
    group = Group(name="group_name_mod")
    group.id = old_groups[0].id
    #  main
    app.group.modify_first_group(group)
    #  control
    assert len(old_groups)  == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
