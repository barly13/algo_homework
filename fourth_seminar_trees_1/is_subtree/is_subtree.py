from fourth_seminar_trees_1.is_same_tree.is_same_tree import is_same_tree_1
from fourth_seminar_trees_1.tree_node import TreeNode


def is_subtree(root: TreeNode | None, subtree: TreeNode | None) -> bool:
    if not subtree:
        return True

    if not root:
        return False

    if is_same_tree_1(root, subtree):
        return True

    return is_subtree(root.left, subtree) or is_subtree(root.right, subtree)