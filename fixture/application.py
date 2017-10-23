from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:


    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        self.session = SessionHelper(self)

    def init_groups_creation(self, group):
        wd = self.wd
        self.open_home_page()
        # init group creation
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

