import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import login_success

class TestAddAppointment(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        login_success.TestLogin.test_a_success_login(self)
    
    def test_add_appointment_success(self):
        driver = self.browser
        # 1. Input Facility
        driver.find_element(By.XPATH, "//select[@id=\'combo_facility\']/option[text()='Tokyo CURA Healthcare Center']").click()
        time.sleep(1)
        # 2. Input Healthcare Program
        driver.find_element(By.ID, "radio_program_medicare").click()
        time.sleep(1)
        # 3. Input Visit Date (Required)
        driver.find_element(By.ID, "txt_visit_date").send_keys('08/02/2023')
        time.sleep(1)
        # 4. Input Comment
        driver.find_element(By.ID, "txt_comment").send_keys('Test comment')
        time.sleep(1)
        # 5. Click Book Appointment button
        driver.find_element(By.ID, "btn-book-appointment").click()
        time.sleep(1)

        # validation
        title = driver.find_element(By.TAG_NAME,"h2").text
        self.assertIn('Appointment Confirmation', title)

        # validation submitted data displayed
        facility = driver.find_element(By.CSS_SELECTOR, "p#facility").text
        hospital_readmission = driver.find_element(By.CSS_SELECTOR, "p#hospital_readmission").text
        program = driver.find_element(By.CSS_SELECTOR, "p#program").text
        visit_date = driver.find_element(By.CSS_SELECTOR, "p#visit_date").text
        comment = driver.find_element(By.CSS_SELECTOR, "p#comment").text
        time.sleep(1)
        self.assertIn('Tokyo CURA Healthcare Center', facility)
        self.assertIn('No', hospital_readmission)
        self.assertIn('Medicare', program)
        self.assertIn('08/02/2023', visit_date)
        self.assertIn('Test comment', comment)
        time.sleep(1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()