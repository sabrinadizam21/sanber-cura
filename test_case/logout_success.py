import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import login_success

class TestLogout(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        login_success.TestLogin.test_a_success_login(self)
    
    def test_a_success_logout(self):
        driver = self.browser        
        driver.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(1)

        # validation
        title = driver.find_element(By.TAG_NAME,"h1").text
        self.assertIn('CURA Healthcare Service', title)

        # validation if login button displayed
        driver.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Login").is_displayed
        time.sleep(1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()