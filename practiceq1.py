import numpy as np

def left_rotate(arr, n):
"""Left rotate the numpy array by n. Args: arr: The numpy array to rotate. n: The number of times to rotate the array. Returns: The rotated numpy array. """

# Check if the array is empty or if n is invalid.
if not arr or n < 0:
return arr

# Get the length of the array.
length = len(arr)

# Rotate the array by n.
for i in range(n):
# Store the first element of the array.
first = arr[0]

# Shift the elements of the array by one.
for j in range(length - 1):
arr[j] = arr[j + 1]

# Add the first element to the end of the array.
arr[length - 1] = first

# Return the rotated array.
return arr


# Example usage:

arr = np.array([1, 2, 3, 4, 5])
n = 2

rotated_arr = left_rotate(arr, n)

print(rotated_arr) # Output: [3, 4, 5, 1, 2]
