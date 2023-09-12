def max_subarray_sum(arr, n):
    max_ending_here = max_so_far = arr[0]  # Initialize variables

    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage:
n = 5
arr = [-2, 2, -3, 4, -1, 5, 4, -5, 4]
result = max_subarray_sum(arr, n)
print(result)
