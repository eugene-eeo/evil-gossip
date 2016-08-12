from collections import Counter
from evil_gossip.utils import edges, full_dist, argmax, sparse_dist


def test_argmax():
    assert argmax(Counter(a=2, b=3)) == 'b'
    assert argmax(Counter(a=1, b=1, c=0)) in ['a', 'b']


def test_full_dist():
    assert dict(full_dist([1,2,3])) == {
        1: [1, 2, 3],
        2: [1, 2, 3],
        3: [1, 2, 3],
    }


def test_edges():
    assert list(edges([1, 2, 3])) == [(1, 2), (1, 3), (2, 3)]


def test_edges_property():
    v = list(edges([1, 2, 3, 4, 5]))
    s = set(frozenset([a, b]) for a, b in v)
    assert len(v) == len(s)
