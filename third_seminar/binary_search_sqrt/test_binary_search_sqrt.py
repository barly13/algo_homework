import pytest
from binary_search_sqrt import binary_search_sqrt_1, binary_search_sqrt_2


@pytest.mark.parametrize(
    "target, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (100, 10),
        (999, 31),
        (1024, 32),
        (123456789, 11111),
        (10**12, 10**6),
    ]
)
def test_binary_search_sqrt_1(target, expected):
    assert binary_search_sqrt_1(target) == expected


@pytest.mark.parametrize(
    "target, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (100, 10),
        (999, 31),
        (1024, 32),
        (123456789, 11111),
        (10**12, 10**6),
    ]
)
def test_binary_search_sqrt_2(target, expected):
    assert binary_search_sqrt_2(target) == expected
