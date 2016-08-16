from collections import Counter
from evil_gossip.node import GoodNode


def test_update_emtpy():
    node = GoodNode()
    node.update({})
    assert not node.ready


def test_update_non_emtpy():
    node = GoodNode()
    node.update(Counter(a=1, b=2))
    assert node.ready
    assert node.counter == {'a': 1, 'b': 2}

    node.update(Counter(a=2))
    assert node.counter == {'a': 3, 'b': 2}


def test_with_knowledge():
    node = GoodNode.with_knowledge(1)
    assert node.ready
    assert node.counter == {1: 1}


def test_broadcast():
    node = GoodNode.with_knowledge(1)
    node.links = [1, 2]
    assert node.broadcast() == (1, [1, 2])
