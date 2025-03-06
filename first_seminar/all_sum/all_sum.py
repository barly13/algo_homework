from typing import List


def all_sum(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) % 2 == 0:
        return (nums[0] + nums[-1]) * (len(nums) // 2)

    else:
        return (nums[0] + nums[-1]) * (len(nums) // 2) + nums[len(nums) // 2]


def all_sum_1(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    left, right, answer = 0, len(nums) - 1, 0

    while left < right:
        answer += (nums[left] + nums[right])
        left += 1
        right -= 1

    if left == right:
        answer += nums[left]

    return answer
