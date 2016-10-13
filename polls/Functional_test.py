__author__ = 'hola'

import unittest
from selenium import webdriver

class BuscoAyudaTest(unittest.TestCase):
    """docstring for ."""
    def setUp(self):
        self.browser = webdriver.Firefox()

    def  tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get("127.0.0.1:8000")
        self.assertIn('Busco Ayuda', self.browser.title)


if __name__ == '__main__':
    unittest.main()
