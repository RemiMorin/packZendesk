from lib.base import Action

class updateTicket(Action):

    def run(self, ticket_id, comment):
        data = {
            "ticket": {
                "id": ticket_id,
                "comment": {
                    "public": True,
                    "body": comment
                }
            }
        }
        # Create the ticket and get its URL
        return self.zendesk.ticket_update(ticket_id,data=data)
        return 42