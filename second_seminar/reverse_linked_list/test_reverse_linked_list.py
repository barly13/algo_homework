import pytest

from reverse_linked_list import ListNode, reverse_linked_list, reverse_linked_list_2


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.mark.parametrize("values, expected", [
    # Базовый случай
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    # Пустой список
    ([], []),
    # Список из одного элемента
    ([1], [1]),
    # Список из двух элементов
    ([1, 2], [2, 1]),
    # Список с отрицательными числами
    ([-1, -2, -3], [-3, -2, -1]),
    # Список с повторяющимися элементами
    ([1, 1, 1], [1, 1, 1]),
])
def test_reverse_linked_list(values: list, expected: list):
    # Тестируем первую функцию
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)

    assert linked_list_to_list(reversed_head) == expected

    # Тестируем вторую функцию
    head = create_linked_list(values)  # Создаем список заново
    reversed_head_2 = reverse_linked_list_2(head)

    assert linked_list_to_list(reversed_head_2) == expected
