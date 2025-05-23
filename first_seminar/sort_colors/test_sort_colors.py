from typing import List

import pytest

from sort_colors import sort_colors


@pytest.mark.parametrize("nums, expected", [
    # Базовый случай
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    # Все элементы уже на своих местах
    ([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]),
    # Все элементы — нули
    ([0, 0, 0], [0, 0, 0]),
    # Все элементы — единицы
    ([1, 1, 1], [1, 1, 1]),
    # Все элементы — двойки
    ([2, 2, 2], [2, 2, 2]),
    # Пустой список
    ([], []),
    # Список из одного элемента
    ([0], [0]),
    ([1], [1]),
    ([2], [2]),
    # Список с двумя элементами
    ([0, 1], [0, 1]),
    ([1, 2], [1, 2]),
    ([0, 2], [0, 2]),
    # Список с повторяющимися элементами
    ([1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1]),
])
def test_sort_colors(nums: List[int], expected: List[int]):
    assert sort_colors(nums) == expected
