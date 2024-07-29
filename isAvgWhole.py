# Create a function that takes a list of integers,
# sums the even and odd numbers separately, 
# then returns the difference between the sums of the even and odd numbers.
# Examples

# war_of_numbers([2, 8, 7, 5]) ➞ 2
# # 2 + 8 = 10
# # 7 + 5 = 12
# # 12 is larger than 10
# # So we return 12 - 10 = 2

# war_of_numbers([12, 90, 75]) ➞ 27

# war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168




def is_avg_whole(arr):
    # Sum the elements of the array
    total_sum = sum(arr)
    # Calculate the length of the array
    length = len(arr)
    # Calculate the average
    average = total_sum / length
    # Check if the average is a whole number
    return average.is_integer()
print(is_avg_whole([9, 2, 2, 5]))



def is_avg_whole2(arr):
    # Initialize total_sum to 0
    total_sum = 0
    # Loop through the array and sum the elements
    for num in arr:
        total_sum += num
    # Calculate the length of the array
    length = len(arr)
    # Calculate the average
    average = total_sum / length
    # Check if the average is a whole number
    return average % 1 == 0

# Example usage
print(is_avg_whole2([1, 2, 3, 4]))  # Output: True
print(is_avg_whole2([1, 2, 3]))     # Output: False
