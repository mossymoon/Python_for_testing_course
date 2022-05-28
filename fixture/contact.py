import time

from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def new_contact(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def create_new_contact(self, new_contact_data):
        driver = self.app.driver
        self.app.open_home_page()
        self.new_contact()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        # self.accept_next_alert = True
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        # time.sleep(3)
        alert = self.app.driver.switch_to.alert
        alert.accept()
        # time.sleep(2)
        driver.find_element_by_link_text("home").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def select_modify_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_modify_by_index(index)
        driver.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_xpath("//form[@action='edit.php']").click()
        driver.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    def return_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[6].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        nickname = driver.find_element_by_name("nickname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        company = driver.find_element_by_name("company").get_attribute("value")
        title = driver.find_element_by_name("title").get_attribute("value")
        address = driver.find_element_by_name("address").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        fax = driver.find_element_by_name("fax").get_attribute("value")
        e_mail = driver.find_element_by_name("email").get_attribute("value")
        e_mail2 = driver.find_element_by_name("email2").get_attribute("value")
        e_mail3 = driver.find_element_by_name("email3").get_attribute("value")
        homepage = driver.find_element_by_name("homepage").get_attribute("value")
        secondaryaddress = driver.find_element_by_name("address2").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        notes = driver.find_element_by_name("notes").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, nickname=nickname, address=address, id=id,
                       company=company, title=title, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       fax=fax, e_mail=e_mail, e_mail2=e_mail2, e_mail3=e_mail3, homepage=homepage,
                       secondaryaddress=secondaryaddress, secondaryphone=secondaryphone, notes=notes)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)
