def dfs(left, right):
    if not left or not right:
        return 0

    count = 0

    if left.val == right.val:
        count = 1

    count += dfs(left.left, right.right)
    count += dfs(left.right, right.left)

    return count


def count_mirror_twins(root):
    if not root:
        return 0

    return dfs(root.left, root.right)