def is_palindrome(a: str) -> bool:
    left = 0
    right = len(a) - 1

    while left < right:
        if a[left] != a[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_2(s: str) -> bool:
    if len(s) == 0:
        return True

    if s[0] != s[-1]:
        return False

    mid = len(s) // 2
    for i in range(mid + 1):
        if s[0 + i] != s[-1 - i]:
            return False

    return True


def is_palindrome_3(s: str) -> bool:
    return s == s[::-1]
