from evil_gossip.node import EvilNode


def test_broadcast():
    node = EvilNode('m')
    node.links = [1, 2, 3]
    assert dict(node.broadcast()) == {
        1: 'm',
        2: 'm',
        3: 'm',
    }


def test_update():
    node = EvilNode('m')
    node.links = [1, 2, 3]
    before = dict(node.broadcast())
    node.update([])
    assert dict(node.broadcast()) == before
