from collections import defaultdict, Counter
from evil_gossip.simulation import broadcast
from evil_gossip.node import EvilNode


def test_broadcast():
    message = 0
    mailbox = defaultdict(Counter)
    node = EvilNode(message)
    node.links = [1, 2, 3]

    assert broadcast(node, mailbox) == message
    assert mailbox == {
        1: {message: 1},
        2: {message: 1},
        3: {message: 1},
    }


def test_broadcast_empty():
    message = 0
    mailbox = defaultdict(Counter)
    node = EvilNode(message)
    assert broadcast(node, mailbox) is None
