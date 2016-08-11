import random
from operator import itemgetter
from collections import defaultdict


def random_max(counter):
    items = sorted(
        counter.items(),
        key=itemgetter(1),
        reverse=True,
        )
    _, max_count = items[0]
    return random.choice([k for (k,v) in items if v >= max_count])


def sparse_dist(xs, p=0.25):
    links = set()
    for node in xs:
        for other in xs:
            if other is node:
                continue
            links.add(frozenset([node, other]))

    values = defaultdict(set)
    for node, other in links:
        if random.random() <= p:
            values[node].add(other)
            values[other].add(node)
    return values.items()


def full_dist(xs):
    for node in xs:
        yield node, xs
