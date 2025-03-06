import pytest

from is_palindrom import is_palindrome, is_palindrome_2, is_palindrome_3


@pytest.mark.parametrize("s, expected", [
    # Палиндромы
    ('deed', True),
    ('madam', True),
    ('level', True),
    ('a', True),
    ('', True),  # Пустая строка считается палиндромом
    # Не палиндромы
    ('hello', False),
    ('world', False),
    ('python', False),
    # Палиндромы с разным регистром (должны быть чувствительны к регистру)
    ('Deed', False),
    ('Madam', False),
    # Палиндромы с пробелами и символами
    ('A man a plan a canal Panama', False),  # С пробелами и символами
    ("No 'x' in Nixon", False),  # С символами
])
def test_is_palindrome(s: str, expected: bool):
    assert is_palindrome(s) == expected
    assert is_palindrome_2(s) == expected
    assert is_palindrome_3(s) == expected
