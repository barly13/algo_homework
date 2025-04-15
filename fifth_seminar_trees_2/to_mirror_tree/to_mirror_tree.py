import queue

from fourth_seminar_trees_1.tree_node import TreeNode


def to_mirror_tree_1(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    to_mirror_tree_1(root.left)
    to_mirror_tree_1(root.right)

    return root


def to_mirror_tree_2(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current = q.get()

        current.left, current.right = current.right, current.left

        if current.left:
            q.put(current.left)

        if current.right:
            q.put(current.right)

    return root
