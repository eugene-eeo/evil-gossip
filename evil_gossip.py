import random
from collections import Counter


def random_max(counter):
    items = sorted(
        counter.items(),
        key=lambda x: x[1],
        reverse=True,
        )
    max_count = items[0][1]
    return random.choice([k for (k,v) in items if v >= max_count])


class GoodNode:
    def __init__(self, id, links):
        self.id = id
        self.counter = Counter()
        self.links   = links

    @property
    def message(self):
        if not self.counter:
            return None
        return random_max(self.counter)

    def broadcast(self):
        msg = self.message
        if msg is None:
            return
        print('good %d broadcasting %s %r' % (self.id, self.message, self.counter))
        for node in self.links:
            yield node, msg

    def update(self, msg):
        self.counter.update([msg])


class BadNode:
    def __init__(self, id, message, links):
        self.id = id
        self.message = message
        self.links = links

    def broadcast(self):
        print('bad %d broadcasting %s' % (self.id, self.message))
        for node in self.links:
            yield node, self.message

    def update(self, msg):
        pass


def simulate(n_good, n_bad, has_knowledge, time):
    v = 0
    good_nodes = [GoodNode(id, []) for id in range(n_good)]
    bad_nodes  = [BadNode(id, 1, []) for id in range(n_bad)]

    knowledgable = good_nodes[:has_knowledge]
    for node in knowledgable:
        node.update(v)

    all_nodes = good_nodes + bad_nodes
    for node in all_nodes:
        node.links += all_nodes

    while time > 0:
        senders = 0
        collect = []
        all_correct = True

        # because of the way we've defined the `update` operation
        # the order of broadcasting doesn't matter.
        for node in good_nodes:
            has_sent = False
            for node, message in node.broadcast():
                has_sent = True
                collect.append((node, message))
                all_correct &= message == v
            if has_sent:
                senders += 1

        if senders == n_good and all_correct:
            return True

        for node in bad_nodes:
            for node, message in node.broadcast():
                collect.append((node, message))

        for node, message in collect:
            node.update(message)

        time -= 1
    return False
