from typing import List

from fourth_seminar_trees_1.tree_node import TreeNode


def build_tree(nums: List[int], i: int) -> TreeNode | None:
    if i >= len(nums):
        return None

    root = TreeNode(nums[i])
    root.left = build_tree(nums, 2 * i + 1)
    root.right = build_tree(nums, 2 * i + 2)

    return root
