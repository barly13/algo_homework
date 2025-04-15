def copy_time(n: int, x: int, y: int) -> int:
    l = 0
    r = (n - 1) * max(x, y)

    while l + 1 < r:
        m = (l + r) // 2

        if m // x + m // y < n - 1:
            l = m

        else:
            r = m

    return r + min(x, y)
