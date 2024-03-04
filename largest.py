def find_largest(tuple1):
    max_value = tuple1[0]
    for x in tuple1:
        if x > max_value:
            max_value = x
    return max_value


# Driver code
tuple1 = (10, 20, 4, 5, 6, 7, 8, 9)
print("Largest element is:", find_largest(tuple1))
