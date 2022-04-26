# Задание №3 создание методов и классов - для контактов
from selenium import webdriver
import unittest
from contact import Contact

class TestCaseContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_case_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login("admin", driver, "secret")
        self.new_contact(driver)
        self.create_new_contact(driver, Contact(firstname="Ivan", lastname="Ivanov", address="Moscow", mobile=3232323))
        self.return_to_homepage(driver)
        self.logout(driver)

    def test_empty_case_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login("admin", driver, "secret")
        self.new_contact(driver)
        self.create_new_contact(driver, Contact(firstname="", lastname="", address="", mobile=""))
        self.return_to_homepage(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, driver):
        driver.find_element_by_link_text("home").click()

    def create_new_contact(self, driver, contact):
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
        # submit new contact
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def new_contact(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, username, driver, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        # open hame page
        driver.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
