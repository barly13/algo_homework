import pytest
from typing import List, Optional

from fourth_seminar_trees_1.build_tree.build_tree import build_tree
from fourth_seminar_trees_1.tree_node import TreeNode


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Вспомогательная функция для преобразования дерева в список (BFS порядок)"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Удаляем лишние None в конце
    while result and result[-1] is None:
        result.pop()

    return result


@pytest.mark.parametrize("nums,expected", [
    # Пустой список
    ([], []),

    # Один элемент
    ([1], [1]),

    # Полное бинарное дерево
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),

    # Неполное бинарное дерево
    ([1, 2, None, 3], [1, 2, None, 3]),
    ([1, None, 3], [1, None, 3]),
    ([1, 2, 3, None, 5], [1, 2, 3, None, 5]),

    # Дерево с None значениями
    ([1, None, None], [1, None, None]),
    ([1, 2, None, None, 5], [1, 2, None, None, 5]),

    # Большое дерево
    ([i for i in range(1, 8)], [1, 2, 3, 4, 5, 6, 7]),

    # Дерево с отрицательными числами
    ([-1, -2, -3], [-1, -2, -3]),

    # Дерево с нулями
    ([0, 0, 0], [0, 0, 0]),
])
def test_build_tree(nums: List[Optional[int]], expected: List[Optional[int]]):
    root = build_tree(nums, 0)
    assert tree_to_list(root) == expected


@pytest.mark.parametrize("nums,start_idx,expected", [
    # Начало с индекса 0
    ([1, 2, 3], 0, [1, 2, 3]),

    # Начало с индекса 1 (поддерево)
    ([1, 2, 3, 4, 5], 1, [2, 4, 5]),

    # Начало с индекса 2 (поддерево)
    ([1, 2, 3, 4, 5, 6, 7], 2, [3, 6, 7]),

    # Начало с индекса за пределами списка
    ([1, 2, 3], 10, []),
])
def test_build_tree_with_start_index(nums: List[int], start_idx: int, expected: List[int]):
    root = build_tree(nums, start_idx)
    assert tree_to_list(root) == expected