class EvilNode:
    def __init__(self, id, message, links):
        self.id = id
        self.message = message
        self.links = links

    def broadcast(self):
        print('Evil [%s] broadcasting %s' % (self.id, self.message))
        for node in self.links:
            yield node, self.message

    def update(self, msg):
        pass
