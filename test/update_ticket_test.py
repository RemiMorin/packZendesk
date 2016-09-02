import unittest2
from actions.update_ticket import updateTicket
import yaml


class testCreateTicket(unittest2.TestCase):

    def test_create_ticket(self):

        action = updateTicket(readConfig('../config.yaml'))
        result = action.run(7,
                            "Comment generated from unit test")
        print result
        self.assertTrue(result != None,"result should be defined")
        #self.assertTrue(result['ticket']['updated_at'] ... validate updated time)


def readConfig(filename):
    with open(filename, 'r') as stream:
        return yaml.load(stream)
