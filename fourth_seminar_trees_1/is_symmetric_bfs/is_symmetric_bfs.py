from fourth_seminar_trees_1.tree_node import TreeNode


def is_symmetric_bfs(root: TreeNode) -> bool:
    if root is None:
        return True

    queue = [root]

    while queue:
        qlen = len(queue)
        for i in range(qlen):
            if queue[i] is None and queue[qlen - i - 1] is None:
                continue

            elif queue[i] is None or queue[qlen - i - 1].left is None:
                return False

            elif queue[i].val != queue[qlen - i - 1].val:
                return False
            
            queue.append(queue[i].left)
            queue.append(queue[i].right)

        queue = queue[qlen:]

    return True