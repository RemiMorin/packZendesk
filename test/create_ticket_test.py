import unittest
from zdesk import Zendesk, get_id_from_url

################################################################
## NEW CONNECTION CLIENT
################################################################
# Manually creating a new connection object
zendesk = Zendesk('https://woophelp.zendesk.com', 'remimorin@gmail.com', 'potatoes12')

# If using an API token, you can create connection object using
# zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'token', True)
# True specifies that the token is being used instead of the password

# See the zdeskcfg module for more sophisticated configuration at
# the command line and via a configuration file.
# https://github.com/fprimex/zdeskcfg


class testCreateTicket(unittest.TestCase):

    def test_create_ticket(self):
        # Create
        new_ticket = {
            'ticket': {
                'requester': {
                    'name': 'Woop Woop',
                    'email': 'woop@mailionator.com',
                },
                'subject':'Not enough woop!',
                'description': 'This is an unclear description of my obscur problem',
                'tags': ['woop', 'Woop-woop'],
                'ticket_field_entries': [
                    {
                        'ticket_field_id': 1,
                        'value': 'venti'
                    },
                    {
                        'ticket_field_id': 2,
                        'value': '$10'
                    }
                ]
            }
        }
        # Create the ticket and get its URL
        result = zendesk.ticket_create(data=new_ticket)

        # Need ticket ID?
        ticket_id = get_id_from_url(result)
        print ticket_id
