import unittest
from selenium import webdriver
from lib import test_constants

class Read(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(test_constants.CHROMEDRIVER_PATH)
        self.driver.maximize_window()

    def test_read_computer_exist(self):
        computerName = "ASCI Purple"
        driver = self.driver

        driver.get(test_constants.COMPUTER_DATABASE_URL)

        driver.find_element_by_id("searchbox").send_keys(computerName)

        driver.find_element_by_id("searchsubmit").click()

        listContainsValue = False
        searchedElement = ""
        listOfComputers = driver.find_elements_by_xpath("//table[contains(@class,'computers')]/tbody/tr/td/a")

        for element in listOfComputers:
            if element.text == computerName:
                listContainsValue = True
                searchedElement = element
                break

        self.assertTrue(listContainsValue, "List of computers not contain expected value: "+computerName+".")
        searchedElement.click()

        actualComputerName = driver.find_element_by_id("name").get_attribute("value")
        self.assertEqual(computerName, actualComputerName,"Displayed computer name '"+actualComputerName+"' in edit window is not the same as expected '"+computerName+"'.")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()