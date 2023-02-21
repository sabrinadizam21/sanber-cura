import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
    
    def test_a_success_login(self):
        driver = self.browser
        # 1. Go to URL
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(1)
        # 2. Click burger button (menu)
        driver.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        # 3. Click Login menu
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(1)
        # 4. Input Valid Username
        driver.find_element(By.NAME,"username").send_keys("John Doe")
        time.sleep(1)
        # 5. Input Valid Password
        driver.find_element(By.NAME,"password").send_keys("ThisIsNotAPassword")
        time.sleep(1)
        #6. Click Login button
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(1)

        # validation
        response_data = driver.find_element(By.TAG_NAME,"h2").text
        self.assertIn('Make Appointment', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()