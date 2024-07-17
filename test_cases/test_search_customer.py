import pytest
import time

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.add_customers_page import AddCustomer
from page_objects.search_customer_page import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_SearchCustomer:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_add_customers(self, setup):
        self.logger.info("******  Test_003_AddCustomer   ******")

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)  # accessing the methods from LoginPage class
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("******  Login Successful  ******")

        self.logger.info("****  Starting search customer. by email  ****")

        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_on_menu_customers()
        self.add_customer.click_on_submenu_customers()

        self.logger.info("****  searching customer by email  *****")
        search_customer = SearchCustomer(self.driver)
        search_customer.set_email("asdfg@gmail.com")
        search_customer.click_on_search()
        status = search_customer.search_customers_by_email("asdfg@gmail.com")
        print(status)
        assert status == True
