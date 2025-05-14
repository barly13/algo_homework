import pytest

from eighth_seminar.max_subarray_sum.max_subarray_sum import max_subarray_sum


@pytest.mark.parametrize("arr, k, expected", [
    (
        [2, 1, 5, 1, 3, 2], 3,
        9
    ),
    (
        [-2, -1, -5, -3, -2], 2,
        -3
    ),
    (
        [0, 0, 0, 0], 2,
        0
    ),
    (
        [1, 2], 3,
        0
    ),
    (
        [5], 1,
        5
    ),
    (
        [4, 4, 4, 4, 4], 3,
        12
    ),
    (
        [], 3,
        0
    )
])
def test_max_subarray_sum(arr, k, expected):
    assert max_subarray_sum(arr, k) == expected
