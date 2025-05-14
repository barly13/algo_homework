import pytest

from sixth_seminar.longest_palindrome.longest_palindrome import longest_palindrome


@pytest.mark.parametrize("s, expected", [
    ("", ""),
    ("a", "a"),
    ("aa", "aa"),
    ("ab", "b"),
    ("babad", "aba"),
    ("cbbd", "bb"),
    ("abcd", "d"),
    ("racecar", "racecar"),
    ("abacdfgdcaba", "aba"),
    ("forgeeksskeegfor", "geeksskeeg"),
    ("abcda", "a"),
])
def test_longest_palindrome(s, expected):
    result = longest_palindrome(s)
    assert result == expected or result == expected[::-1]
    assert result == result[::-1]