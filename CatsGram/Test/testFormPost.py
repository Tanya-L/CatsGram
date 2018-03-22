import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumCatTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        self.driver.quit()


class TestFormCatUpdate(SeleniumCatTestCase):

    def __set_field__(self, id, text):
        self.driver.execute_script("document.getElementById('%s').value='%s'" % (id, text))

    def test_input_should_change_name_after_update(self):
        #
        # Given
        #
        name = "Bageera%s" % time.time()
        self.driver.get("http://127.0.0.1:8000/cattery/cat/1/")

        #
        # When
        #
        # driver.find_element_by_id("cat_name_input").send_keys("Bageera")
        self.__set_field__("cat_name_input", name)
        self.driver.find_element_by_id("btnK").send_keys(Keys.ENTER)


        #
        # Then
        #
        assert name == self.driver.find_element_by_id("cat_name").text
