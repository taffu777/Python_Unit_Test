import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestAtgWorld(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

  
