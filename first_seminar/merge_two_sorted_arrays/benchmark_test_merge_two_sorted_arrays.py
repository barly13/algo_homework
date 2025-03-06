import pytest
from merge_two_sorted_arrays import merge_two_sorted_arrays, merge_two_sorted_arrays_1


@pytest.fixture
def large_nums1():
    return list(range(1, 10001))


@pytest.fixture
def large_nums2():
    return list(range(10001, 20001))


def test_merge_two_sorted_arrays_performance(benchmark, large_nums1, large_nums2):
    result = benchmark(merge_two_sorted_arrays, large_nums1.copy(), large_nums2.copy())
    assert result == list(range(1, 20001))


def test_merge_two_sorted_arrays_1_performance(benchmark, large_nums1, large_nums2):
    result = benchmark(merge_two_sorted_arrays_1, large_nums1.copy(), large_nums2.copy())
    assert result == list(range(1, 20001))
