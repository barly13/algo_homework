import pytest
from typing import List

from merge_two_sorted_arrays import merge_two_sorted_arrays, merge_two_sorted_arrays_1


@pytest.mark.parametrize("nums1, nums2, expected", [
    # Базовый случай
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    # Один из массивов пустой
    ([], [1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [], [1, 2, 3]),
    # Оба массива пусты
    ([], [], []),
    # Массивы с одним элементом
    ([1], [2], [1, 2]),
    ([2], [1], [1, 2]),
    # Массивы с повторяющимися элементами
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
    # Массивы с отрицательными числами
    ([-3, -1], [-2, 0], [-3, -2, -1, 0]),
])
def test_merge_two_sorted_arrays(nums1: List[int], nums2: List[int], expected: List[int]):
    assert merge_two_sorted_arrays(nums1.copy(), nums2.copy()) == expected
    assert merge_two_sorted_arrays_1(nums1.copy(), nums2.copy()) == expected

