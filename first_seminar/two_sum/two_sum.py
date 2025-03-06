from typing import List


# для неотсортированного массива
def two_sum_unsorted(nums: List[int], target: int) -> List[int]:
    variants_dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in variants_dict:
            return [variants_dict[complement], i]

        variants_dict[nums[i]] = i

    return []


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        target_sum = nums[left] + nums[right]

        if target_sum == target:
            return [left, right]

        elif target_sum > target:
            right -= 1

        else:
            left += 1

    return []
