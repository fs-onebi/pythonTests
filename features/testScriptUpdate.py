import unittest
from selenium import webdriver
import sys
sys.path.append('../')
from lib import test_constants

class Update(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(test_constants.CHROMEDRIVER_PATH)
        self.driver.maximize_window()

    def test_update_computer(self):
        computerName = "IBM 7030"
        discontinuedDate = "2015-06-07"

        driver = self.driver
        driver.get("http://computer-database.herokuapp.com/computers")

        driver.find_element_by_id("searchbox").send_keys(computerName)
        driver.find_element_by_id("searchsubmit").click()

        searchedElement = ""
        listOfComputers = driver.find_elements_by_xpath("//table[contains(@class,'computers')]/tbody/tr/td/a")

        for element in listOfComputers:
            if element.text == computerName:
                searchedElement = element
                break

        searchedElement.click()

        driver.find_element_by_id("discontinued").clear()
        driver.find_element_by_id("discontinued").send_keys(discontinuedDate)
        driver.find_element_by_xpath("//div[@class='actions']/input").click()

        message = driver.find_element_by_xpath("//div[@class='alert-message warning']")
        self.assertEqual(message.text,
                          "Done! Computer IBM 7030 has been updated",
                          "Text from success message not equals text: Done! Computer has been updated")
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()