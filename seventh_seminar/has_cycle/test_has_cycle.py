import pytest

from seventh_seminar.has_cycle.has_cycle import has_cycle


@pytest.mark.parametrize("graph, expected", [
    (
        {
            0: [1],
            1: [0, 2],
            2: [1]
        },
        True
    ),
    (
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        },
        True
    ),
    (
        {
            0: [],
            1: [],
            2: []
        },
        False
    ),
    (
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 0]
        },
        True
    ),
    (
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 1]
        },
        True
    ),
    (
        {
            0: [1, 2],
            1: [0],
            2: [0, 3],
            3: [2]
        },
        True
    ),
])
def test_has_cycle(graph, expected):
    assert has_cycle(graph) == expected
