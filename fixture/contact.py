import time

class UserHelper:

    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        self.open_user_page()
        #init users creation
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.e_mail)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # submit first contact's deletion
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//div/div[4]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        time.sleep(1)

    def modify_first_contact(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        self.choose_contact()
        self.go_to_contact_modification_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.e_mail)
        wd.find_element_by_name("update").click()
        time.sleep(5) # to wait for refresh  page

    def go_to_contact_modification_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def choose_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

