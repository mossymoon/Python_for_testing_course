import time

from model.contact import Contact


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
        self.contact_cashe = None

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
        self.contact_cashe = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("homephone", contact.homephone)
        self.change_field_value("workphone", contact.workphone)
        self.change_field_value("secondaryphone", contact.secondaryphone)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

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
        self.contact_cashe = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    def return_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cashe = []
            for row in driver.find_elements_by_xpath("//tr[position() >1]"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_name("input").get_attribute("value")
                all_phones = cells[5].splitlines()
                self.contact_cashe.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobile=all_phones[1],
                                                workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cashe)

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.select_contact_by_index(index)
        firstname = driver.find_elements_by_name("firstname").get_atribute("value")
        lastname = driver.find_elements_by_name("lastname").get_atribute("value")
        id = driver.find_elements_by_name("id").get_atribute("value")
        homephone = driver.find_elements_by_name("home").get_atribute("value")
        workphone = driver.find_elements_by_name("work").get_atribute("value")
        mobile = driver.find_elements_by_name("mobile").get_atribute("value")
        secondaryphone = driver.find_elements_by_name("phone2").get_atribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobile=mobile,
                       secondaryphone=secondaryphone)

