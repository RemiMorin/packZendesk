import unittest2
from actions.create_ticket import createTicket
import yaml


class testCreateTicket(unittest2.TestCase):

    def test_create_ticket(self):

        action = createTicket(readConfig('../config.yaml'))
        result = action.run("Example from test","this ticked was generated automatically from unit test")
        print result
        self.assertTrue(result != None,"result should be defined")


def readConfig(filename):
    with open(filename, 'r') as stream:
        return yaml.load(stream)
