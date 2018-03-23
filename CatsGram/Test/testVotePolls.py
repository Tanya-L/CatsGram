import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from polls.models import Choice


class SeleniumCatTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        self.driver.refresh()
        self.driver.quit()

class TestVotePolls(SeleniumCatTestCase):

    def __set_field__(self, id, text):
        pass

    def test_vote(self):
        #
        # Given
        #
        self.driver.get("http://127.0.0.1:8000/polls/")

        # How many votes to we have before voting below?
        # Choice.objects.all()
        choice_id = 9
        choice = Choice.objects.get(pk=choice_id)
        votes_before = choice.votes

        #
        # When
        #

        self.driver.find_element_by_name("question1").click()
        # self.driver.find_element_by_id("choice3")
        self.driver.find_element_by_css_selector("input[type='radio'][value='%s']" % choice_id).click()

        self.driver.find_element_by_name("VoteButton").send_keys(Keys.ENTER)

        # self.driver.get("http://127.0.0.1:8000/polls/3/results/")

        #
        # Then
        #
        # assert name == self.driver.find_element_by_id("cat_name").text
        #
        # Count votes after
        choice = Choice.objects.get(pk=choice_id)
        votes_after = choice.votes

        self.assertEquals(votes_after, votes_before+1)
