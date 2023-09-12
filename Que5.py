def max_circular_sum(n, numbers):
    # Function to find the maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_sum = float('-inf')
        current_sum = 0

        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    # Find the maximum subarray sum without considering the circular aspect
    max_sum_linear = kadane(numbers)

    # Find the total sum of the array
    total_sum = sum(numbers)

    # Negate each number and find the maximum subarray sum (inverted)
    inverted_numbers = [-num for num in numbers]
    max_sum_inverted = kadane(inverted_numbers)

    # Calculate the maximum circular sum
    max_circular = total_sum + max_sum_inverted

    # Return the maximum of the linear and circular sums
    return max(max_sum_linear, max_circular)

# Example usage:
n = 5
numbers = [10, -4, 1, 3, 3]
result = max_circular_sum(n, numbers)
print(result)