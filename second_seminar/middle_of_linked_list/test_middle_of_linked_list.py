from typing import Optional

import pytest

from middle_of_linked_list import ListNode, middle_of_linked_list


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def get_node_value(node: Optional[ListNode]):
    return node.val if node else None


@pytest.mark.parametrize("values, expected", [
    # Список с нечетным количеством элементов
    ([1, 2, 3, 4, 5], 3),
    # Список с четным количеством элементов (возвращается второй из двух средних)
    ([1, 2, 3, 4, 5, 6], 4),
    # Пустой список
    ([], None),
    # Список из одного элемента
    ([1], 1),
    # Список из двух элементов
    ([1, 2], 2),
    # Список с отрицательными числами
    ([-1, -2, -3, -4, -5], -3),
    # Список с повторяющимися элементами
    ([1, 1, 1, 1, 1], 1),
])
def test_middle_of_linked_list(values: list, expected: int):
    head = create_linked_list(values)
    middle_node = middle_of_linked_list(head)

    assert get_node_value(middle_node) == expected
