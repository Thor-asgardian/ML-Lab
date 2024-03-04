import numpy as np

def right_rotate(arr, n):
  """
  Right rotate a numpy array by n positions.

  Args:
    arr: The numpy array to rotate.
    n: The number of positions to rotate the array by.

  Returns:
    The rotated numpy array.
  """

  n = n % len(arr)
  return np.roll(arr, -n)

# Example usage:

arr = np.array([1, 2, 3, 4, 5])
n = 2

rotated_arr = right_rotate(arr, n)

print("Original array:", arr)
print("Rotated array:", rotated_arr)
