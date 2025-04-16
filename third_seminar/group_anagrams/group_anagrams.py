from collections import defaultdict
from typing import List


def group_anagrams(str_list: List[str]) -> List[List[str]]:
    result = defaultdict(list)

    for word in str_list:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        result[tuple(count)].append(word)

    return list(result.values())