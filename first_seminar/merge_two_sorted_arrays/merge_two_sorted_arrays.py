from typing import List


def merge_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    pointer1 = len(nums1) - 1
    pointer2 = len(nums2) - 1
    pointer3 = len(nums1) + len(nums2) - 1

    for i in range(pointer1, pointer3):
        nums1.append(0)

    while pointer2 >= 0:
        if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
            nums1[pointer3] = nums1[pointer1]
            pointer1 -= 1

        else:
            nums1[pointer3] = nums2[pointer2]
            pointer2 -= 1

        pointer3 -= 1

    return nums1


def merge_two_sorted_arrays_1(nums1: List[int], nums2: List[int]) -> List[int]:
    merged_array = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i += 1

        else:
            merged_array.append(nums2[j])
            j += 1

    if i < len(nums1):
        merged_array.extend(nums1[i:])

    else:
        merged_array.extend(nums2[j:])

    return merged_array
