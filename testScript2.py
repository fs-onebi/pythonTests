import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

class CRUD(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_create(self):
        driver = self.driver
        driver.get("http://computer-database.herokuapp.com/computers")

    def test_read(self):
        driver = self.driver
        driver.get("http://www.google.com/")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()