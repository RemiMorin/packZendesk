from lib.base import Action


class closeTicket(Action):
    def run(self, ticket_id):
        data = {
            "ticket": {
                "id": ticket_id,
                "status": "closed"
            }
        }  # Create the ticket and get its URL
        return self.zendesk.ticket_update(ticket_id, data=data)
