from typing import List


def reverse_array_k(nums: List[int], k: int) -> List[int]:
    if len(nums) == 0:
        return []

    k %= len(nums)

    def reverse(left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)

    return nums
