def extra_letter_1(a: str, b: str) -> str:
    count = {}

    for c in a:
        count[c] = count.get(c, 0) + 1

    for c in b:
        if c in count:
            count[c] -= 1

            if count[c] == 0:
                del count[c]
                continue

            continue

        return c

    return ''


def extra_letter_2(a: str, b: str) -> str:
    res = 0

    for c in a + b:
        res ^= ord(c)

    return chr(res)