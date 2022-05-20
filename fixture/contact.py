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

    def delete_first_contact(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("selected[]").click()
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        # self.accept_next_alert = True
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        # time.sleep(3)
        alert = self.app.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element_by_link_text("home").click()
        self.contact_cashe = None

    def edit_first_contact(self, contact):
        driver = self.app.driver
        self.return_to_homepage()
        self.select_first_contact()
        driver.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_contact_form(contact)
        driver.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//img[@alt='Edit']").click()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        self.app.open_home_page()
        self.select_first_contact()
        driver.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_xpath("//form[@action='edit.php']").click()
        driver.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_homepage()
        self.contact_cashe = None

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
            for element in driver.find_elements_by_xpath("//tr[position() >1]"):
                firstname = element.find_element_by_xpath(".//td[3]").text
                lastname = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cashe.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cashe)

