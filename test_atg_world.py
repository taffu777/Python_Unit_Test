import unittest
from selenium import webdriver

class TestAtgWorld(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_website_loading(self):
        self.driver.get("https://atg.world")
        self.assertTrue("ATG" in self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

