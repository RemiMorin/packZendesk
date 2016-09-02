from lib.base import Action

class createTicket(Action):

    def run(self,ticket_title,ticket_description, userName, userEmail):
                # Create
        new_ticket = {
            'ticket': {
                'requester': {
                    'name': userName,
                    'email': userEmail,
                },
                'subject':ticket_title,
                'description': ticket_description,
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
        return self.zendesk.ticket_create(data=new_ticket)