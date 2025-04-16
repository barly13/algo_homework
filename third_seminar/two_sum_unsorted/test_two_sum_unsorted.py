from typing import List

import pytest

from two_sum_unsorted import two_sum_unsorted


@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),       # 2 + 7 = 9
    ([3, 2, 4], 6, [1, 2]),            # 2 + 4 = 6
    ([3, 3], 6, [0, 1]),              # 3 + 3 = 6
    ([1, 2, 3, 4], 8, []),            # Нет подходящей пары
    ([0, 4, 3, 0], 0, [0, 3]),        # 0 + 0 = 0
    ([-1, -2, -3, -4, -5], -8, [2, 4]), # -3 + -5 = -8
    ([5, 75, 25], 100, [1, 2])        # 75 + 25 = 100
])
def test_two_sum_unsorted(nums: List[int], target: int, expected: List[int]):
    result = two_sum_unsorted(nums, target)
    assert result == expected
