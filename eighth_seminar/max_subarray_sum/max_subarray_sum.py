def max_subarray_sum(arr, k):
    if len(arr) < k:
        return 0

    current_sum = 0
    for i in range(k):
        current_sum += arr[i]

    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(current_sum, max_sum)

    return max_sum