"""
Usage:
  test.py [--no-header]
  test.py (-h | --help)

Options:
  -h --help    Show this text.
  --no-header  Skip JSONL headers.
"""

import sys
import json
from evil_gossip import run
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


def main(args):
    if not args['--no-header']:
        dump(['p', 'B', 'immediate', 'ok'])
    for p, B, repeats in conditions:
        for _ in range(repeats):
            is_immediate, ok = run(N, K, B, p, t)
            dump([p, B, is_immediate, ok])


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
