import timeit
import random

from fifth_seminar_trees_2.is_max_heap.is_max_heap import is_max_heap, is_max_heap_2
from fourth_seminar_trees_1.tree_node import TreeNode


def generate_max_heap_array(size):
    arr = [random.randint(0, 1000) for _ in range(size)]
    arr.sort(reverse=True)
    return arr


def generate_non_max_heap_array(size):
    arr = [random.randint(0, 1000) for _ in range(size)]
    arr[0], arr[-1] = arr[-1], arr[0]  # Делаем некорректной
    return arr


def array_to_tree(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]
    for i in range(len(nodes)):
        if nodes[i] and 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if nodes[i] and 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


# Подготовка тестовых данных
sizes = [10, 100, 1000, 10000]
test_cases = []

for size in sizes:
    # Корректные кучи
    valid_arr = generate_max_heap_array(size)
    valid_tree = array_to_tree(valid_arr)

    # Некорректные кучи
    invalid_arr = generate_non_max_heap_array(size)
    invalid_tree = array_to_tree(invalid_arr)

    test_cases.append((valid_arr, valid_tree, True))
    test_cases.append((invalid_arr, invalid_tree, False))

for arr, tree, expected in test_cases:
    size = len(arr)

    array_time = timeit.timeit(
        lambda: is_max_heap(arr),
        number=100
    )

    tree_time = timeit.timeit(
        lambda: is_max_heap_2(tree),
        number=100
    )

    print(f"Размер: {size}")
    print(f"Массив: {array_time:.6f} сек (100 итераций)")
    print(f"Дерево: {tree_time:.6f} сек (100 итераций)")
    print(f"Отношение (дерево/массив): {tree_time / array_time:.2f}x")