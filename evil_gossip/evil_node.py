class EvilNode:
    __slots__ = ('message', 'links')

    def __init__(self, message):
        self.message = message
        self.links = []

    def broadcast(self):
        for node in self.links:
            yield node, self.message

    def update(self, messages):
        pass
