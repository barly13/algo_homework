import pytest

from has_cycle import ListNode, has_cycle, has_cycle_2


def create_large_linked_list_with_cycle(size, cycle_pos):
    nodes = [ListNode(i) for i in range(size)]
    for i in range(size - 1):
        nodes[i].next = nodes[i + 1]

    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


@pytest.fixture
def large_linked_list_with_cycle():
    return create_large_linked_list_with_cycle(1000000, 500000)  # Большой список с циклом


@pytest.fixture
def large_linked_list_without_cycle():
    return create_large_linked_list_with_cycle(1000000, -1)  # Большой список без цикла


def test_has_cycle_performance(benchmark, large_linked_list_with_cycle, large_linked_list_without_cycle):
    # Тестируем на большом списке с циклом
    result = benchmark(has_cycle, large_linked_list_with_cycle)
    assert result

    # Тестируем на большом списке без цикла
    result = benchmark(has_cycle, large_linked_list_without_cycle)
    assert not result


def test_has_cycle_2_performance(benchmark, large_linked_list_with_cycle, large_linked_list_without_cycle):
    # Тестируем на большом списке с циклом
    result = benchmark(has_cycle_2, large_linked_list_with_cycle)
    assert result

    # Тестируем на большом списке без цикла
    result = benchmark(has_cycle_2, large_linked_list_without_cycle)
    assert not result
