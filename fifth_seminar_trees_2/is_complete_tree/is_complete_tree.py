import queue

from fourth_seminar_trees_1.tree_node import TreeNode


def is_complete_tree(root: TreeNode | None) -> bool:
    if not root:
        return True

    q = queue.Queue([root])
    seen_null = False

    while queue:
        node = q.popleft()

        if not node:
            seen_null = True

        else:
            if seen_null:
                return False

            q.append(node.left)
            q.append(node.right)

    return True