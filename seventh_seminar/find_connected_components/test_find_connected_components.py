import pytest

from seventh_seminar.find_connected_components.find_connected_components import find_connected_components


@pytest.mark.parametrize("graph, expected_components", [
    (
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1],
        },
        {0: 1, 1: 1, 2: 1}
    ),
    (
        {
            0: [1],
            1: [0],
            2: []
        },
        {0: 1, 1: 1, 2: 2}
    ),
    (
        {
            0: [],
            1: [],
            2: []
        },
        {0: 1, 1: 2, 2: 3}
    ),
    (
        {
            0: [1],
            1: [0, 2],
            2: [1],
            3: [4],
            4: [3],
        },
        {0: 1, 1: 1, 2: 1, 3: 2, 4: 2}
    ),
    (
        {
            0: []
        },
        {0: 1}
    )
])
def test_find_connected_components(graph, expected_components):
    result = find_connected_components(graph)

    assert len(set(result.values())) == len(set(expected_components.values()))

    for u, v in expected_components.items():
        assert result[u] == v