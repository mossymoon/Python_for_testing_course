# тест из задания №1 (1 урок)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group

class UntitledTestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login("admin", driver)
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="test", header="test", footer="test"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login("admin", driver)
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="", header="", footer=""))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def create_group(self, driver, group):
        # init group creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

        # submit group creation
        driver.find_element_by_name("submit").click()

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, driver):
        # return to groups page
        driver.find_element_by_link_text("group page").click()

    def open_groups_page(self, driver):
        # open groups page
        driver.find_element_by_link_text("groups").click()

    def login(self, username, driver, password="secret"):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("%s" % username)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("%s" % password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("http://localhost/addressbook/index.php")

    
    def tearDown(self):
        self.driver.quit()
