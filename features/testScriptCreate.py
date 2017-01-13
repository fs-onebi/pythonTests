import unittest
from selenium import webdriver

class Create(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../resources/chromedriver.exe')
        self.driver.maximize_window()

    def test_adding_computer(self):
        driver = self.driver
        driver.get("http://computer-database.herokuapp.com/computers")

        computerName = "Blue Dragon"
        introducedDate = "2016-08-10"
        discontinuedDate = "2017-01-05"
        company = "IBM"

        driver.find_element_by_id('add').click()

        header = driver.find_element_by_xpath('//*[@id="main"]/h1')
        self.assertEqual(header.text, 'Add a computer', "Text from success message not equals text: Add a computer.")

        driver.find_element_by_id('name').send_keys(computerName)
        driver.find_element_by_id('introduced').send_keys(introducedDate)
        driver.find_element_by_id('discontinued').send_keys(discontinuedDate)

        selectCompanyList = driver.find_elements_by_xpath("//*[@id='company']/option")
        listContainsValue = False

        for element in selectCompanyList:
            if element.text == company:
                element.click()
                listContainsValue = True
                break
        self.assertTrue(listContainsValue, "There is no element on list named: " + company + ".")

        driver.find_element_by_xpath("//div[@class='actions']/input").click()

        messageSuccess = driver.find_element_by_xpath("//div[@class='alert-message warning']")
        self.assertEqual(messageSuccess.text,
                         "Done! Computer " + computerName + " has been created",
                         "Text from success message not equals text: Done! Computer " + computerName + " has been created.")

        driver.find_element_by_id('searchbox').send_keys(computerName)
        driver.find_element_by_id("searchsubmit").click()

        listContainsValue = False
        listOfComputers = driver.find_elements_by_xpath("//table[contains(@class,'computers')]/tbody/tr/td/a")

        for element in listOfComputers:
            if element.text == computerName:
                listContainsValue = True
                break

        self.assertTrue(listContainsValue, "List of computers not contain expected value: " + computerName + ".")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()