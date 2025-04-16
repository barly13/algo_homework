import pytest
from shell_sort import shell_sort


@pytest.mark.parametrize("arr,expected", [
    ([], []),
    ([1], [1]),
    ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([2, 2, 2, 1, 1, 1], [1, 1, 1, 2, 2, 2]),
    ([-5, -1, -3, 0, 4, 2], [-5, -3, -1, 0, 2, 4]),
])
def test_shell_sort(arr, expected):
    assert shell_sort(arr) == expected

