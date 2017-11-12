import time

class UserHelper:

    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        self.open_user_page()
        #init users creation
        self.fill_contact_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
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
        self.fill_contact_form(user)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

    def fill_contact_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.name)
        self.change_field_value("lastname", user.last_name)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.phone) #  search for home phone
        self.change_field_value("email", user.e_mail)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def go_to_contact_modification_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def choose_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()  # home & contacts' page are the same one
        return len(wd.find_elements_by_name("selected[]"))

