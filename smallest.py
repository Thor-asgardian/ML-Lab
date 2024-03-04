def find_smallest_item(tuple1):
  """Finds the smallest item in a tuple.

  Args:
    tuple1: A tuple of items.

  Returns:
    The smallest item in the tuple.
  """

  smallest_item = tuple1[0]
  for item in tuple1:
    if item < smallest_item:
      smallest_item = item

  return smallest_item


# Example usage:

tuple1 = (1, 2, 3, 4, 5)
smallest_item = find_smallest_item(tuple1)
print(smallest_item)
