from fourth_seminar_trees_1.tree_node import TreeNode


def is_same_tree_1(tree1: TreeNode | None, tree2: TreeNode | None) -> bool:
    if not tree1 and not tree2:
        return True

    if tree1 and tree2 and tree1.val == tree2.val:
        return is_same_tree_1(tree1.left, tree2.left) and is_same_tree_1(tree1.right, tree2.right)

    return False


def is_same_tree_2(tree1: TreeNode | None, tree2: TreeNode | None) -> bool:
    stack = [(tree1, tree2)]

    while stack:
        node1, node2 = stack.pop()

        if not node1 and not node2:
            continue

        if not node1 and not node2 or node1.val != node2.val:
            return False

        stack.append((node1.right, node2.right))
        stack.append((node1.left, node2.left))

    return True