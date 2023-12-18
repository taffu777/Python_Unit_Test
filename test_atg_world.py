import unittest
from selenium import webdriver

class TestAtgWorld(unittest.TestCase):
    def setUp(self):
        # Your setup code here
        self.driver = webdriver.Chrome()

    def test_website_loading(self):
        # Your test code here
        self.driver.get("https://atg.world")
        self.assertTrue("ATG" in self.driver.title)

    def tearDown(self):
        # Your teardown code here
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
