import pytest

from sixth_seminar.pascal_triangle.pascal_triangle import pascal_triangle


@pytest.mark.parametrize("n, expected", [
    (0, []),
    (1, [[1]]),
    (2, [[1], [1, 1]]),
    (3, [[1], [1, 1], [1, 2, 1]]),
    (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (6, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]),
])
def test_pascal_triangle(n, expected):
    assert pascal_triangle(n) == expected
