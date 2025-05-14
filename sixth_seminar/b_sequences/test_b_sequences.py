import pytest

from sixth_seminar.b_sequences.b_sequences import b_sequences


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 8),
    (5, 13),
    (6, 21),
    (7, 34),
    (8, 55),
    (9, 89),
    (10, 144),
])
def test_b_sequences(n, expected):
    assert b_sequences(n) == expected
