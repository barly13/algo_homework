from typing import List
from collections import deque

from fourth_seminar_trees_1.tree_node import TreeNode


def is_max_heap(arr: List[int]) -> bool:
    for i in range((len(arr) - 1) // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(arr) and arr[i] < arr[left]:
            return False

        if right < len(arr) and arr[i] < arr[right]:
            return False

    return True


def is_max_heap_2(root: TreeNode | None) -> bool:
    if not root:
        return True

    queue = deque([root])

    should_be_leaf = False

    while queue:
        current = queue.popleft()

        if current.left:
            if should_be_leaf or current.left.val > current.val:
                return False

            queue.append(current.left)

        else:
            should_be_leaf = True

        if current.right:
            if should_be_leaf or current.right.val > current.val:
                return False

            queue.append(current.right)

        else:
            should_be_leaf = True

    return True