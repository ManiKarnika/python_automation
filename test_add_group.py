# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.init_groups_creation(Group (name="group_name", header="group_header", footer="group_footer"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.init_groups_creation(Group (name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
