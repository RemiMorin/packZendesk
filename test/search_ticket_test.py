import unittest2
from config import config

from actions.search_ticket import searchTicket
from actions.lib.base import Action
import yaml

class testCreateTicket(unittest2.TestCase):

    def test_search_ticket(self):
        action = searchTicket(config)
        result = action.run(search_string="woop")
        print result
        self.assertTrue(result != None,"result should be defined")
        result = action.run(search_string="status:open")
        print result
        self.assertTrue(result != None,"result should be defined")