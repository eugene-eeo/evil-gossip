from evil_gossip import add_links, simulate, full_dist, \
        sparse_dist, allocate


full = full_dist
sparse = lambda p: (lambda xs: sparse_dist(xs, p))

N = 100
K = 10
conditions = [
    (full, 10),
    (full, 20),
    (full, 30),
    (full, 40),
    (full, 50),

    (sparse(0.1), 10),
    (sparse(0.1), 20),
    (sparse(0.1), 30),
    (sparse(0.1), 40),
    (sparse(0.1), 50),
]


for dist, B in conditions:
    P, A = allocate(N, K, B)
    add_links(dist(P + A))
    print(simulate(P, A))
