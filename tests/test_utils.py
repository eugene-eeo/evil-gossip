from collections import Counter
from hypothesis import given
import hypothesis.strategies as st
from evil_gossip.utils import edges, full_dist, argmax, sparse_dist


def test_argmax():
    assert argmax(Counter(a=2, b=3)) == 'b'
    assert argmax(Counter(a=1, b=1, c=0)) in ['a', 'b']


@given(st.lists(st.integers(), unique=True))
def test_full_dist(xs):
    x = set(xs)
    for u, v in full_dist(xs):
        assert u not in v
        assert {u} | set(v) == x


@given(st.lists(st.integers(), unique=True))
def test_edges_property(xs):
    v = list(edges(xs))
    s = set(frozenset([a, b]) for a, b in v)
    assert len(v) == len(s)



@given(st.lists(st.integers(), unique=True))
def test_sparse_dist(xs):
    d = dict(sparse_dist(xs))
    for a in d:
        for b in d[a]:
            assert a in d[b]
