from collections import defaultdict, Counter
from .node import GoodNode, EvilNode


def broadcast(node, mailbox):
    message, receivers = node.broadcast()
    if receivers:
        for recv in receivers:
            mailbox[recv][message] += 1
        return message
    return None


def simulate(n_good, n_evil, has_knowledge, dist, t):
    v = 0
    good = [GoodNode() for _ in range(n_good - has_knowledge)]
    good.extend(GoodNode.with_knowledge(v) for _ in range(has_knowledge))
    evil = [EvilNode(1) for _ in range(n_evil)]

    for node, links in dist(good + evil):
        node.links = links

    T = t
    mailbox = defaultdict(Counter)
    while t > 0:
        all_sent = True
        all_correct = True
        all_wrong = True

        for node in good:
            message = broadcast(node, mailbox)
            if message is None:
                all_wrong = False
                all_correct = False
                all_sent = False
                continue
            if message == v:
                all_wrong = False
            else:
                all_correct = False

        if all_sent:
            if all_correct:
                return (True, T-t)
            if all_wrong:
                break

        for node in evil:
            broadcast(node, mailbox)

        for node, messages in mailbox.items():
            node.update(messages)

        t -= 1
        mailbox.clear()
    return (False, 0)
