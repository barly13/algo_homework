import pytest
from very_simple_task import copy_time


@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (4, 1, 1, 3),
        (1, 1, 1, 1),
        (2, 1, 2, 2),
        (5, 1, 2, 4),
        (3, 2, 3, 5),
        (10, 2, 3, 14),
        (1000000, 1, 2, 666667),
        (1000000, 3, 5, 1875003),
    ]
)
def test_copy_time(n, x, y, expected):
    assert copy_time(n, x, y) == expected
