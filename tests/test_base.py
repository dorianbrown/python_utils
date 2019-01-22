from my_utils.base import flatten


def test_flatten():
    assert flatten([['a'], ['b']]) == ['a', 'b']
    assert flatten([[['a'], ['b']], [['a'], ['b']]]) == [['a'], ['b'], ['a'], ['b']]
    assert flatten([[1], [2]]) == [1, 2]

