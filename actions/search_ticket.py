from lib.base import Action


class searchTicket(Action):

    def run(self,search_string):
        result = self.zendesk.search(query=search_string)
        return result