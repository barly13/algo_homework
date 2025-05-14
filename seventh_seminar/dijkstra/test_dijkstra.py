import pytest

from seventh_seminar.dijkstra.dijkstra import dijkstra


@pytest.mark.parametrize("graph, start, expected", [
    (
        {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        },
        'A',
        {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    ),
    (
        {
            'A': {'B': 2},
            'B': {},
            'C': {'D': 1},
            'D': {}
        },
        'A',
        {'A': 0, 'B': 2, 'C': float('inf'), 'D': float('inf')}
    ),
    (
        # Граф из одной вершины
        {
            'X': {}
        },
        'X',
        {'X': 0}
    ),
    (
        {
            'A': {'B': 1},
            'B': {'C': 1},
            'C': {'A': 1}
        },
        'A',
        {'A': 0, 'B': 1, 'C': 2}
    ),
    (
        {
            'S': {'A': 0, 'B': 0},
            'A': {'C': 0},
            'B': {'C': 0},
            'C': {}
        },
        'S',
        {'S': 0, 'A': 0, 'B': 0, 'C': 0}
    ),
])
def test_dijkstra(graph, start, expected):
    result = dijkstra(graph, start)
    assert result == expected