import pytest

from typing import List

from group_anagrams import group_anagrams


@pytest.mark.parametrize("str_list, expected", [
    ([], []),
    (["a"], [["a"]]),
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    ([""], [[""]]),
    (["a", "a"], [["a", "a"]]),
    (["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]),
    (["ab", "ba", "abc", "bac", "cab", "cba"], [["ab", "ba"], ["abc", "bac", "cab", "cba"]]),
])
def test_group_anagrams(str_list: List[str], expected: List[List[str]]):
    result = group_anagrams(str_list)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])
