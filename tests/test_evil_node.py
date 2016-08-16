from evil_gossip.node import EvilNode


def test_broadcast():
    node = EvilNode('m')
    node.links = [1, 2, 3]
    assert node.broadcast() == ('m', [1,2,3])


def test_update():
    node = EvilNode('m')
    node.links = [1, 2, 3]
    before = node.broadcast()
    node.update([])
    assert node.broadcast() == before
