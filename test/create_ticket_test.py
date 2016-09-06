import unittest2
from actions.create_ticket import createTicket
from config import config



class testCreateTicket(unittest2.TestCase):

    def test_create_ticket(self):

        action = createTicket(config)
        result = action.run("Example from test",
                            "this ticked was generated automatically from unit test",
                            "Youpi",
                            "woop@mailinator.com")
        print result
        self.assertTrue(result != None,"result should be defined")
        self.assertTrue('zendesk.com/api/v2/tickets/' in result,"result should be an url pointing to created resource")



