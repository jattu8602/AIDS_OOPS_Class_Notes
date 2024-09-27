from collections import Counter

# create set
x = {"a", "b", "c","d"}
print("Initial set:", x)

# add new set
y = {"c"}  # Note: Sets don't allow duplicate values, so "d" will appear only once
x.update(y)
print("After adding new set:", x)

# remove a value (since sets don't support indexing, remove by value)
x.remove("b")
print("After removing 'b':", x)

# to check for duplicate values, we convert the set into a list and use Counter
# (since sets don't have duplicates, we create a sample list with duplicates to demonstrate)
sample_list = ["a", "b", "b", "c", "c", "c"]
duplicates = [item for item, count in Counter(sample_list).items() if count > 1]
b  = set(duplicates)
print("Duplicate values in sample list:", b)










