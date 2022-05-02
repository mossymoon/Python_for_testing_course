import time
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def new_contact(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def create_new_contact(self, contact):
        driver = self.app.driver
        self.new_contact()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # self.app.return_to_homepage()

    def delete_first_group(self):
        driver = self.app.driver
        self.app.open_groups_page()
        # select first group
        driver.find_element_by_name("selected[]").click()
        # submit deletion
        driver.find_element_by_name("delete").click()
        driver.find_element_by_link_text("group page").click()

    def delete_first_contact(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("selected[]").click()
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.accept_next_alert = True
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        time.sleep(3)
        alert = self.app.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element_by_link_text("home").click()

    def test_edit_first_contact(self):
        driver = self.app.driver
        self.app.open_home_page()
        # driver.find_element_by_link_text("home").click()
        driver.find_element_by_xpath("//img[@alt='Edit']").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("rdfd")
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("fdfdf")
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("fdfdf")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("fdfdf")
        driver.find_element_by_xpath("//form[@action='edit.php']").click()
        driver.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        # driver.find_element_by_link_text("home page").click()
        # driver.find_element_by_link_text("Logout").click()
        # driver.find_element_by_name("user").clear()
        # driver.find_element_by_name("user").send_keys("admin")

    def return_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

