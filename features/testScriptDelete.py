import unittest
from selenium import webdriver
from lib import test_constants

class Delete(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(test_constants.CHROMEDRIVER_PATH)

    def test_read_computer_exist(self):
        computerName = "Blue Dragon"
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

        driver.find_element_by_xpath("//input[@value='Delete this computer']").click()

        messageSuccess = driver.find_element_by_xpath("//div[@class='alert-message warning']")

        self.assertEqual(messageSuccess.text,
                         "Done! Computer has been deleted",
                         "Text from success message not equals text: Done! Computer has been deleted")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()