import random
from collections import Counter, defaultdict
from .node import Acceptor, Proposer


GOOD_MSG = True
EVIL_MSG = False


class Gaplist:
    __slots__ = ('xs', 'hole')

    def __init__(self, xs, hole):
        self.xs = xs
        self.hole = hole

    def __iter__(self):
        for item in self.xs:
            if item != self.hole:
                yield item


def full_dist(xs):
    for v in xs:
        yield v, Gaplist(xs, v)


def sparse_dist(xs, p, entropy=random.random):
    for v, peers in full_dist(xs):
        yield v, [n for n in peers if entropy() <= p]


def allocate(N, K, B):
    B = [Proposer(EVIL_MSG) for _ in range(B)]
    B.extend(Proposer(GOOD_MSG) for _ in range(K))
    N = [Acceptor() for _ in range(N)]
    return B, N


def add_links(source):
    for node, peers in source:
        node.peers = peers


def broadcast(node, mailbox):
    message, peers = node.broadcast()
    if message is not None:
        for p in peers:
            # assert p is not node
            mailbox[p][message] += 1
        return message
    return None


def send_all(mailbox):
    for node, messages in mailbox.items():
        node.update(messages)


def simulate(proposers, acceptors, t=1000):
    mailbox = defaultdict(Counter)
    for i in range(1, t+1):
        assert not mailbox
        # A = []
        all_good = True
        all_evil = True

        for node in acceptors:
            m = broadcast(node, mailbox)
            all_evil &= m == EVIL_MSG
            all_good &= m == GOOD_MSG
            # A.append(m)

        for node in proposers:
            broadcast(node, mailbox)

        send_all(mailbox)
        mailbox.clear()
        # assert all_good == all(m == GOOD_MSG for m in A)
        # assert all_evil == all(m == EVIL_MSG for m in A)
        # if all_good or all_evil: assert all(m != None for m in A)
        if all_good: return True, i
        if all_evil: return False, i
    return False, t


def convergence_check(good, evil, acceptors):
    for node in acceptors:
        m, _ = node.broadcast()
        if m == GOOD_MSG: good += 1
        if m == EVIL_MSG: evil += 1
    return good > evil
