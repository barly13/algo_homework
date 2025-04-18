import pytest
from typing import List

from third_seminar.feed_animals.feed_animals import feed_animals


@pytest.mark.parametrize("animals, food, expected", [
    ([], [1, 2, 3], 0),
    ([1, 2, 3], [], 0),
    ([], [], 0),

    ([1, 2, 3], [3, 2, 1], 3),
    ([1, 1, 1], [1, 1, 1], 3),
    ([5, 10, 15], [15, 10, 5], 3),

    ([1, 2, 3], [1, 1], 1),
    ([5, 10, 15], [8, 8, 8], 1),
    ([2, 3, 4], [1, 2, 3], 2),

    ([5, 6, 7], [1, 2, 3], 0),
    ([10], [5], 0),

    ([2, 3], [1, 2, 3, 4, 5], 2),
    ([5], [10, 20, 30], 1),

    ([3], [3], 1),
    ([3], [2], 0),
    ([3], [4], 1),

    ([1000000, 2000000], [1500000, 2500000], 2),
    ([999999], [1000000], 1),
    ([1000000], [999999], 0),

    ([3, 1, 2], [2, 1, 3], 3),
    ([5, 1, 10], [2, 8, 3], 2),

    ([1, 2, 3, 4], [2, 3, 4], 3),
    ([5, 5, 5], [5, 5], 2),
    ([1, 2, 3, 4, 5], [3, 3, 3, 3], 3),
])
def test_feed_animals(animals: List[int], food: List[int], expected: int):
    assert feed_animals(animals, food) == expected
