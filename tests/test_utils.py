from collections import Counter
from unittest import TestCase
from evil_gossip.utils import edges, full_dist, argmax


class TestArgmax(TestCase):
    def test_argmax(self):
        assert argmax(Counter(a=2, b=3)) == 'b'
        assert argmax(Counter(a=1, b=1, c=0)) in ['a', 'b']


class TestFullDist(TestCase):
    def test_full_dist(self):
        assert dict(full_dist([1,2,3])) == {
            1: [1, 2, 3],
            2: [1, 2, 3],
            3: [1, 2, 3],
        }


class TestEdges(TestCase):
    def test_edges(self):
        assert list(edges([1, 2, 3])) == [(1, 2), (1, 3), (2, 3)]
