def main():
    # List Operations
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)

    # Insert
    my_list.append(6)

    # Update
    my_list[0] = 0

    # Delete
    del my_list[1]

    # Display
    print("List after operations:", my_list)

    # Sorting
    my_list.sort()
    print("Sorted List:", my_list)

    # Searching
    search_item = 3
    if search_item in my_list:
        print(f"{search_item} found in the list.")
    else:
        print(f"{search_item} not found in the list.")

    # Tuple Operations
    my_tuple = (1, 2, 3, 4, 5)
    print("\nOriginal Tuple:", my_tuple)

    # Display
    print("Tuple:", my_tuple)

    # Set Operations
    my_set = {1, 2, 3, 4, 5}
    print("\nOriginal Set:", my_set)

    # Insert
    my_set.add(6)

    # Delete
    my_set.remove(1)

    # Display
    print("Set after operations:", my_set)

    # Dictionary Operations
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("\nOriginal Dictionary:", my_dict)

    # Insert/Update
    my_dict['d'] = 4

    # Delete
    del my_dict['a']

    # Display
    print("Dictionary after operations:", my_dict)

    # Sorting (for dictionary)
    sorted_dict = dict(sorted(my_dict.items()))
    print("Sorted Dictionary:", sorted_dict)


if __name__ == "__main__":
    main()
