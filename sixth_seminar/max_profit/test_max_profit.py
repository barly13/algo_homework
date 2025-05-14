import pytest

from sixth_seminar.max_profit.max_profit import max_profit


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2, 3, 4, 5], 4),
    ([2, 4, 1], 2),
    ([3, 3, 3, 3], 0),
    ([1], 0),
    ([5, 2], 0),
    ([2, 1, 4], 3),
    ([1, 2], 1),
    ([2, 1, 2, 1, 2], 1),
])
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected