import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.set_window_size(1200, 900)

    def test_search_in_google(self):
        driver = self.driver
        driver.get('https://www.google.com/')

        # find field
        search_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

        # write
        search_field.send_keys('ibovespa')
        search_field.send_keys(Keys.ENTER)

    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

