from typing import List

from fourth_seminar_trees_1.tree_node import TreeNode


def dfs(root: TreeNode | None, result: List[int]):
    if root is None:
        return

    dfs(root.left, result)
    result.append(root.val)
    dfs(root.right, result)


def is_symmetric_dfs(root: TreeNode | None) -> bool:
    if root is None:
        return True

    result = []
    dfs(root, result)

    for i in range(len(result)):
        if result[i] != result[len(result) - i - 1]:
            return False

    return True
