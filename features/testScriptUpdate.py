import unittest
import time
from selenium import webdriver

class Update(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../resources/chromedriver.exe')
        self.driver.maximize_window()

    def test_adding_computer(self):
        computerName = "IBM 7030"
        discontinuedDate = "2015-06-07"

        driver = self.driver

        driver.get("http://computer-database.herokuapp.com/computers")

        driver.find_element_by_id("searchbox").send_keys(computerName)

        driver.find_element_by_id("searchsubmit").click()
        time.sleep(10)

        searchedElement = ""
        listOfComputers = driver.find_elements_by_xpath("//table[contains(@class,'computers')]/tbody/tr/td/a")

        for element in listOfComputers:
            if element.text == computerName:
                searchedElement = element
                break

        searchedElement.click()

        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()