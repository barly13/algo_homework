import pytest

from seventh_seminar.is_bipartite.is_bispartite import is_bipartite


@pytest.mark.parametrize("graph, expected", [
    (
        [],
        True
    ),
    (
        [[]],
        True
    ),
    (
        [[1], [0]],
        True
    ),
    (
        [[1, 2], [0, 2], [0, 1]],
        False
    ),
    (
        [[1, 3], [0, 2], [1, 3], [0, 2]],
        True
    ),
    (
        [[1], [0], [3, 4], [2, 4], [2, 3]],
        False
    ),
    (
        [[1, 2], [0, 3], [0], [1]],
        True
    ),
    (
        [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]],
        False
    ),
    (
        [[1], [0], [3], [2]],
        True
    )
])
def test_is_bipartite(graph, expected):
    assert is_bipartite(graph) == expected
