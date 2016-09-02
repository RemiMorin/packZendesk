from zdesk import Zendesk, get_id_from_url

__all__ = [
    'Action'
]

class Action(object):
    def __init__(self, config):
        self.config = config
        self.zendesk = Zendesk(self.config['url'],self.config['user'],self.config['password'])
