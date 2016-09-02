import unittest2
from actions.close_ticket import closeTicket
from actions.create_ticket import createTicket
import yaml


class testCreateTicket(unittest2.TestCase):

    def test_close_ticket(self):

        create = createTicket(readConfig('../config.yaml'))
        result = create.run("Example from test",
                            "this ticked was generated automatically from unit test",
                            "Youpi",
                            "woop@mailinator.com")
        print result
        #get the id
        id = result[result.rfind("/") + 1:result.find(".json")]
        action = closeTicket(readConfig('../config.yaml'))
        result = action.run(id)
        print result
        self.assertTrue(result != None,"result should be defined")
        #self.assertTrue(result['ticket']['updated_at'] ... validate updated time)


def readConfig(filename):
    with open(filename, 'r') as stream:
        return yaml.load(stream)
