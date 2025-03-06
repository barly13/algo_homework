from typing import List


def sort_binary_array(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] == 1:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1

        else:
            left += 1

    return nums
