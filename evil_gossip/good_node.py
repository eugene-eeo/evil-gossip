from collections import Counter


class GoodNode:
    __slots__ = ('counter', 'links')

    def __init__(self):
        self.counter = Counter()
        self.links = []

    @property
    def message(self):
        if not self.counter:
            return None
        message, _ = self.counter.most_common(1)[0]
        return message

    def broadcast(self):
        msg = self.message
        if msg is None:
            return
        for node in self.links:
            yield node, msg

    def __repr__(self):
        return 'Good(%r)' % ([n.id for n in self.links],)

    def update(self, messages):
        self.counter.update(messages)
