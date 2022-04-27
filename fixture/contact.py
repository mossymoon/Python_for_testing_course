class ContactHelper:

    def __init__(self, app):
        self.app = app

    def new_contact(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def create_new_contact(self, contact):
        driver = self.app.driver
        self.app.new_contact()
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

    def return_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()
