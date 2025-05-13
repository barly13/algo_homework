from collections import defaultdict


def subarray_sum_equals_k(nums, k):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1

    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]

        prefix_sum[current_sum] += 1

    return count
