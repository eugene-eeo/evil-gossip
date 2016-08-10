from collections import Counter


class Node:
    def __init__(self, links):
        self.counter = Counter()
        self.links   = links

    def message(self):
        msg, _ = self.counter.most_common(1)
        return msg

    def send(self):
        for item in self.links:
            item.update(self.message)

    def update(self, msg):
        self.counter.update([msg])
