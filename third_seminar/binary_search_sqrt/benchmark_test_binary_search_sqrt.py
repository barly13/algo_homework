from binary_search_sqrt import binary_search_sqrt_2, binary_search_sqrt_1


def test_benchmark_binary_search_sqrt_1(benchmark):
    result = benchmark(binary_search_sqrt_1, 10**12)
    assert result == 10**6


def test_benchmark_binary_search_sqrt_2(benchmark):
    result = benchmark(binary_search_sqrt_2, 10**12)
    assert result == 10**6
