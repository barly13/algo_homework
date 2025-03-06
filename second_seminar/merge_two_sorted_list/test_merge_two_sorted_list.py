from typing import Optional

import pytest

from merge_two_sorted_list import merge_two_sorted_lists, ListNode


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# Вспомогательная функция для преобразования связного списка в список значений
def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


@pytest.mark.parametrize("list1_values, list2_values, expected", [
    # Оба списка не пустые
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    # Один список пустой
    ([], [1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [], [1, 2, 3]),
    # Оба списка пустые
    ([], [], []),
    # Списки с одним элементом
    ([1], [2], [1, 2]),
    ([2], [1], [1, 2]),
    # Списки с повторяющимися элементами
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
    # Списки с отрицательными числами
    ([-3, -1], [-2, 0], [-3, -2, -1, 0]),
    # Списки с разной длиной
    ([1, 3, 5, 7], [2, 4], [1, 2, 3, 4, 5, 7]),
    ([2, 4], [1, 3, 5, 7], [1, 2, 3, 4, 5, 7]),
])
def test_merge_two_sorted_lists(list1_values: list, list2_values: list, expected: list):
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    merged_list = merge_two_sorted_lists(list1, list2)
    assert linked_list_to_list(merged_list) == expected
