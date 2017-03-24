import json
from evil_gossip import add_links, simulate, full_dist, \
        sparse_dist, allocate


full = full_dist
sparse = lambda p: (lambda xs: sparse_dist(xs, p))
dump = lambda k: print(json.dumps(k))

N = 100
K = 25
t = 1000
conditions = [
    (1.0, 10, 1),
    (1.0, 20, 1),
    (1.0, 30, 1),
    (1.0, 40, 1),
    (1.0, 50, 1),

    (0.001, 10, 20),
    (0.001, 20, 20),
    (0.001, 30, 20),
    (0.001, 40, 20),
    (0.001, 50, 20),

    (0.01, 10, 20),
    (0.01, 20, 20),
    (0.01, 30, 20),
    (0.01, 40, 20),
    (0.01, 50, 20),

    (0.1, 10, 10),
    (0.1, 20, 10),
    (0.1, 30, 10),
    (0.1, 40, 10),
    (0.1, 50, 10),
]


dump(['p', 'B', 'ok', 'ticks'])
for p, B, repeats in conditions:
    dist = full if p == 1.0 else sparse(p)
    for _ in range(repeats):
        P, A = allocate(N, K, B)
        add_links(dist(P + A))
        ok, ticks = simulate(P, A, t)
        dump([p, B, ok, ticks])
