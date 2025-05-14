import pytest

from eighth_seminar.subarray_sum_equals_k.subarray_sum_equals_k import subarray_sum_equals_k


@pytest.mark.parametrize("nums, k, expected", [
    (
        [1, 1, 1], 2,
        2
    ),
    (
        [1, 2, 3], 6,
        1
    ),
    (
        [-1, -1, 1], 0,
        1
    ),
    (
        [], 0,
        0
    ),
    (
        [5], 5,
        1
    ),
    (
        [1, 1, 1, 1, 1], 3,
        3
    ),
    (
        [10, 5, 1, -1, 0, 5, 2], 5,
        3
    ),
    (
        [-1, -2, -3, 1, 2, 3], 0,
        2
    )
])
def test_subarray_sum_equals_k(nums, k, expected):
    assert subarray_sum_equals_k(nums, k) == expected
