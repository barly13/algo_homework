import pytest
from extra_letter import extra_letter_1, extra_letter_2


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("abc", "cabd", "d"),
        ("hello", "helloo", "o"),
        ("xyz", "xxyz", "x"),
        ("aabbcc", "abccbaq", "q"),
    ]
)
def test_extra_letter_1(a, b, expected):
    assert extra_letter_1(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("abc", "cabd", "d"),
        ("hello", "helloo", "o"),
        ("xyz", "xxyz", "x"),
        ("aabbcc", "abccbaq", "q"),
    ]
)
def test_extra_letter_2(a, b, expected):
    assert extra_letter_2(a, b) == expected
