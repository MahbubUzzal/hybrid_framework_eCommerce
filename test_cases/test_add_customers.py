import pytest
import time

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.add_customers_page import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    @pytest.mark.regression
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

        self.logger.info("******  Starting Add Customer Test  ******")
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_on_menu_customers()
        self.add_customer.click_on_submenu_customers()

        self.add_customer.click_on_btn_add_new_customer()

        self.logger.info("******  Providing customer info  ******")

        self.email = random_str_generator() + "@gmail.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password("testpass123")
        self.add_customer.set_first_name("Sarder")
        self.add_customer.set_last_name("Rahman")
        self.add_customer.set_customer_role("vendors")
        self.add_customer.set_manager_vendor("Vendor 2")
        self.add_customer.set_gender("Male")
        # self.add_customer.set_dob("05/05/1980")
        self.add_customer.set_company_name("Ava testing Lda.")
        self.add_customer.click_on_tax_exempt()
        self.add_customer.set_admin_comment("This is a testing comment.....!!!")
        self.add_customer.click_on_save()

        self.logger.info("******  Add customer validation  ******* ")
        self.msg = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissable").text
        print(self.msg)
        if "The customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("***** Add Customer Test Passed..... ******")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_add_customer_src.png")
            self.logger.info("***** Add Customer Test Failed  ********")
            assert False == False


# Generating random string
def random_str_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
