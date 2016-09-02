import unittest

from actions.search_ticket import searchTicket
from actions.lib.base import Action

class testCreateTicket(unittest.TestCase):

    def test_search_ticket(self):
        test = searchTicket(Action({}));
        result = test.run(search_string="woop")
        print result

        result = test.run(search_string="status:open")
        print result