import unittest2

from actions.search_ticket import searchTicket
from actions.lib.base import Action
import yaml

class testCreateTicket(unittest2.TestCase):

    def test_search_ticket(self):
        action = searchTicket(readConfig('../config.yaml'))
        result = action.run(search_string="woop")
        print result
        self.assertTrue(result != None,"result should be defined")
        result = action.run(search_string="status:open")
        print result
        self.assertTrue(result != None,"result should be defined")

def readConfig(filename):
    with open(filename, 'r') as stream:
       return yaml.load(stream)