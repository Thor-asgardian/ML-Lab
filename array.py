import array as arr

# Create an array
arr1 = arr.array('i', [1, 2, 3, 4, 5])

# Add an element to the array
arr1.append(6)

# Insert an element at a specific location
arr1.insert(2, 7)

# Access an element from the array
print(arr1[3])

# Search for an element in the array
print(arr1.index(4))

# Remove an element from the array
arr1.remove(5)

# Print the array
print(arr1)
