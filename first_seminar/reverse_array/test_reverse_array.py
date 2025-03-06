import pytest
from typing import List

from reverse_array import reverse_array


@pytest.mark.parametrize("nums, expected", [
    # Базовый случай
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    # Список с одним элементом
    ([10], [10]),
    # Пустой список
    ([], []),
    # Список с четным количеством элементов
    ([6, 7, 8, 9], [9, 8, 7, 6]),
    # Список с нечетным количеством элементов
    ([1, 2, 3], [3, 2, 1]),
    # Список с отрицательными числами
    ([-1, -2, -3], [-3, -2, -1]),
    # Список с повторяющимися элементами
    ([4, 4, 4, 4], [4, 4, 4, 4]),
])
def test_reverse_array(nums: List[int], expected: List[int]):
    assert reverse_array(nums) == expected
