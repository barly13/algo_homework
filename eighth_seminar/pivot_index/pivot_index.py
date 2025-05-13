from typing import List


def pivot_index(nums: List[int]) -> int:
    total_sum = 0
    left_sum = 0

    for i in range(len(nums)):
        total_sum += nums[i]

    for i in range(len(nums)):
        if left_sum == total_sum - left_sum - nums[i]:
            return i

        left_sum += nums[i]

    return -1
