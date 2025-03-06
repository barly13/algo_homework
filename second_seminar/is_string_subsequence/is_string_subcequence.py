def is_subsequence(a: str, b: str) -> bool:
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1

        j += 1

    return i == len(a)