from collections import Counter
from .utils import random_max


class GoodNode:
    def __init__(self, id):
        self.id = id
        self.counter = Counter()
        self.links = []

    @property
    def message(self):
        if not self.counter:
            return None
        return random_max(self.counter)

    def broadcast(self):
        msg = self.message
        if msg is None:
            return
        for node in self.links:
            yield node, msg

    def __repr__(self):
        return 'Good(%i, %r)' % (self.id, [n.id for n in self.links])

    def update(self, messages):
        self.counter.update(messages)
