from fourth_seminar_trees_1.tree_node import TreeNode


def balance_factor(root: TreeNode):
    if not root:
        return 0

    left_height = balance_factor(root.left)
    right_height = balance_factor(root.right)

    return 1 + max(left_height, right_height)