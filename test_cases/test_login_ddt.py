import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_login:
    base_url = ReadConfig.get_application_url()
    path = ".//test_data//loginData.xlsx"

    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******  Test_002_DDT_login  ******")
        self.logger.info("******  Verifying Login DDT test ******")
        self.driver = setup
        self.driver.get(self.base_url)

        self.login_page = LoginPage(self.driver)  # accessing the methods from LoginPage class
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        # print('Number of Rows in Excel: ', self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.login_page.set_username(self.user)
            self.login_page.set_password(self.password)
            self.login_page.click_login()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp == "pass":
                    self.logger.info("****** Passed  ******")
                    self.login_page.click_logout()
                    lst_status.append("pass")

                elif self.exp == "fail":
                    self.logger.info("****** failed  ******")
                    self.login_page.click_logout()
                    lst_status.append("fail")

            if actual_title != expected_title:
                if self.exp == "pass":
                    self.logger.info("****** failed  ******")
                    lst_status.append("pass")

                elif self.exp == "fail":
                    self.logger.info("****** failed  ******")
                    lst_status.append("pass")

        print(lst_status)
        if "fail" not in lst_status:
            self.logger.info("********  Login DDT test passed   *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("********  Login DDT test failed   *****")
            self.driver.close()
            assert False






