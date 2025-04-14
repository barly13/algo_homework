from collections import defaultdict
from typing import List


def two_sum_unsorted(nums: List[int], target: int) -> List[int]:
    variants_dict = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in variants_dict:
            return [variants_dict[diff], i]

        variants_dict[nums[i]] = i

    return []


def group_anagrams(str_list: List[str]) -> List[List[str]]:
    result = defaultdict(list)

    for word in str_list:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        result[tuple(count)].append(word)

    return list(result.values())


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


