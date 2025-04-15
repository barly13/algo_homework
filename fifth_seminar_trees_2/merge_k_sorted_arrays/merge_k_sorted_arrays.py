import heapq
from typing import List


def merge_k_sorted_arrays_1(sorted_arrays: List[List[int]]) -> List[int]:
    heap = []

    for i in range(len(sorted_arrays)):
        for j in range(len(sorted_arrays[i])):
            heapq.heappush(heap, sorted_arrays[i][j])

    merged_array = []
    while heap:
        merged_array.append(heapq.heappop(heap))

    return merged_array


def merge_k_sorted_arrays_2(sorted_arrays: List[List[int]]) -> List[int]:
    merged_array, heap = [], []

    for i in range(len(sorted_arrays)):
        current_array = sorted_arrays[i]

        if current_array:
            heapq.heappush(heap, (current_array[0], i, 0))

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        merged_array.append(value)

        if element_index + 1 < len(sorted_arrays[array_index]):
            next_element = sorted_arrays[array_index][element_index + 1]
            heapq.heappush(heap, (next_element, array_index, element_index + 1))

    return merged_array


print(merge_k_sorted_arrays_2([[1, 2, 5], [4, 5, 8], [7, 99, 101]]))