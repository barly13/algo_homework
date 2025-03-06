import pytest

from reverse_linked_list import ListNode, reverse_linked_list, reverse_linked_list_2


def create_large_linked_list(size):
    head = ListNode(0)
    current = head
    for i in range(1, size):
        current.next = ListNode(i)
        current = current.next
    return head


@pytest.fixture
def large_linked_list():
    return create_large_linked_list(1000000)  # Большой список из миллиона элементов


def test_reverse_linked_list_performance(benchmark, large_linked_list):
    # Тестируем первую функцию
    result = benchmark(reverse_linked_list, large_linked_list)
    assert result is not None  # Проверяем, что результат не пустой


def test_reverse_linked_list_2_performance(benchmark, large_linked_list):
    # Тестируем вторую функцию
    result = benchmark(reverse_linked_list_2, large_linked_list)
    assert result is not None  # Проверяем, что результат не пустой