import time
import re
from model.contact import Contact

class UserHelper:

    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        self.open_user_page()
        #init users creation
        self.fill_contact_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contacts_cash = None

    def open_user_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # submit first contact's deletion
        self.choose_contact_by_index(index)
        wd.find_element_by_xpath('//div/div[4]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.contacts_cash = None
        time.sleep(1)

    def modify_first_contact(self, user):
        self.modify_contact_by_index(0, user)

    def modify_contact_by_index(self, index, user):
        wd = self.app.wd
        self.app.open_home_page()
        self.choose_contact_by_index(index)
        self.go_to_contact_modification_page(index)
        self.fill_contact_form(user)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contacts_cash = None

    def fill_contact_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.homephone) #  search for home phone
        self.change_field_value("mobile", user.mobilephone)
        self.change_field_value("work", user.workphone)
        self.change_field_value("fax", user.secondaryphone)
        self.change_field_value("email", user.e_mail)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def go_to_contact_modification_page(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def choose_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()  # home & contacts' page are the same one
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cash = None

    def get_contacts_list(self):
        if self.contacts_cash is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cash = []
            for element in wd.find_elements_by_name('entry'):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_xpath(".//td")
                name = cells[2].text
                last_name = cells[1].text
                all_phones = cells[5].text
                self.contacts_cash.append(Contact(firstname=name, lastname=last_name, id=id,
                                                  all_phones_from_home_page=all_phones))
        return self.contacts_cash

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.choose_contact_by_index(index)
        self.go_to_contact_modification_page(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("fax").get_attribute("value")
        # return object
        return Contact(firstname=firstname, lastname=lastname, homephone=homephone, mobilephone=mobilephone,
                 workphone=workphone, secondaryphone=secondaryphone, id=id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd

        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("F: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

