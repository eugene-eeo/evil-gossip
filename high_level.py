from sys import stdout
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from itertools import repeat, product
from json import dumps

from evil_gossip.simulation import simulate
from evil_gossip.utils import sparse_dist, full_dist


def emit(cols):
    print(dumps(cols))
    def j(data):
        print(dumps([data[col] for col in cols]))
        stdout.flush()
    return j


def multiples_of(start, end, multiple, non_zero=True):
    def gen(start):
        while True:
            if not non_zero or start != 0:
                yield start
            start += multiple
            if start > end:
                break
    return list(gen(start))


def tasks(n_good, n_evil, has_knowledge, probs, t):
    for ng, ne, hk, p, t_ in product(n_good, n_evil, has_knowledge, probs, t):
        yield {
            'n_good': ng,
            'n_evil': ne,
            'has_knowledge': hk,
            'p': p,
            't': t_,
        }


def execute(args):
    return simulate(
        n_good=args['n_good'],
        n_evil=args['n_evil'],
        has_knowledge=args['has_knowledge'],
        dist=full_dist if args['p'] == 1.0 else partial(sparse_dist, p=args['p']),
        t=args['t'],
        )


def run(n_good, n_evil, has_knowledge, prob, t, repeats=1000):
    j = emit(['n_good', 'n_evil', 'has_knowledge', 'p', 't', 'passed', 'failed', 'ticks_distribution'])
    with ProcessPoolExecutor() as executor:
        for param in tasks(n_good, n_evil, has_knowledge, prob, t):
            reps = 1 if param['p'] == 1.0 else repeats
            dist = Counter()
            passed = 0
            failed = 0
            for ok, ticks in executor.map(execute, repeat(param, reps)):
                if ok:
                    passed += 1
                    dist[ticks] += 1
                else:
                    failed += 1
            param.update({
                'ticks_distribution': dist,
                'passed': passed,
                'failed': failed,
            })
            j(param)
