from typing import List


def find_lis(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1

    return max(dp)