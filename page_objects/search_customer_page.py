from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchCustomer:
    txt_email_id = "SearchEmail"
    txt_first_name_id = "SearchFirstName"
    txt_last_name_id = "SearchLastName"
    btn_search_xpath = "//button[@id='search-customers']"

    table_search_result_xpath = "//div[@class='dataTables_scroll']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    searched_email_xpath = "//table[@id='customers-grid']//tbody/tr/td[2]"
    searched_name_xpath = "//table[@id='customers-grid']//tbody/tr/td[3]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, self.txt_email_id)))
        email_input.clear()  # Clear the input field before entering the email
        email_input.send_keys(email)

    def set_first_name(self, first_name):
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, self.txt_first_name_id)))
        first_name_input.clear()  # Clear the input field before entering the first name
        first_name_input.send_keys(first_name)

    def set_last_name(self, last_name):
        last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, self.txt_last_name_id)))
        last_name_input.clear()  # Clear the input field before entering the last name
        last_name_input.send_keys(last_name)

    def click_on_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_search_xpath)))
        search_button.click()

    def get_number_of_rows(self):
        rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)
        return len(rows)

    def get_number_of_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.table_column_xpath)
        return len(columns)

    def search_customers_by_email(self, email):
        self.set_email(email)
        self.click_on_search()
        rows = self.get_number_of_rows()
        flag = False
        for i in range(1, rows + 1):
            email_xpath = f"//table[@id='customers-grid']//tbody/tr[{i}]/td[2]"
            email_id = self.driver.find_element(By.XPATH, email_xpath).text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customers_by_name(self, name):
        self.set_first_name(name.split()[0])  # Assuming first name
        self.set_last_name(name.split()[-1])  # Assuming last name
        self.click_on_search()
        rows = self.get_number_of_rows()
        flag = False
        for i in range(1, rows + 1):
            name_xpath = f"//table[@id='customers-grid']//tbody/tr[{i}]/td[3]"
            name_searched = self.driver.find_element(By.XPATH, name_xpath).text
            if name_searched == name:
                flag = True
                break
        return flag
