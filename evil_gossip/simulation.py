from collections import defaultdict
from .good_node import GoodNode
from .evil_node import EvilNode


def simulate(n_good, n_evil, has_knowledge, t):
    v = 0

    good = [GoodNode(id, [])    for id in range(n_good)]
    evil = [EvilNode(id, 1, []) for id in range(n_evil)]

    knowledgable = good[:has_knowledge]
    for node in knowledgable:
        node.update([v])

    all_nodes = good + evil
    for node in all_nodes:
        node.links += all_nodes

    while t > 0:
        mailbox = defaultdict(list)
        good_senders = 0
        all_correct = True

        # `.update` operation is commutative, so whether good
        # or evil nodes broadcast first does not affect results.
        for node in good:
            has_sent = False
            for node, message in node.broadcast():
                has_sent = True
                mailbox[node].append(message)
                all_correct &= message == v
            if has_sent:
                good_senders += 1

        if good_senders == n_good and all_correct:
            return True

        for node in evil:
            for node, message in node.broadcast():
                mailbox[node].append(message)

        for node, messages in mailbox.items():
            node.update(messages)

        t -= 1
    return False
