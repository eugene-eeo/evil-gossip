from .simulation import add_links, allocate, sparse_dist, \
        full_dist, simulate, convergence_check


def run(neutral, good, evil, p, t):
    P, A = allocate(neutral, good, evil)
    add_links(
        full_dist(P + A) if p == 1.0 else
        sparse_dist(P + A, p)
        )
    win, ticks = simulate(P, A, t)
    return (
       (convergence_check(good, evil, A), t) if not win and ticks == t else
       (win, ticks)
       )
