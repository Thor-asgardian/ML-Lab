from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# using collections.Counter to get count
# of each element in string
all_freq = Counter(test_str)

# printing result
print("Count of all characters in GeeksforGeeks is :\n " + str(all_freq))
