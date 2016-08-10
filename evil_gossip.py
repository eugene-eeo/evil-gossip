from collections import Counter


class GoodNode:
    def __init__(self, links):
        self.counter = Counter()
        self.links   = links

    @property
    def message(self):
        most_common = self.counter.most_common(1)
        if not most_common:
            return None
        msg, _ = most_common[0]
        return msg

    def broadcast(self):
        msg = self.message
        if msg is None:
            return
        for item in self.links:
            yield item, msg

    def update(self, msg):
        self.counter.update([msg])


class BadNode:
    def __init__(self, message, links):
        self.message = message
        self.links = links

    def broadcast(self):
        for item in self.links:
            yield item, self.message

    def update(self, msg):
        pass



def simulate(n_good, n_bad, has_knowledge, time):
    v = 0
    good_nodes = [GoodNode([]) for _ in range(n_good)]
    bad_nodes  = [BadNode(1, []) for _ in range(n_bad)]

    knowledgable = good_nodes[:has_knowledge]
    knowledgable.update(v)

    while time > 0:
        collect = []
        msgs = []

        # because of the way we've defined the `update` operation
        # the order of broadcasting doesn't matter.
        for node in good_nodes:
            for node, message in node.broadcast():
                collect.append((node, message))
                msgs.append(message)

        if len(msgs) == n_good and all(item == v for item in msgs):
            return 1

        for node in bad_nodes:
            for node, message in node.broadcast():
                collect.append((node, message))

        for node, message in collect:
            node.update(message)

        time -= 1
    return 0
