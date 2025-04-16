import random
import string

from extra_letter import extra_letter_1, extra_letter_2


def generate_test_strings(n: int):
    a = ''.join(random.choices(string.ascii_lowercase, k=n))
    extra = random.choice(string.ascii_lowercase)
    b = ''.join(sorted(a + extra))
    return a, b, extra


def test_benchmark_extra_letter_1(benchmark):
    a, b, expected = generate_test_strings(10**6)
    result = benchmark(extra_letter_1, a, b)
    assert result == expected


def test_benchmark_extra_letter_2(benchmark):
    a, b, expected = generate_test_strings(10**6)
    result = benchmark(extra_letter_2, a, b)
    assert result == expected
