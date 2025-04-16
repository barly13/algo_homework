def binary_search_sqrt_1(target: int) -> int:
    l, r = 0, target

    while l <= r:
        m = l + (r - l) // 2

        if m ** 2 > target:
            r = m - 1
            continue

        if m ** 2 < target:
            l = m + 1
            continue

        return m

    return r


def binary_search_sqrt_2(target: int) -> int:
    return int(target ** 0.5)