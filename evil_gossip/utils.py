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


def edges(xs):
    for index, a in enumerate(xs, 1):
        for b in xs[index:]:
            yield (a, b)


def sparse_dist(xs, p=0.25):
    values = defaultdict(list)
    for node, other in edges(xs):
        if random.random() <= p:
            values[node].append(other)
            values[other].append(node)
    return values.items()


def full_dist(xs):
    for node in xs:
        yield node, xs
