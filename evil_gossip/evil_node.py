class EvilNode:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.links = []

    def broadcast(self):
        for node in self.links:
            yield node, self.message

    def update(self, messages):
        pass

    def __repr__(self):
        return 'Evil(%i, %r)' % (self.id, [n.id for n in self.links])
