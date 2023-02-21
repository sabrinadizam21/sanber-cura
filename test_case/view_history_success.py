import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import login_success

class TestViewHistoryPage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        login_success.TestLogin.test_a_success_login(self)
    
    def test_view_history_success(self):
        driver = self.browser
        # 1. Click burger button (menu)
        driver.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        # 2. Click History button
        driver.find_element(By.LINK_TEXT, "History").click()
        time.sleep(1)
       
        # validation
        title = driver.find_element(By.TAG_NAME,"h2").text
        self.assertIn('History', title)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()