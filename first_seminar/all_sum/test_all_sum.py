from typing import List

import pytest

from all_sum import all_sum, all_sum_1


@pytest.mark.parametrize("nums, expected", [
    # Список c четной длиной
    ([1, 2, 3, 4], 10),
    # Список нечетной длиной
    ([1, 2, 3, 4, 5], 15),
    # Список с одним элементом
    ([7], 7),
    # Пустой список
    ([], 0),
])
def test_all_sum(nums: List[int], expected: int):
    assert all_sum(nums) == expected
    assert all_sum_1(nums) == expected
