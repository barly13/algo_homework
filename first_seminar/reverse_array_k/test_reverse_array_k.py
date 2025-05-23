import pytest
from typing import List

from reverse_array_k import reverse_array_k


@pytest.mark.parametrize("nums, k, expected", [
    # Базовый случай
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    # Сдвиг на длину массива (результат должен быть таким же, как исходный массив)
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    # Сдвиг на 0 (результат должен быть таким же, как исходный массив)
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    # Сдвиг больше длины массива
    ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),  # 7 % 5 = 2
    # Пустой список
    ([], 3, []),
    # Список с одним элементом
    ([10], 2, [10]),  # 2 % 1 = 0
    # Список с отрицательным сдвигом (должен работать как положительный сдвиг)
    ([1, 2, 3, 4, 5], -1, [2, 3, 4, 5, 1]),  # -1 % 5 = 4
    # Список с повторяющимися элементами
    ([4, 4, 4, 4], 2, [4, 4, 4, 4]),
    # Список с отрицательными числами
    ([-1, -2, -3, -4], 3, [-2, -3, -4, -1]),
])
def test_reverse_array_k(nums: List[int], k: int, expected: List[int]):
    assert reverse_array_k(nums, k) == expected
