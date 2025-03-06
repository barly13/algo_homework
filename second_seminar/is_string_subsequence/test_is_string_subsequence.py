import pytest

from is_string_subcequence import is_subsequence


@pytest.mark.parametrize("a, b, expected", [
    # a является подпоследовательностью b
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False),
    # Пустая строка a всегда является подпоследовательностью
    ('', 'ahbgdc', True),
    # Пустая строка b, a не пустая
    ('abc', '', False),
    # Обе строки пустые
    ('', '', True),
    # a равна b
    ('abc', 'abc', True),
    # a длиннее b
    ('abcdef', 'abc', False),
    # a состоит из одного символа, который есть в b
    ('a', 'ahbgdc', True),
    # a состоит из одного символа, которого нет в b
    ('z', 'ahbgdc', False),
    # Повторяющиеся символы в a и b
    ('aabbcc', 'aaabbbccc', True),
    ('aabbcc', 'abcabcabc', False),
    # Символы в a идут в неправильном порядке
    ('acb', 'ahbgdc', False),
])
def test_is_subsequence(a: str, b: str, expected: bool):
    assert is_subsequence(a, b) == expected
