import pytest

from sixth_seminar.find_lis.find_lis import find_lis


@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 1),
    ([1, 2, 1, 2, 3], 3),
    ([1, 3, 2, 4, 3, 5], 2),
    ([10, 20, 10, 30, 40, 5, 6], 3),
    ([1, 2, 3, 2, 3, 4], 3),
])
def test_find_lis(nums, expected):
    assert find_lis(nums) == expected
