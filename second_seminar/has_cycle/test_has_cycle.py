import pytest

from has_cycle import ListNode, has_cycle, has_cycle_2


def create_linked_list_with_cycle(values, cycle_pos):
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


@pytest.mark.parametrize("values, cycle_pos, expected", [
    # Список без цикла
    ([1, 2, 3, 4], -1, False),
    # Список с циклом
    ([1, 2, 3, 4], 1, True),
    # Пустой список
    ([], -1, False),
    # Список из одного элемента без цикла
    ([1], -1, False),
    # Список из одного элемента с циклом (сам на себя)
    ([1], 0, True),
    # Список с циклом в конце
    ([1, 2, 3, 4], 3, True),
    # Список с циклом в середине
    ([1, 2, 3, 4, 5], 2, True),
])
def test_has_cycle(values: list, cycle_pos: int, expected: bool):
    head = create_linked_list_with_cycle(values, cycle_pos)
    assert has_cycle(head) == expected
    assert has_cycle_2(head) == expected
