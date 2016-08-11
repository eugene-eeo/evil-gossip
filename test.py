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

from concurrent.futures import ProcessPoolExecutor
from functools import partial
from itertools import repeat

from docopt import docopt
from progressbar import ProgressBar
from evil_gossip import simulate
from evil_gossip.utils import sparse_dist, full_dist, prob


def task(args):
    return simulate(
        n_good=int(args['--good']),
        n_evil=int(args['--evil']),
        has_knowledge=int(args['--has-knowledge']),
        dist=partial(sparse_dist, entropy=prob(0.5)),
        t=int(args['--t']),
    )


def main():
    args = docopt(__doc__)
    repeats = int(args['--repeats'])
    bar = ProgressBar(max_value=repeats)
    res = []

    with ProcessPoolExecutor() as executor:
        for rep, rv in zip(range(repeats), executor.map(task, repeat(args, repeats))):
            res.append(rv)
            bar.update(rep + 1)

    print(res)


if __name__ == '__main__':
    main()
