from typing import List


def two_sum_unsorted(nums: List[int], target: int) -> List[int]:
    variants_dict = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in variants_dict:
            return [variants_dict[diff], i]

        variants_dict[nums[i]] = i

    return []
