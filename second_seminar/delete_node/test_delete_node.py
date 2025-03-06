import pytest

from delete_node import ListNode, delete_node


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


@pytest.mark.parametrize("values, val_to_delete, expected", [
    # Удаление одного узла
    ([1, 2, 3, 4], 3, [1, 2, 4]),
    # Удаление первого узла
    ([1, 2, 3, 4], 1, [2, 3, 4]),
    # Удаление последнего узла
    ([1, 2, 3, 4], 4, [1, 2, 3]),
    # Удаление всех узлов
    ([5, 5, 5], 5, []),
    # Удаление узла, которого нет в списке
    ([1, 2, 3, 4], 5, [1, 2, 3, 4]),
    # Пустой список
    ([], 1, []),
    # Список из одного узла, который нужно удалить
    ([1], 1, []),
    # Список из одного узла, который не нужно удалять
    ([1], 2, [1]),
    # Удаление нескольких узлов с одинаковым значением
    ([1, 2, 2, 3, 2], 2, [1, 3]),
    # Удаление узлов с отрицательными значениями
    ([-1, -2, -3, -4], -3, [-1, -2, -4]),
])
def test_delete_node(values: list, val_to_delete: int, expected: list):
    head = create_linked_list(values)
    new_head = delete_node(head, val_to_delete)
    assert linked_list_to_list(new_head) == expected