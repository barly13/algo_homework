import pytest

from sixth_seminar.coin_change.coin_change import coin_change


@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 2, 2),
    ([186, 419, 83, 408], 6249, 20),
    ([1, 2, 5], 100, 20),
    ([2, 3, 7], 12, 3),
    ([5, 10, 25], 30, 2),
])
def test_coin_change(coins, amount, expected):
    assert coin_change(coins, amount) == expected
