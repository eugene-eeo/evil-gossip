from collections import Counter


def argmax(c):
    key, _ = c.most_common(1)[0]
    return key


class Acceptor:
    __slots__ = ('peers', 'counter')

    def __init__(self):
        self.peers = []
        self.counter = Counter()

    def broadcast(self):
        if self.counter:
            return argmax(self.counter), self.peers
        return None, []

    def update(self, messages):
        self.counter.update(messages)


class Proposer:
    __slots__ = ('peers', 'value')

    def __init__(self, value):
        self.peers = []
        self.value = value

    def broadcast(self):
        return self.value, self.peers

    def update(self, _):
        pass
