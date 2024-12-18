def miniMaxSum(arr):
    # Step 1: Calculate the total sum of the array
    total_sum = sum(arr)
    
    # Step 2: Calculate the sums by excluding one element at a time
    min_sum = float('inf')  # Start with a very large number
    max_sum = float('-inf') # Start with a very small number
    
    for num in arr:
        current_sum = total_sum - num  # Exclude the current number
        min_sum = min(min_sum, current_sum)  # Update the minimum sum
        max_sum = max(max_sum, current_sum)  # Update the maximum sum
    
    # Step 3: Print the results as required
    print(min_sum, max_sum)

# Example usage:
arr = list(map(int, input().split()))  # Taking input as space-separated integers
miniMaxSum(arr)