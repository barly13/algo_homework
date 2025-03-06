from typing import List
import pytest

from two_sum import two_sum_unsorted, two_sum_sorted


@pytest.mark.parametrize("nums, target, expected", [
    # Базовый случай
    ([2, 7, 11, 15], 9, [0, 1]),
    # Неотсортированный массив
    ([3, 2, 4], 6, [1, 2]),
    # Два одинаковых числа
    ([3, 3], 6, [0, 1]),
    # Нет решения
    ([1, 2, 3, 4], 10, []),
    # Пустой список
    ([], 0, []),
    # Список из одного элемента
    ([5], 5, []),
])
def test_two_sum(nums: List[int], target: int, expected: List[int]):
    assert two_sum_unsorted(nums, target) == expected


@pytest.mark.parametrize("nums, target, expected", [
    # Отсортированный массив
    ([2, 7, 11, 15], 9, [0, 1]),
    ([1, 2, 3, 4], 5, [0, 3]),
    # Два одинаковых числа
    ([3, 3], 6, [0, 1]),
    # Нет решения
    ([1, 2, 3, 4], 10, []),
    # Пустой список
    ([], 0, []),
    # Список из одного элемента
    ([5], 5, []),
])
def test_two_sum_1(nums: List[int], target: int, expected: List[int]):
    assert two_sum_sorted(nums, target) == expected
