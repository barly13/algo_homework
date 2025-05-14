import pytest

from seventh_seminar.is_tree.is_tree import is_tree


@pytest.mark.parametrize("graph, start, expected", [
    (
        {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        },
        0,
        True
    ),
    (
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
        0,
        False
    ),
    (
        {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        },
        0,
        False
    ),
    (
        {
            0: []
        },
        0,
        True
    ),
    (
        {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        },
        0,
        False
    ),
    (
        {
            0: [1],
            1: [0, 2, 3],
            2: [1],
            3: [1]
        },
        0,
        True
    )
])
def test_is_tree(graph, start, expected):
    assert is_tree(graph, start) == expected
