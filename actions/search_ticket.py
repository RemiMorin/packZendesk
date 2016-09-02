from lib.base import Action
import urllib

from zdesk import Zendesk, get_id_from_url
zendesk = Zendesk('https://woophelp.zendesk.com', 'remimorin@gmail.com', 'potatoes12')

class searchTicket(Action):

    def run(self,search_string):
        result = zendesk.search(query=search_string)
        return result