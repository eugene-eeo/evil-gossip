"""
Usage:
  test.py [--no-header] [--debug]
  test.py (-h | --help)

Options:
  -h --help    Show this text.
  --no-header  Skip JSONL headers.
  --debug      Show time taken for simulations.
"""

import sys
import json
import time
import evil_gossip
import itertools
from concurrent.futures import ProcessPoolExecutor
from docopt import docopt


def dump(k):
    print(json.dumps(k))


N = 100
K = 25
t = 2000
conditions = [
    (1.0, 10, 1),
    (1.0, 20, 1),
    (1.0, 30, 1),
    (1.0, 40, 1),
    (1.0, 50, 1),

    (0.001, 10, 50),
    (0.001, 20, 50),
    (0.001, 30, 50),
    (0.001, 40, 50),
    (0.001, 50, 50),

    (0.05, 10, 50),
    (0.05, 20, 50),
    (0.05, 30, 50),
    (0.05, 40, 50),
    (0.05, 50, 50),

    (0.01, 10, 50),
    (0.01, 20, 50),
    (0.01, 30, 50),
    (0.01, 40, 50),
    (0.01, 50, 50),

    (0.1, 10, 50),
    (0.1, 20, 50),
    (0.1, 30, 50),
    (0.1, 40, 50),
    (0.1, 50, 50),

    (0.2, 10, 50),
    (0.2, 20, 50),
    (0.2, 30, 50),
    (0.2, 40, 50),
    (0.2, 50, 50),
]


def run_simulation(params):
    return evil_gossip.run(*params)


def main(args):
    if not args['--no-header']:
        dump(['p', 'B', 'immediate', 'ok'])
    with ProcessPoolExecutor() as exe:
        for p, B, repeats in conditions:
            start = time.time()
            results = exe.map(run_simulation, itertools.repeat(
                (N, K, B, p, t),
                repeats,
                ))
            for is_immediate, ok in results:
                dump([p, B, is_immediate, ok])
            end = time.time()
            dt = end - start
            sys.stderr.write('p=%r B=%r t=%r\n' % (p, B, dt))
            sys.stderr.flush()


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
