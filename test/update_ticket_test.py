import unittest2
from config import config

from actions.update_ticket import updateTicket
from actions.create_ticket import createTicket
from zdesk import get_id_from_url




class testCreateTicket(unittest2.TestCase):

    def test_create_ticket(self):

        result = createTicket(config).run("Example from test",
                            "this ticked was generated automatically from unit test",
                            "Youpi",
                            "woop@mailinator.com")
        id = get_id_from_url(result)
        action = updateTicket(config)
        result = action.run(id,
                            "Comment generated from unit test")
        print result
        self.assertTrue(result != None,"result should be defined")
        #self.assertTrue(result['ticket']['updated_at'] ... validate updated time)



