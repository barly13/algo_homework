from fourth_seminar_trees_1.tree_node import TreeNode


def kth_smallest_bst_1(root: TreeNode | None, k: int) -> int | None:
    stack = []
    counter = 0

    current_node = root

    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        counter += 1

        if counter == k:
            return current_node.val

        current_node = current_node.right

    return None