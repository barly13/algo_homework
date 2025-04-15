from fourth_seminar_trees_1.tree_node import TreeNode


def min_depth_1(root: TreeNode | None) -> int:
    if not root:
        return 0

    queue = [(root, 1)]

    while queue:
        node, depth = queue.pop(0)

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))

        if node.right:
            queue.append((node.right, depth + 1))


def min_depth_2(root: TreeNode | None) -> int:
    if not root:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is not None and root.right is not None:
        return 1 + min(min_depth_2(root.left), min_depth_2(root.right))

    if root.left is not None:
        return 1 + min_depth_2(root.left)

    if root.right is not None:
        return 1 + min_depth_2(root.right)
