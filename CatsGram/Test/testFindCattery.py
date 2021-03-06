import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumCatTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        self.driver.maximize_window()
        self.driver.refresh()
        self.driver.quit()


class TestFindCattery(SeleniumCatTestCase):

    def __set_field__(self, id, text):
        self.driver.execute_script("document.getElementById('%s').value='%s'" % (id, text))

    def test_search_info_about_cattery(self):
        #
        # Given
        #
        self.driver.get("http://google.com")

        #
        # When
        #
        self.driver.find_element_by_name("q").send_keys("Cattery 'Naked Tails'")
        self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

        #
        # Then
        #
        # assert name == self.driver.find_element_by_id("cat_name").text






