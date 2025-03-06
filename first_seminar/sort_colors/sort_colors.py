from typing import List


def sort_colors(nums: List[int]) -> List[int]:
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

    return nums
