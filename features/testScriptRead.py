import unittest
from selenium import webdriver

class Read(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../resources/chromedriver.exe')

    def test_read_computer_exist(self):
        computerName = "ASCI Purple"
        driver = self.driver

        driver.get("http://computer-database.herokuapp.com/computers")

        driver.find_element_by_id("searchbox").send_keys(computerName)

        driver.find_element_by_id("searchsubmit").click()

        listContainsValue = False
        searchedElement = ""
        listOfComputers = driver.find_elements_by_xpath("//table[contains(@class,'computers')]/tbody/tr/td/a")

        for element in listOfComputers:
            if element.text == computerName:
                listContainsValue = True
                searchedElement = element

        # assert listContainsValue == True
        self.assertTrue(listContainsValue, "List of computers not contain expected value: "+computerName+".")
        searchedElement.click()

        # assert computerName == driver.find_element_by_id("name").get_attribute("value")
        actualComputerName = driver.find_element_by_id("name").get_attribute("value")
        self.assertEqual(computerName, actualComputerName,"Displayed computer name '"+actualComputerName+"' in edit window is not the same as expected '"+computerName+"'.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()