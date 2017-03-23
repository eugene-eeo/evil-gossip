import random
from collections import Counter, defaultdict


GOOD_MSG = True
EVIL_MSG = False


def argmax(c):
    key, _ = c.most_common(1)[0]
    return key


class Acceptor:
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
    def __init__(self, value):
        self.peers = []
        self.value = value

    def broadcast(self):
        return self.value, self.peers

    def update(self, _):
        pass


def full_dist(xs):
    for i, v in enumerate(xs):
        yield v, xs[:i] + xs[i+1:]


def sparse_dist(xs, p, entropy=random.random):
    for node, peers in full_dist(xs):
        yield node, [p for p in peers if entropy() <= p]


def allocate(N, K, B):
    B = [Proposer(EVIL_MSG) for _ in range(B)]
    B.extend(Proposer(GOOD_MSG) for _ in range(K))
    N = [Acceptor() for _ in range(N)]
    return B, N


def add_links(nodes):
    for node, peers in full_dist(nodes):
        node.peers = peers


def broadcast(node, mailbox):
    message, peers = node.broadcast()
    if message is not None:
        for p in peers:
            mailbox[p][message] += 1
        return message
    return None


def update_all(mailbox):
    for receiver in mailbox:
        receiver.update(mailbox[receiver])


def simulate(proposers, acceptors, t=500):
    mailbox = defaultdict(Counter)
    for i in range(1, t+1):
        #A = []
        all_sent = True
        all_good = True
        all_evil = True

        for node in acceptors:
            m = broadcast(node, mailbox)
            all_sent &= m is not None
            all_evil &= m == EVIL_MSG
            all_good &= m == GOOD_MSG
            #A.append(m)

        for node in proposers:
            broadcast(node, mailbox)

        update_all(mailbox)
        mailbox.clear()
        #assert all_good == all(m == GOOD_MSG for m in A)
        #assert all_evil == all(m == EVIL_MSG for m in A)
        if all_sent:
            if all_good: return True, i
            if all_evil: return False, i
    return False, t
