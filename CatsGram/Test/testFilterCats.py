import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumCatTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        self.driver.refresh()
        self.driver.quit()


class TestFilterCats(SeleniumCatTestCase):

    def __set_field__(self, id, text):
        pass

    def test_cats_should_load_all_cats(self):
        #
        # Given
        #
        self.driver.get("http://127.0.0.1:8000/cattery/cats/")

        #
        # When
        #
        result = self.driver.find_elements_by_class_name("cat_panel_header")

        # self.driver.find_elements_by_name("color")


        #
        # Then
        #
        self.assertGreater(len(result), 0)
