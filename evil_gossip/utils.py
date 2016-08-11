import random
from operator import itemgetter


def random_max(counter):
    items = sorted(
        counter.items(),
        key=itemgetter(1),
        reverse=True,
        )
    _, max_count = items[0]
    return random.choice([k for (k,v) in items if v >= max_count])
