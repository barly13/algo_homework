import pytest

from eighth_seminar.pivot_index.pivot_index import pivot_index


@pytest.mark.parametrize("nums, expected", [
    (
        [1, 7, 3, 6, 5, 6],
        3
    ),
    (
        [1, 2, 3],
        -1
    ),
    (
        [],
        -1
    ),
    (
        [10],
        0
    ),
    (
        [2, 2, 2, 2, 2],
        2
    ),
    (
        [-1, -1, -1, 0, 1, 1],
        0
    ),
    (
        [1, -1],
        -1
    ),
])
def test_pivot_index(nums, expected):
    assert pivot_index(nums) == expected
