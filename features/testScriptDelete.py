import unittest
from selenium import webdriver

class Delete(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../resources/chromedriver.exe')

    def test_read_computer_exist(self):
        computerName = "Blue Dragon"
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
                break

        self.assertTrue(listContainsValue, "List of computers not contain expected value: "+computerName+".")
        searchedElement.click()

        driver.find_element_by_class_name("btn danger").click()

        messageSuccess = driver.find_element_by_xpath("//div[@class='alert-message warning']")
        self.assertEqual(messageSuccess.text,
                         "Done! Computer " + computerName + " has been deleted",
                         "Text from success message not equals text: Done! Computer " + computerName + " has been deleted")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()