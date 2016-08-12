from collections import Counter
from .utils import argmax


class GoodNode:
    __slots__ = ('counter', 'links', 'ready')

    def __init__(self):
        self.counter = Counter()
        self.links = []
        self.ready = False

    def broadcast(self):
        if self.ready:
            message = argmax(self.counter)
            for node in self.links:
                yield node, message

    def update(self, messages):
        self.counter.update(messages)
        self.ready |= bool(len(self.counter))

    @classmethod
    def with_knowledge(cls, message):
        node = cls()
        node.update([message])
        return node


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
