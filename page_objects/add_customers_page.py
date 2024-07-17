import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    lnk_menu_customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_submenu_customers_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_customer_xpath = "//a[normalize-space()='Add new']"

    # selectors for a new customer form
    txt_box_email_xpath = "//input[@id='Email']"
    txt_box_password_xpath = "//input[@id='Password']"
    txt_box_first_name_id = "FirstName"
    txt_box_last_name_id = "LastName"
    btn_gender_male_id = "Gender_Male"
    btn_gender_female_id = "Gender_Female"
    txt_box_dob_xpath = "//input[@id='DateOfBirth']"
    txt_box_company_name_xpath = "//input[@id='Company']"
    chk_box_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    btn_newsletter_xpath = "(//input[@role='searchbox'])[1]"
    lst_newsletter_xpath = "//li[@title='Test store 2']"
    txt_customer_role_xpath = "(//input[@role='searchbox'])[2]"
    lst_customer_role_administrator_id = "select2-SelectedCustomerRoleIds-result-qp6v-1"
    lst_customer_role_forum_moderator_id = "select2-SelectedCustomerRoleIds-result-16i4-2"
    lst_customer_role_registered_id = "select2-SelectedCustomerRoleIds-result-yun5-3"
    lst_customer_role_guest_xpath = "//li[contains(text(),'Guests')]"
    lst_customer_role_vendors_id = "select2-SelectedCustomerRoleIds-result-s54x-5"
    drp_manger_vendor_xpath = "//select[@id='VendorId']"
    chk_box_active_xpath = "//input[@id='Active']"
    txt_box_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_on_menu_customers(self):
        menu_customers = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_menu_customers_xpath)))
        menu_customers.click()

    def click_on_submenu_customers(self):
        submenu_customers = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_submenu_customers_xpath)))
        submenu_customers.click()

    def click_on_btn_add_new_customer(self):
        add_new_customer_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_add_new_customer_xpath)))
        add_new_customer_btn.click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_box_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_box_password_xpath).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element(By.ID, self.txt_box_first_name_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.ID, self.txt_box_last_name_id).send_keys(last_name)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.btn_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.btn_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.btn_gender_male_id).click()

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, self.txt_box_dob_xpath).send_key(dob)

    def set_company_name(self, company_name):
        self.driver.find_element(By.XPATH, self.txt_box_company_name_xpath).send_keys(company_name)

    def click_on_tax_exempt(self):
        self.driver.find_element(By.XPATH, self.chk_box_tax_exempt_xpath).click()

    def set_customer_role(self, role):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.txt_customer_role_xpath))).click()
        time.sleep(5)
        if role == "Administrators":
            self.lst_item = self.wait.until(EC.element_to_be_clickable((By.ID, self.lst_customer_role_administrator_id)))
        elif role == "Registered":
            self.lst_item = self.wait.until(EC.element_to_be_clickable((By.ID, self.lst_customer_role_registered_id)))
        elif role == "Vendors":
            self.lst_item = self.wait.until(EC.element_to_be_clickable((By.ID, self.lst_customer_role_vendors_id)))
        elif role == "Forum Moderators":
            self.lst_item = self.wait.until(EC.element_to_be_clickable((By.ID, self.lst_customer_role_forum_moderator_id)))
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@role='presentation']").click()
            self.lst_item = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lst_customer_role_guest_xpath)))
        else:
            self.lst_item = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lst_customer_role_guest_xpath)))
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", self.lst_item)

    def set_manager_vendor(self, value):
        drp_lst = Select(self.driver.find_element(By.XPATH, self.drp_manger_vendor_xpath))
        drp_lst.select_by_visible_text(value)

    def set_admin_comment(self, comments):
        self.driver.find_element(By.XPATH, self.txt_box_admin_comment_xpath).send_keys(comments)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()















