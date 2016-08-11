"""
Usage:
    evil-gossip -h | --help
    evil-gossip [--good=<n>] [--evil=<n>] [--has-knowledge=<n>] [--t=<n>]
        [--repeats=<n>] [--full | --sparse=<p>]

Options:
    --good=<n>           no. of good nodes [default: 100]
    --evil=<n>           no. of evil nodes [default: 10]
    --has-knowledge=<n>  no. of good nodes with knowledge [default: 10]
    -h, --help           show this screen
    --t=<n>              ticks [default: 10]
    --repeats=<n>        no. of repeats [default: 100]
    --sparse=<p>         sparse connections [default: 0.25]
    --full               fully connect nodes
"""

from __future__ import print_function

import statistics as stats
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from itertools import repeat

from docopt import docopt
from tqdm import tqdm
from evil_gossip import simulate
from evil_gossip.utils import sparse_dist, full_dist


def task(args):
    return simulate(
        n_good=args['n_good'],
        n_evil=args['n_evil'],
        has_knowledge=args['has_knowledge'],
        dist=full_dist if args['full'] else partial(sparse_dist, p=args['p']),
        t=args['t'],
    )


def main():
    args = docopt(__doc__)
    repeats = int(args['--repeats']) if not args['--full'] else 1
    bar = tqdm(total=repeats)

    task_args = {
        'n_good': int(args['--good']),
        'n_evil': int(args['--evil']),
        'has_knowledge': int(args['--has-knowledge']),
        'full':   args['--full'],
        'p':      None if args['--full'] else float(args['--sparse']),
        't':      int(args['--t']),
    }

    success = 0
    failed  = 0
    ticks   = []

    with ProcessPoolExecutor() as executor:
        for rv in executor.map(task, repeat(task_args, repeats)):
            ok, req = rv
            if ok:
                success += 1
                ticks.append(req)
            else:
                failed += 1
            bar.update(1)
    bar.close()

    print()
    print('  failed:    ', failed)
    print('  successful:', success)
    print('  mean ticks:', stats.mean(ticks) if len(ticks) > 0 else '-')
    print()


if __name__ == '__main__':
    main()
