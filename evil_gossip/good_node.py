from collections import Counter
from .utils import random_max


class GoodNode:
    def __init__(self, id, links):
        self.id = id
        self.counter = Counter()
        self.links = links

    @property
    def message(self):
        if not self.counter:
            return None
        return random_max(self.counter)

    def broadcast(self):
        msg = self.message
        if msg is None:
            return
        print('Good [%s] broadcasting %s (%r)' % (self.id, msg, self.counter))
        for node in self.links:
            yield node, msg

    def update(self, messages):
        self.counter.update(messages)
