from typing import List


def shell_sort(arr: List[int]) -> List[int]:
    gap = len(arr) // 2

    while gap > 0:
        for current_position in range(gap, len(arr)):
            m_gap = current_position

            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap

        gap = gap // 2

    return arr


# def shell_sort_optimized(arr: List[int]) -> List[int]:
#     n = len(arr)
#     gaps = [701, 301, 132, 57, 23, 10, 4, 1]
#
#     for gap in gaps:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#
#             arr[j] = temp
#
#     return arr