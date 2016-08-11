"""
Usage:
    evil-gossip -h | --help
    evil-gossip [--good=<n>] [--evil=<n>] [--has-knowledge=<n>] [--t=<n>]
        [--repeats=<n>]

Options:
    --good=<n>           no. of good nodes [default: 100]
    --evil=<n>           no. of evil nodes [default: 10]
    --has-knowledge=<n>  no. of good nodes with knowledge [default: 10]
    -h, --help           show this screen
    --t=<n>              ticks [default: 10]
    --repeats=<n>        no. of repeats [default: 100]
"""

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
        n_good=int(args['--good']),
        n_evil=int(args['--evil']),
        has_knowledge=int(args['--has-knowledge']),
        dist=sparse_dist,
        t=int(args['--t']),
    )


def main():
    args = docopt(__doc__)
    repeats = int(args['--repeats'])
    bar = tqdm(total=repeats)
    res = []

    task_args = {
        'n_good': int(args['--good']),
        'n_evil': int(args['--evil']),
        'has_knowledge': int(args['--has-knowledge']),
        'dist':   partial(sparse_dist, p=0.25),
        't':      int(args['--t']),
    }

    with ProcessPoolExecutor() as executor:
        for rv in executor.map(task, repeat(args, repeats)):
            res.append(rv)
            bar.update(1)
    bar.close()

    success = 0
    failed  = 0
    ticks   = []

    for ok, req in res:
        if ok:
            success += 1
            ticks.append(req)
        else:
            failed += 1

    print()
    print('  failed:    ', failed)
    print('  successful:', success)
    print('  mean ticks:', stats.mean(ticks))
    print()


if __name__ == '__main__':
    main()
