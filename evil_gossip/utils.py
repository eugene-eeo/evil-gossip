import random
from operator import itemgetter
from collections import defaultdict


def edges(xs):
    length = len(xs)
    for index, a in enumerate(xs, 1):
        for j in range(index, length):
            yield a, xs[j]


def sparse_dist(xs, p=0.25, entropy=random.random):
    values = defaultdict(list)
    for node, other in edges(xs):
        if entropy() <= p:
            values[node].append(other)
            values[other].append(node)
    return values.items()


def full_dist(xs):
    for node in xs:
        yield node, xs


def argmax(counter):
    return counter.most_common(1)[0][0]
