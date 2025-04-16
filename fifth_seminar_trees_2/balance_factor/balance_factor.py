from typing import Tuple

from fourth_seminar_trees_1.tree_node import TreeNode


def balance_factor_and_height(root: TreeNode) -> Tuple[int, int]:
    if not root:
        return 0, 0

    left_height, left_balance = balance_factor_and_height(root.left)
    right_height, right_balance = balance_factor_and_height(root.right)

    current_height = 1 + max(left_height, right_height)
    current_balance = left_height - right_height

    return current_height, current_balance
