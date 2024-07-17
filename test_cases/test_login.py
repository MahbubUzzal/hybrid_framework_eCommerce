import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("******  Test_001_login   ******")
        self.logger.info("******  Verifying home page title   ******")

        self.driver = setup
        self.driver.get(self.base_url)
        try:
            actual_title = self.driver.title
            assert actual_title == "Your store. Login"
            self.logger.info("******  Home page title is passed   ******")

        except Exception:
            self.driver.save_screenshot(".\\screenshots\\test_home_page_title.png")
            self.logger.error("******  Home page title is failed   ******")
            raise

        finally:
            self.driver.close()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******  Verifying Login test ******")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)  # accessing the methods from LoginPage class
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        try:
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            assert actual_title == expected_title
            self.logger.info("******  Login test is passed ******")

        except Exception:
            self.driver.save_screenshot(".\\screenshots\\test_login.png")
            self.logger.error("******  Login test is failed ******")
            raise

        finally:
            self.driver.close()



