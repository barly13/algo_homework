import pytest
from typing import List

from zeros_back import zeros_back


@pytest.mark.parametrize("nums, expected", [
    # Базовый случай
    ([5, 0, 3, 0, 8, 0, 1], [5, 3, 8, 1, 0, 0, 0]),
    # Все элементы уже на своих местах
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    # Все элементы — нули
    ([0, 0, 0], [0, 0, 0]),
    # Пустой список
    ([], []),
    # Список из одного ненулевого элемента
    ([5], [5]),
    # Список из одного нуля
    ([0], [0]),
    # Список с отрицательными числами
    ([-1, 0, -2, 0, -3], [-1, -2, -3, 0, 0]),
])
def test_move_zeros_to_end(nums: List[int], expected: List[int]):
    assert zeros_back(nums) == expected
