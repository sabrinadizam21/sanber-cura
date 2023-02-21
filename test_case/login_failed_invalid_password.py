import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginFailedPassword(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
    
    def test_a_failed_login_w_invalid_password(self):
        # steps
        driver = self.browser
        # 1. Go to URL
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(3)
        # 2. Click burger button (menu)
        driver.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
         # 3. Click Login menu
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(1)
        # 4. Input Valid Username
        driver.find_element(By.NAME,"username").send_keys("John Doe")
        time.sleep(1)
        # 5. Input invalid Password
        driver.find_element(By.NAME,"password").send_keys("invalidPassword")
        time.sleep(1)
        #6. Click Login button
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)

        # validasi
        errorMessage = driver.find_element(By.CSS_SELECTOR,"p.text-danger").text
        self.assertIn('Login failed! Please ensure the username and password are valid.', errorMessage)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()