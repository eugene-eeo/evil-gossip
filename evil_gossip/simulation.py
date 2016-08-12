from collections import defaultdict, Counter
from .good_node import GoodNode
from .evil_node import EvilNode


def broadcast(node, mailbox):
    message = None
    for recv, message in node.broadcast():
        mailbox[recv][message] += 1
    return message


def simulate(n_good, n_evil, has_knowledge, dist, t):
    v = 0
    good = [GoodNode() for _ in range(n_good)]
    evil = [EvilNode(1) for _ in range(n_evil)]

    knowledgable = good[:has_knowledge]
    for node in knowledgable:
        node.update([v])

    for node, links in dist(good + evil):
        node.links = links

    T = t
    mailbox = defaultdict(Counter)
    while t > 0:
        all_sent = True
        all_correct = True
        all_wrong = True

        # `.update` operation is commutative, so whether good
        # or evil nodes broadcast first does not affect results.
        for node in good:
            message = broadcast(node, mailbox)
            if message is not None:
                all_correct &= message == v
                all_wrong &= message != v
                continue
            else:
                all_wrong = False
                all_correct = False
                all_sent = False

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
