from actions.lib.base import Action

from zdesk import Zendesk, get_id_from_url
zendesk = Zendesk('https://woophelp.zendesk.com', 'remimorin@gmail.com', 'potatoes12')

class createTicket(Action):

    def create_ticket(self):
                # Create
        new_ticket = {
            'ticket': {
                'requester': {
                    'name': 'Woop Woop',
                    'email': 'woop@mailionator.com',
                },
                'subject':'Hello world don''t work!',
                'description': 'we try stuff but look like it doesn''t work',
                'tags': ['problem', 'setup'],
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
        pass