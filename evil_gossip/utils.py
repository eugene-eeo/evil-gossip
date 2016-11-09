import random
from operator import itemgetter
from collections import defaultdict


def edges(xs):
    length = len(xs)
    for index, a in enumerate(xs, 1):
        for j in range(index, length):
            yield a, xs[j]


def sparse_dist(xs, p=0.25, entropy=random.random):
    links = defaultdict(list)
    for node, other in edges(xs):
        if entropy() <= p:
            links[node].append(other)
            links[other].append(node)
    return links.items()


def full_dist(xs):
    for i, node in enumerate(xs):
        yield node, xs[:i] + xs[i+1:]


def argmax(counter):
    return counter.most_common(1)[0][0]
