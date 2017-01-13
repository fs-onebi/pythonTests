import unittest
import testScriptDelete
import testScriptRead
import testScriptCreate
import testScriptUpdate

class Test_Suite(unittest.TestCase):
    def test_main(self):

        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(testScriptCreate.Create),
            unittest.defaultTestLoader.loadTestsFromTestCase(testScriptRead.Read),
            unittest.defaultTestLoader.loadTestsFromTestCase(testScriptUpdate.Update),
            unittest.defaultTestLoader.loadTestsFromTestCase(testScriptDelete.Delete)
        ])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)

if __name__ == "__main__":
    unittest.main()