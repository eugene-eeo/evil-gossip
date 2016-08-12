from collections import defaultdict
from .good_node import GoodNode
from .evil_node import EvilNode
from .utils import sparse_dist, full_dist


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
    while t > 0:
        mailbox = defaultdict(list)
        good_senders = 0
        all_correct = True
        all_wrong = True

        # `.update` operation is commutative, so whether good
        # or evil nodes broadcast first does not affect results.
        for node in good:
            has_sent = False
            for node, message in node.broadcast():
                has_sent = True
                mailbox[node].append(message)
                all_correct &= message == v
                all_wrong   &= not all_correct
            if has_sent:
                good_senders += 1

        if good_senders == n_good:
            if all_correct:
                return (True, T-t)
            if all_wrong:
                break

        for node in evil:
            for node, message in node.broadcast():
                mailbox[node].append(message)

        for node, messages in mailbox.items():
            node.update(messages)

        t -= 1
    return (False, 0)
