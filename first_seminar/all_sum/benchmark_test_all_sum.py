from all_sum import all_sum, all_sum_1


def test_all_sum_performance(benchmark):
    nums = list(range(1000))
    benchmark(all_sum, nums)


def test_all_sum_1_performance(benchmark):
    nums = list(range(1000))
    benchmark(all_sum_1, nums)