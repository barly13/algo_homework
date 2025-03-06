import pytest

from is_palindrom import is_palindrome, is_palindrome_2, is_palindrome_3


@pytest.fixture
def long_palindrome():
    return 'a' * 1000000  # Длинный палиндром


@pytest.fixture
def long_non_palindrome():
    return 'a' * 999999 + 'b'  # Длинная строка, не являющаяся палиндромом


def test_is_palindrome_performance(benchmark, long_palindrome, long_non_palindrome):
    # Тестируем на длинном палиндроме
    result = benchmark(is_palindrome, long_palindrome)
    assert result == True

    # Тестируем на длинной строке, не являющейся палиндромом
    result = benchmark(is_palindrome, long_non_palindrome)
    assert result == False


def test_is_palindrome_2_performance(benchmark, long_palindrome, long_non_palindrome):
    # Тестируем на длинном палиндроме
    result = benchmark(is_palindrome_2, long_palindrome)
    assert result

    # Тестируем на длинной строке, не являющейся палиндромом
    result = benchmark(is_palindrome_2, long_non_palindrome)
    assert not result


def test_is_palindrome_3_performance(benchmark, long_palindrome, long_non_palindrome):
    # Тестируем на длинном палиндроме
    result = benchmark(is_palindrome_3, long_palindrome)
    assert result

    # Тестируем на длинной строке, не являющейся палиндромом
    result = benchmark(is_palindrome_3, long_non_palindrome)
    assert not result
